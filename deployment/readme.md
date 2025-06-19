ADK Short Bot
A Python-based agent that helps shorten messages using Google's Agent Development Kit (ADK) and Vertex AI.

Prerequisites
Python 3.12+
Poetry (Python package manager)
Google Cloud account with Vertex AI API enabled
Google Cloud CLI (gcloud) installed and authenticated
Follow the official installation guide to install gcloud
After installation, run gcloud init and gcloud auth login
Installation
Clone the repository:
git clone https://github.com/bhancockio/deploy-adk-agent-engine.git
cd adk-short-bot
Install Poetry if you haven't already:
curl -sSL https://install.python-poetry.org | python3 -
Install project dependencies:
poetry install
Activate the virtual environment:
source $(poetry env info --path)/bin/activate
Configuration
Create a .env file in the project root with the following variables:
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=your-location  # e.g., us-central1
GOOGLE_CLOUD_STAGING_BUCKET=gs://your-bucket-name
Set up Google Cloud authentication:
gcloud auth login
gcloud config set project your-project-id
Enable required APIs:
gcloud services enable aiplatform.googleapis.com
Usage
Local Testing
Create a new session:
poetry run deploy-local --create_session
List all sessions:
poetry run deploy-local --list_sessions
Get details of a specific session:
poetry run deploy-local --get_session --session_id=your-session-id
Send a message to shorten:
poetry run deploy-local --send --session_id=your-session-id --message="Shorten this message: Hello, how are you doing today?"
Remote Deployment
Deploy the agent:
poetry run deploy-remote --create
Create a session:
poetry run deploy-remote --create_session --resource_id=your-resource-id
List sessions:
poetry run deploy-remote --list_sessions --resource_id=your-resource-id
Send a message:
poetry run deploy-remote --send --resource_id=your-resource-id --session_id=your-session-id --message="Hello, how are you doing today? So far, I've made breakfast today, walkted dogs, and went to work."
Clean up (delete deployment):
poetry run deploy-remote --delete --resource_id=your-resource-id
Project Structure
adk-short-bot/
├── adk_short_bot/          # Main package directory
│   ├── __init__.py
│   ├── agent.py           # Agent implementation
│   └── prompt.py          # Prompt templates
├── deployment/            # Deployment scripts
│   ├── local.py          # Local testing script
│   └── remote.py         # Remote deployment script
├── .env                  # Environment variables
├── poetry.lock          # Poetry lock file
└── pyproject.toml       # Project configuration
Development
To add new features or modify existing ones:

Make your changes in the relevant files
Test locally using the local deployment script
Deploy to remote using the remote deployment script
Update documentation as needed
Troubleshooting
If you encounter authentication issues:

Ensure you're logged in with gcloud auth login
Verify your project ID and location in .env
Check that the Vertex AI API is enabled
If deployment fails:

Check the staging bucket exists and is accessible
Verify all required environment variables are set
Ensure you have the necessary permissions in your Google Cloud project
Contributing
Fork the repository
Create a feature branch
Make your changes
Submit a pull request
License
[Your chosen license]