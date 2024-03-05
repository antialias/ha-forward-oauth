import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Home Assistant settings
HOME_ASSISTANT_URL = os.getenv('HOME_ASSISTANT_URL', 'http://your-homeassistant-instance.com')
CLIENT_ID = os.getenv('CLIENT_ID', 'https://your-forward-auth-service.io')
REDIRECT_URI = os.getenv('REDIRECT_URI', 'https://your-forward-auth-service.io/callback')

# Authentication service settings
SECRET_KEY = os.getenv('SECRET_KEY', 'your_random_secret_key_here')
TOKEN_URL = f"{HOME_ASSISTANT_URL}/auth/token"

# Additional settings as needed
# For example, logging configuration, external API keys, etc.
