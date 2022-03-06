import drive_helper
import apiRequests
import time


def main():
    while True:
        drive_helper.setup()
        folders = drive_helper.loadFolder()
        drive_helper.addFiles(folders)
        drive_helper.checkAndRunFileUpdates(folders)
        time.sleep(60)




if __name__ == '__main__':
    main()
    