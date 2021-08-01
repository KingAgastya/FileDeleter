import time
import os
import shutil

path = input("Enter the Path")
days = input('How many days old files do you want to delete')
seconds = time.time() - (days*24*60*60)
doesPathExist = os.path.exists(path)

if doesPathExist(path):
    os.walk(path)
else:
    print("OI Y U GIVING RONG PATH")
path = os.path.join()

nowTime = os.stat(path).st_ctime

if(seconds < nowTime):
    os.os.remove(path)
    shutil.rmtree()
