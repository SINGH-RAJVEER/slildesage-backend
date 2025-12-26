import os
from dotenv import load_dotenv

load_dotenv()

class ConfigAI:
    LITELLM_MODEL = os.getenv('LITELLM_MODEL')
    LITELLM_PROXY_URL = os.getenv('LITELLM_PROXY_URL')
    
    DEBUG = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    CORS_ORIGINS = os.getenv('CORS_ORIGINS')
