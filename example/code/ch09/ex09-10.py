#inheritance

class Father: # superclass 1
    def walking(self):
        print('It is good to walk!')
        
class Mother: # superclass 2
    def riding(self):
        print('I can ride a bike!')
        
class Son(Father, Mother): # subclass
    pass

#create object
bob = Son()
bob.walking()
bob.riding()
