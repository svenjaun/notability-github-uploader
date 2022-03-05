from operator import le
import drive_helper
import json

def main():
    drive_helper.setup()
    drive_helper.updatePropsTest()
    return
    custom = drive_helper.getAllFiles()
    for item in custom:
        for key in item:
            if key == 'parents':
                print(item[key])
        # print(item)
        # print("\n")



if __name__ == '__main__':
    main()