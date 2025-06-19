# run_server.py
from vertexai import agent_engines, init
from beebi.agent import root_agent
import vertexai

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

# ✅ 包装正式 agent（含数据库功能）
app = agent_engines.AdkApp(agent=root_agent, enable_tracing=True)

# 创建会话
session = app.create_session(user_id="user_daniel")
print("🧠 会话创建成功:", session.id)

# 用户提问：开始交互
for event in app.stream_query(
    user_id="user_daniel",
    session_id=session.id,
    message="how's my sleep in the past 7 days?",
):
    print("🤖", event)

# 如果你要关闭
# remote_app.delete(force=True)
