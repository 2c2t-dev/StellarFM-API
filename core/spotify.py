import requests
import os
import base64

def get_access_token():
    credentials = f"{os.getenv('SPOTIFY_ID')}:{os.getenv('SPOTIFY_SECRET')}"
    key = base64.b64encode(credentials.encode('ascii')).decode('ascii')
    headers = {
        "Authorization": f"Basic {key}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials"
    }
    response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        return None