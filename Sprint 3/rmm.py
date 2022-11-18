# Import time, possibly date - Daniel and Yash
from datetime import time
import os
import sys


# Initialize time
now = time.now()


# prints datetime - Daniel and Damien
print(datetime.datetime.now())


# Check file path with os.walk, check to see if file exists - Chris and Syed
def run():
    print ('run')
    for dirName, subdirList, fileList in os.walk("C:/Program_Files/Google/Chrome/Application/"):
        for fname in fileList:
            if fname.find("chrome.exe")<0: continue
            update_file(https://www.google.com/chrome/)

# Check program version
# If currentInstalledVersion is < VersionFromWeb Update
# If CurrentInstalledVersion is = VersionFromWeb do not update

# If time is not 3 am do not update - Damien
            else:
                DontUpate_file(time != 03:00)


# For program to run - Yash
if __name__ == '__main__':
    run()

