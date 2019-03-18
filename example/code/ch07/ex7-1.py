# file
fp = open("note.txt", "w")
if fp != None:
    print("File open successfully!")
fp.close()

fp = open("temp/note.txt", "w")
if fp != None:
    print("File open successfully!")
fp.close()