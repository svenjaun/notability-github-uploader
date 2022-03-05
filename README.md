# Notability Github Uploader

## Setup Google Drive

- Backup Notability in Google Drive
- Create Project: https://console.cloud.google.com/projectcreate
- API Key erstellen: https://developers.google.com/workspace/guides/create-credentials#create_credentials_for_a_service_account
  - => Desktop Application
  - #create_credentials_for_a_service_account

- Active Google Drive API. Change url!!! 
  - https://console.cloud.google.com/apis/library/drive.googleapis.com?project=<your-project-id!!!>

## Pip install 
`pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`

# Google Drive API docs
[API Documentation]("https://developers.google.com/drive/api?hl=de")