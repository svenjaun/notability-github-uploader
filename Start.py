import driveHelper
import time


def main():
    while True:
        driveHelper.setup()
        folders = driveHelper.loadFolder()
        driveHelper.addFiles(folders)
        driveHelper.checkAndRunFileUpdates(folders)
        time.sleep(60)


if __name__ == '__main__':
    main()
    