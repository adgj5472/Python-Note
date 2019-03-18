# file read
fp = open("note.txt", "r")
str1 = fp.read()
print("Content:")
print(str1)
fp.close()

fp = open("note.txt", "r")
list1 = fp.readlines()
print("Content:")
print(list1)
for line in list1:
    print(line, end="")    
fp.close()
