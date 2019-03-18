# class
# define Vehicle superclass
class Vehicle:
    # constructor
    def __init__(self, name, color):
        self.__name = name
        self.__color = color
    # method
    def getcolor(self):
        return self.__color

    def setcolor(self, color):
        self.__color = color
        
    def getname(self):
        return self.__name

# define Car subclass
class Car(Vehicle):
    # constructor
    def __init__(self, name, color, model):
        # call superclass constructor
        super().__init__(name, color)
        self.__model = model
    # method
    def display_car(self):
        print("name = " + self.getname())
        print("model = " + self.__model)
        print("color = " + self.getcolor())

# create object
c1 = Car("Ford", "Black", "GT350")

# call method
c1.display_car()
print("車輛廠牌 = " + c1.getname())
