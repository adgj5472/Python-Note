# modules
import os

files = (os.getcwd(), "osmod3.py")

for f in files:
    print("item = " + str(f))
    if os.path.exists(f):
        print("exist!")
    if os.path.isdir(f):
        print("directory!")
    if os.path.isfile(f):
        print("file!")
