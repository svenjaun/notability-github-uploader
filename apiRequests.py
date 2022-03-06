from googleapiclient.errors import HttpError
from config import MAIN_FOLDER_NAME

service = None

def setService(newService):
    global service
    service = newService
    
def getFoldersByParentId(parentId):
        try:
            return service.files().list(
                    q="mimeType='application/vnd.google-apps.folder' and parents = '{0}'".format(parentId),
                    fields="nextPageToken, files(id, name)"
                ).execute()
        except HttpError as error:
            print(f'getFoldersByParentId({parentId}): Error with google drive API: {error}')


def getFilesByParentId(id):
        try:
            return service.files().list(
                    q="mimeType != 'application/vnd.google-apps.folder' and '{0}' in parents".format(id), 
                    fields="nextPageToken, files(id, name, modifiedTime)"
                ).execute()
        except HttpError as error:
            print(f'getFilesByParentId({id}): Error with google drive API: {error}')

def getMainFolder():
        try:
            return service.files().list(
                    q="mimeType='application/vnd.google-apps.folder' and name = '{0}'".format(MAIN_FOLDER_NAME),
                    fields="nextPageToken, files(id, name)"
                ).execute()
        except HttpError as error:
            print(f'getMainFolder(): Error with google drive API: {error}')

def getFileMedia(id):
    return service.files().get_media(fileId=id)