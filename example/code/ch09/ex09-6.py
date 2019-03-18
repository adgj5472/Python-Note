# class
# Vehicle class
class Vehicle:
    pass

# Car class
class Car():
    pass
        
# create object
c1 = Car()
v1 = Vehicle()

# check object's class 
print("isinstance(1,int) =", isinstance(1, int))
print("isinstance(1.5,int) =", isinstance(1.5, int))
print("isinstance([1,2,3,4],list) =", isinstance([1, 2, 3, 4], list))
print("isinstance(c1,Car) =", isinstance(c1, Car))
print("isinstance(v1,Vehicle) =", isinstance(v1, Vehicle))
