import vertexai
from vertexai import agent_engines
from vertexai.preview import reasoning_engines
from beebi.agent import deployment_stub_agent
from basic_agent.greeting_agent.agent import sleep_analysis_agent as root_agent

# 配置项
PROJECT_ID = "ever-443501"
LOCATION = "us-central1"
STAGING_BUCKET = "gs://beebi-agent"

# 初始化 Vertex AI
vertexai.init(
    project=PROJECT_ID,
    location=LOCATION,
    staging_bucket=STAGING_BUCKET,
)

# 包装 agent 以便部署
app = reasoning_engines.AdkApp(
    agent=deployment_stub_agent,
    enable_tracing=True,  # 可选，便于调试
)

# 本地测试（可选）
if __name__ == "__main__":
    # 本地 session 测试
    session = app.create_session(user_id="u_123")
    print("Local session:", session)
    for event in app.stream_query(
        user_id="u_123",
        session_id=session.id,
        message="whats last 7days sleep",
    ):
        print("Local event:", event)

    # 部署到 Agent Engine
    remote_app = agent_engines.create(
        agent_engine=root_agent,
        requirements=[
            "google-cloud-aiplatform[adk,agent_engines]",
        ],
    
    )
    print("Deployed agent resource name:", remote_app.resource_name)

    # 远程 session 测试
    remote_session = remote_app.create_session(user_id="u_456")
    print("Remote session:", remote_session)
    for event in remote_app.stream_query(
        user_id="u_456",
        session_id=remote_session["id"],
        message="what's last 7 days sleep",
    ):
        print("Remote event:", event)

    # 清理资源（可选）
#remote_app.delete(force=True)
