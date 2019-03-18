# function
# function with default value
def volume(length, width = 2, height = 3):
    return length * width * height

l, w, h = 10, 5, 15            
print("volume: " + str(volume(l, w, h))) 
print("volume: " + str(volume(l, w))) 
print("volume: " + str(volume(l)))



