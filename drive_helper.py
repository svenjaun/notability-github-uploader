from __future__ import print_function

import os.path
import time
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

service = None
folderId = ''


FOLDER_NAME = 'Notability'

def updatePropsTest():
    file_id='128ml4RAJI-B-eef4fzgojOGdsTgj_sOK'
    testData = {
        "val1": "Value 1",
        "val2": "Value 2",
        "val3": "Value 3"
    }
    return service.properties().update(
        fileId=file_id, propertyKey='appProperties', body=testData).execute()


def getAllFiles():
    global service
    if not isReady():
        return None
    # Call the Drive v3 API
    print("{0}".format("mimeType != 'application/vnd.google-apps.folder' and '{0}' in parents".format(folderId)))
    results = service.files().list(
        q="mimeType != 'application/vnd.google-apps.folder'", 
        fields="nextPageToken, files(id, name, parents)"
        ).execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
        return
    else:
        return items

def getSubFolderIds(parentId):
    subFolderResults = service.files().list(
        q="mimeType='application/vnd.google-apps.folder' and parents = '{0}'".format(parentId),
        fields="nextPageToken, files"
        ).execute()
    items = subFolderResults.get('files', [])
    ids = []
    for item in items:
        ids.append(item['id'])
        for id in getSubFolderIds(item['id']):
            ids.append(id)
        if item['id'] == '128ml4RAJI-B-eef4fzgojOGdsTgj_sOK':
            print(item)
    return ids
        


def setup():
    global service, folderId
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('authorization/token.json'):
        creds = Credentials.from_authorized_user_file('authorization/token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'authorization/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('authorization/token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('drive', 'v3', credentials=creds)
        # Call the Drive v3 API
        results = service.files().list(
            q="mimeType='application/vnd.google-apps.folder' and name = '{0}'".format(FOLDER_NAME),
            fields="nextPageToken, files"
            ).execute()
        items = results.get('files', [])
        if not items:
            print('No folder found.')
            return
        elif len(items) > 1:
            print('More than one folder found.')
            print('---')
            print(items)
            return

        folderId = items[0]['id']
        print('Folder found: {0}'.format(folderId))
        print('Folder name: {0}'.format(items[0]['name']))
        
        folders = getSubFolderIds(folderId)
        

    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')

def main():
    setup()


def isReady():
    global service, folderId
    if service is None:
        print('Service not initialized.')
        return False
    if folderId == '':
        print('Folder not found.')
        return False
    return True

