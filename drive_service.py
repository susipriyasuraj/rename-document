"""
Google Drive API service initialisation.
Supports both Service Account (recommended for automation)
and OAuth2 desktop-app credentials.
"""

import os
import pickle

from google.auth.transport.requests import Request
from google.oauth2 import service_account
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

import config

# Scopes required: full Drive access so we can copy, rename and optionally trash files.
SCOPES = ["https://www.googleapis.com/auth/drive"]


def _is_service_account(cred_path: str) -> bool:
    """Return True when the JSON file is a service-account key."""
    import json
    with open(cred_path) as f:
        data = json.load(f)
    return data.get("type") == "service_account"


def get_drive_service():
    """Build and return an authenticated Drive v3 service object."""
    cred_path = config.CREDENTIALS_FILE

    if not os.path.exists(cred_path):
        raise FileNotFoundError(
            f"Credentials file not found: '{cred_path}'\n"
            "Download it from Google Cloud Console → APIs & Services → Credentials."
        )

    if _is_service_account(cred_path):
        creds = service_account.Credentials.from_service_account_file(
            cred_path, scopes=SCOPES
        )
    else:
        # OAuth2 desktop-app flow
        creds = None
        if os.path.exists(config.TOKEN_FILE):
            creds = Credentials.from_authorized_user_file(config.TOKEN_FILE, SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(cred_path, SCOPES)
                creds = flow.run_local_server(port=0)
            with open(config.TOKEN_FILE, "w") as token:
                token.write(creds.to_json())

    return build("drive", "v3", credentials=creds)
