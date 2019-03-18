# module
import random
#import random as R

print(dir(random))

target = random.randint(1, 100) # generate random number
guess = 1
while True:
    guess = int(input("Guess the number(1~100) =>"))
    if target == guess:
        break      # exit loop
    
    if guess > target:
        print("Too big!")
    else:
        print("Too small!")
print("Bingo:", target)


