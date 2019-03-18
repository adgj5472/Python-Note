# mybmi.py
name = None

def bmi(h, w):
    r = w/h/h
    return r
    
if __name__ == '__main__':
    print('BMI with 160cm height and 50kg weight :',
          bmi(1.60,50))
