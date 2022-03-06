import driveHelper
import time
from config import INTERVAL

def main():
    while True:
        driveHelper.setup()
        folders = driveHelper.loadFolder()
        driveHelper.addFiles(folders)
        driveHelper.checkAndRunFileUpdates(folders)
        time.sleep(INTERVAL)


if __name__ == '__main__':
    main()
    