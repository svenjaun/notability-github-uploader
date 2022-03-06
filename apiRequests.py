from config import MAIN_FOLDER_NAME

service = None

def setService(newService):
    global service
    service = newService
    
def getFoldersByParentId(parentId):
    return service.files().list(
            q="mimeType='application/vnd.google-apps.folder' and parents = '{0}'".format(parentId),
            fields="nextPageToken, files(id, name)"
        ).execute()


def getFilesByParentId(id):
    return service.files().list(
            q="mimeType != 'application/vnd.google-apps.folder' and '{0}' in parents".format(id), 
            fields="nextPageToken, files(id, name, modifiedTime)"
        ).execute()

def getMainFolder():
    return service.files().list(
            q="mimeType='application/vnd.google-apps.folder' and name = '{0}'".format(MAIN_FOLDER_NAME),
            fields="nextPageToken, files(id, name)"
        ).execute()

def getFileMedia(id):
    return service.files().get_media(fileId=id)