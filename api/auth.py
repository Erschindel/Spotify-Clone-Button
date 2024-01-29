import base64
import requests
import datetime
import os
import string
import random
from urllib.parse import urlencode

CLIENT_ID = os.environ["SPOTIPY_CLIENT_ID"]
CLIENT_SECRET = os.environ["SPOTIPY_CLIENT_SECRET"]
REDIRECT_URI = os.environ["SPOTIPY_REDIRECT_URI"]

def get_token():
    client_creds = f"{CLIENT_ID}:{CLIENT_SECRET}"
    client_creds_64 = base64.b64encode(client_creds.encode())

    token_url = 'https://accounts.spotify.com/api/token'
    token_data = {
        "grant_type" : "client_credentials"
    }
    token_headers = {
        "Authorization" : f"Basic {client_creds_64.decode()}"
    }

    r = requests.post(token_url, data = token_data, headers = token_headers)

    if r.status_code in range(200, 299) :
        token_response_data = r.json()
        now = datetime.datetime.now()
        access_token = token_response_data["access_token"]
        expires_in = token_response_data["expires_in"]
        remaining_token_time = now + datetime.timedelta(seconds = expires_in)
        did_expire = remaining_token_time < now
        print(f"time remaining: {expires_in}")
        return access_token

        # print("token: %s" % access_token)
        # print("expired") if did_expire else print(f"expires in: {expires_in}")
    else :
        print("invalid request")

def authorize(scope = "") :
    base_URL = 'https://accounts.spotify.com/authorize?'
    state = ''.join(random.choices(string.ascii_letters, k=10))

    query_string = {
        "response_type": "code",
        "client_id": CLIENT_ID,
        "scope": scope,
        "redirect_uri": REDIRECT_URI,
        "state": state
    }

    try:
        res = requests.get(base_URL, params=query_string, allow_redirects=True)
        res = res.json()
        print(f"code: {res.status_code}")
    except:
        print("failed to authorize")

    return res