#using super()

class Parent(): # superclass
    def display(self, pay):
        self.price = pay
        
        if self.price >= 20000:            
            self.price *= 0.9
        else:
            self.price
        print(' = {:,}'.format(self.price))        
        
class Child(Parent): # subclass
    def display(self, pay): # override display method        
        self.price = pay
        super().display(pay)
        
        if self.price >= 20000:            
            self.price *= 0.8
        else:
            self.price        
        print('8折 {:,}'.format(self.price))
        
c1 = Parent() # superclass object
print('30000 * 9折', end = '')
c1.display(30000)

c2 = Child() # subclass object
print('25000 * 9折', end = '')
c2.display(25000)


