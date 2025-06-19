# deploy.py
from vertexai import agent_engines
import vertexai
from beebi.agent import root_agent
from vertexai.preview import reasoning_engines
import os
os.environ["DISABLE_DB"] = "true"

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
    agent=root_agent,
    enable_tracing=True,  # 可选，便于调试
)
    # 部署到 Agent Engine
remote_app = agent_engines.create(
    agent_engine=root_agent,
    requirements=[
        "google-cloud-aiplatform[adk,agent_engines]",
    ],

)
print("Deployed agent resource name:", remote_app.resource_name)


