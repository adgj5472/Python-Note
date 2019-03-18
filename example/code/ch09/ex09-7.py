# class
# define Circle class
class Circle:
    # constructor
    def __init__(self, radius):
        self.__radius = radius
    # method
    def setradius(self, radius):
        self.__radius = radius
        
    def getradius(self):
        return self.__radius
    
    def area(self):
        return 3.1415926 * self.__radius ** 2
    
    def __add__(self, circle2):
        return Circle(self.__radius + circle2.__radius)
        
    def __gt__(self, circle2):
        return self.__radius > circle2.__radius      
        
    def __lt__(self, circle2):
        return self.__radius < circle2.__radius   
    
    def __str__(self):
        return "圓半徑 = " + str(self.__radius)  

# create object
c1 = Circle(10)
c2 = Circle(15)

r = c1.getradius()
print("c1 radius = " + str(r))
r = c2.getradius()
print("c2 radius = " + str(r))
c3 = c1 + c2
r = c3.getradius()
print("c3=c1+c2 radius = " + str(r))

b = c3 > c2
print("c3 > c2 = " + str(b))

b = c1 < c2
print("c1 < c2 = " + str(b))

print(str(c3))

print (c3._Circle__radius)  # Ok
print (c3.__radius)  # Error
