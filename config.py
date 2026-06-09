import os
from dotenv import load_dotenv

load_dotenv()

# Azure OpenAI settings
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY", "").strip()
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT", "").strip()
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview").strip()
AZURE_OPENAI_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4o-mini").strip()

# Google Drive credentials
CREDENTIALS_FILE = r"C:\Users\manchems\Downloads\client_secret_502256482410-r3f9hms5kmebspvmmr1actt9gncfc9lv.apps.googleusercontent.com.json"
TOKEN_FILE = "token.json"
