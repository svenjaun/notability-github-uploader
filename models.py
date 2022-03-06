class Folder:
    def __init__(self, name, id, subfolders):
        self.name = name
        self.id = id
        self.subfolders = subfolders
        self.files = []
    def addFile(self, file):
        self.files.append(file)
    def addFiles(self, files):
        for file in files:
            self.addFile(file)
    def print(self):
        printFolder(self)
    


class File:
    def __init__(self, id, name, modifiedTime, lastSyncDate):
        self.name = name
        self.id = id
        self.modifiedTime = modifiedTime
        self.lastSyncDate = lastSyncDate


def printFolder(folder, c = 0):
    print(c*"-" + "Foldername: " + folder.name)
    for file in folder.files:
        print(c*" " + "Fileinformation: ")
        print((c+1)*" " + file.id)
        print((c+1)*" " + file.name)
        print((c+1)*" " + "- Modify: " + file.modifiedTime)
        print((c+1)*" " + "- Sync: " + file.lastSyncDate)
    print()
    for subfolder in folder.subfolders:
        printFolder(subfolder, c+1)


