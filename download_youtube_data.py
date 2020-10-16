# Sample Python code for youtube.videos.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import sys 
import os
import pprint

import json
import os.path
import google.oauth2.credentials
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

CLIENT_SECRETS_FILE = "YOUR_CLIENT_SECRET_JSON_FILE"
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

def get_authenticated_service():

  if os.path.isfile("credentials.json"):
    with open("credentials.json", 'r') as f:
      creds_data = json.load(f)
    creds = Credentials(creds_data['token'])

  else:
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    creds = flow.run_console()
    creds_data = {
          'token': creds.token,
          'refresh_token': creds.refresh_token,
          'token_uri': creds.token_uri,
          'client_id': creds.client_id,
          'client_secret': creds.client_secret,
          'scopes': creds.scopes
      }
    # print(creds_data)
    with open("credentials.json", 'w') as outfile:
      json.dump(creds_data, outfile)
  return build(API_SERVICE_NAME, API_VERSION, credentials = creds)

def videoinfo(youtube, my_part,myid):
    
    
    request = youtube.videos().list(
      part=my_part,
      id=myid
    )
    response = request.execute()

    pprint.pprint(response)

if __name__ == "__main__":
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    youtube = get_authenticated_service()
    
    part = "snippet"
    id=sys.argv[1]
    
    videoinfo(youtube, part, id)


