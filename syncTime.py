import json
from config import SYNC_DATA_PATH, DEFAULT_TIMESTAMP, STANDARD_SYNC_DATA
def readData():
    try:
        with open(SYNC_DATA_PATH) as json_file:
            jsonData = json.load(json_file)
        return jsonData
    except:
        with open(SYNC_DATA_PATH, "w") as json_file:
            json_file.write(STANDARD_SYNC_DATA)
        return STANDARD_SYNC_DATA

def saveData(obj):
    with open(SYNC_DATA_PATH, "w") as json_file:
        json_file.write(json.dumps(obj))


def getLastSyncDate(fileId):
    data = readData()
    for file in data["files"]:
        if file["id"] == fileId:
            return file["lastSyncDate"]

    data['files'].append({"id": fileId, "lastSyncDate": DEFAULT_TIMESTAMP})
    saveData(data)
    return DEFAULT_TIMESTAMP


def updateLastSyncDate(fileId, lastSyncDate):
    data = readData()

    for file in data["files"]:
        if file["id"] == fileId:
            file["lastSyncDate"] = lastSyncDate
    saveData(data)