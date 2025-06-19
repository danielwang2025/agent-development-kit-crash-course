import vertexai
from vertexai import agent_engines

# 初始化 Vertex AI
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

# 获取远程 agent
remote_app = agent_engines.get(resource_name=DEPLOYED_AGENT_RESOURCE_NAME)

# 删除 agent
remote_app.delete(force=True)
print("✅ Agent 删除成功")
