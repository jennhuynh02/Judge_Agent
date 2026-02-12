import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Mock Mode - Set to True to use mock responses without API keys
USE_MOCK = os.getenv("USE_MOCK", "true").lower() == "true"

# API Keys - Loaded from .env file
GPTZERO_API_KEY = os.getenv("GPTZERO_API_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# API Endpoints
GPTZERO_ENDPOINT = "https://api.gptzero.me/v2/predict/text"
OPENAI_ENDPOINT = "https://api.openai.com/v1/chat/completions"

# Model Configuration
GPT_MODEL = "gpt-4o"
