# file read
fp = open("note.txt", "r")
print("Content(with new line):")

for line in fp:
    print(line)
fp.close() 

fp = open("note.txt", "r")   
print("Content(no new line):")

for line in fp:
    print(line, end="")    
fp.close()    