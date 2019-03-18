# Function definition is here
def changeme( mylist ):
    mylist = [1,2,3,4]
    #This would assign new reference in mylist
    print ("Values in the function: ", mylist)
    return

# Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)