# With the "with" statement, you get better syntax and exceptions handling. 
# The with statement simplifies exception handling by encapsulating common
# preparation and cleanup tasks.

try:
    fp = open("note.txt", "r")
    str1 = fp.read()
    print("Content:")
    print(str1) 
except:
    print("Error: File I/O error!")
finally:
    fp.close()

	
with open("note.txt", "r") as fp:
    str1 = fp.read()
    print("Content:")
    print(str1)    