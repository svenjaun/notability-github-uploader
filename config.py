MAIN_FOLDER_NAME = 'Notability'
INTERVAL = 60
SYNC_DATA_PATH = "syncTime.json"
DEFAULT_TIMESTAMP = '2000-00-00T13:00:00.000Z'
STANDARD_SYNC_DATA = """
{
    "files": []
}
"""
# If modifying these scopes, delete the file token.json.
SCOPES = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.metadata'
]
TOKEN_PATH ='authorization/token.json'
CREDENTIALS_PATH = 'authorization/credentials.json'