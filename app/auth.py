import requests
from flask import session, redirect, url_for, request
from urllib.parse import urlencode
from config import settings  # Import the centralized settings

def initiate_auth_flow():
    """
    Redirect the user to Home Assistant's OAuth authorization page.
    """
    params = {
        'client_id': settings.CLIENT_ID,
        'redirect_uri': settings.REDIRECT_URI
    }
    # Redirect user to Home Assistant's authorization page
    return redirect(f"{settings.HOME_ASSISTANT_URL}/auth/authorize?{urlencode(params)}")

def exchange_code_for_token(code):
    """
    Exchange the authorization code for an access and refresh token.
    """
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'client_id': settings.CLIENT_ID
    }
    response = requests.post(settings.TOKEN_URL, data=data)
    
    if response.status_code == 200:
        tokens = response.json()
        # Store tokens in session or a secure place
        session['access_token'] = tokens.get('access_token')
        session['refresh_token'] = tokens.get('refresh_token')
        return True
    else:
        return False

def is_user_authenticated():
    """
    Check if the user is authenticated by verifying the presence and validity of the access token.
    """
    access_token = session.get('access_token')
    if not access_token:
        return False
    # Here, you can add additional checks on the access token, such as verifying its expiration
    return True
