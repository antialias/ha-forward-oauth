from flask import Flask, request, redirect, url_for, session
from app.auth import initiate_auth_flow, exchange_code_for_token, is_user_authenticated
import os
from config import settings  # Import the centralized settings

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = settings.SECRET_KEY  # Use the secret key from settings

@app.route('/auth')
def auth():
    # Check if user is authenticated
    if not is_user_authenticated():
        return initiate_auth_flow()
    return 'Authenticated', 200

@app.route('/callback')
def callback():
    code = request.args.get('code')
    if code and exchange_code_for_token(code):
        # Redirect to a confirmation or directly to the protected resource
        return redirect(settings.CLIENT_ID)
    else:
        return 'Failed to authenticate', 401

if __name__ == '__main__':
    app.run(port=5000)
