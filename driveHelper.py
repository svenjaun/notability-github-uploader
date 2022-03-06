from __future__ import print_function

import os.path
import io
import apiRequests
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
from authentication import createCredentials
from models import Folder, File
from syncTime import updateLastSyncDate, getLastSyncDate


service = None
folderId = ''

def downloadFileById(file, filePath, ):
    bytesIO = downloadFileBytes(file.id)
    saveFile(bytesIO, filePath, file.name)
    updateLastSyncDate(file.id, file.modifiedTime)

def saveFile(bytesIO, filePath, fileName):
    os.makedirs("downloads/" + filePath, exist_ok=True)
    with open("downloads/" + filePath + "/" + fileName, "wb") as f:
        f.write(bytesIO.getbuffer())
        
def checkAndRunFileUpdates(folder, path = ''):
    global service
    for file in folder.files:
        if file.modifiedTime > file.lastSyncDate:
            downloadFileById(file, path)
    for subfolder in folder.subfolders:
        checkAndRunFileUpdates(subfolder, path + subfolder.name + '/')

def downloadFileBytes(id):
    global service
    request = apiRequests.getFileMedia(id)
    bytesIO = io.BytesIO()
    downloader = MediaIoBaseDownload(bytesIO, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
    return bytesIO

def addFiles(folders):
    global folderId
    loopThroughFolder(folders)

def loopThroughFolder(folder):
    files = updateFilesInFolder(folder.id)
    folder.addFiles(files)
    for subfolder in folder.subfolders:
        loopThroughFolder(subfolder)

def updateFilesInFolder(id):
    global service
    results = apiRequests.getFilesByParentId(id)
    items = results.get('files', [])
    files = []
    for item in items:
        files.append(File(item['id'], item['name'], item['modifiedTime'], getLastSyncDate(item['id'])))
    return files


def getSubFolderIds(parentId, parentName):
    subFolderResults = apiRequests.getFoldersByParentId(parentId)
    items = subFolderResults.get('files', [])
    folders = []
    for item in items:
        folders.append(getSubFolderIds(item['id'], item['name']))
    return Folder(parentName, parentId, folders)
        


def setup():
    global service
    try:
        service = build('drive', 'v3', credentials=createCredentials())
        apiRequests.setService(service)
    except HttpError as error:
        print(f'Unable to autenticate: {error}')

def loadFolder():
    global folderId
    results = apiRequests.getMainFolder()
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
    folders = getSubFolderIds(folderId, items[0]['name'])
    addFiles(folders)
    return folders
