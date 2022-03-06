# Notability Github Uploader

# Setup
## Setup Google Drive

- Backup Notability in Google Drive
- Create Project: https://console.cloud.google.com/projectcreate
- Create API Key: Change url!!! 
  - https://console.cloud.google.com/apis/library/drive.googleapis.com?project=<your-project-id!!!>
  - => Desktop Application
    - Maybe you have to configure OAuth with some data

- Activate Google Drive API. Change url!!! 
  - https://console.cloud.google.com/apis/library/drive.googleapis.com?project=<your-project-id!!!>

Download your Client-ID Credentials as .JSON
Save JSON as `authorization/credentials.json` 

## Setup script

Change the `config.py` to your needs

## Pip install 
`pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`

# Start script
`python3 Start.py`

# Google Drive API docs
[API Documentation]("https://developers.google.com/drive/api?hl=de")
[PIP Library Docs](https://googleapis.github.io/google-api-python-client/docs/dyn/drive_v3.html)