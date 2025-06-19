import vertexai
from vertexai import agent_engines

# 配置项
PROJECT_ID = "ever-443501"
LOCATION = "us-central1"
STAGING_BUCKET = "gs://beebi-agent"

# 1. 初始化 Vertex AI 环境
vertexai.init(
    project=PROJECT_ID,
    location=LOCATION,
    staging_bucket=STAGING_BUCKET
)

# 2. 连接到已经部署好的远程 Agent（用 resource_name）
# 👉 替换为你自己的 resource_name！
DEPLOYED_AGENT_RESOURCE_NAME = "projects/159224617767/locations/us-central1/reasoningEngines/10528923347582976"

remote_app = agent_engines.get(resource_name=DEPLOYED_AGENT_RESOURCE_NAME)

# 3. 创建远程 session
remote_session = remote_app.create_session(user_id="test_user")
print(f"🔗 远程 session 创建成功: {remote_session['id']}")

# 4. 向 agent 发送消息
def ask(message):
    print(f"\n💬 你问: {message}")
    for event in remote_app.stream_query(
        user_id="test_user",
        session_id=remote_session["id"],
        message=message,
    ):
        print(f"🤖 Agent 回复: {event}")

# 5. 示例：问时间和天气
ask("what's the time in new york")
ask("what's the weather in new york")
