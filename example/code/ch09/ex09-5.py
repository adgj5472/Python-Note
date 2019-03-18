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
        
    def getname(self):
        return self.__name   

    def display_vehicle(self):
        print("vendor = " + self.__name)
        print("color = " + self.__color)

# define Car subclass
class Car(Vehicle):
    # constructor
    def __init__(self, name, color, model):
        # call superclass constructor
        super().__init__(name, color)
        self.__model = model
    # method
    def display_vehicle(self):
        print("name = " + self.getname())
        print("model = " + self.__model)
        print("color = " + self.getcolor())
        
# create object
c1 = Car("Ford", "Black", "GT350")

# call method
c1.display_vehicle()


