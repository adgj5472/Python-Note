# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator contains yield statements
    yield n
    n += 1
    print('This is printed second')
    yield n
    n += 1
    print('This is printed at last')
    yield n

for item in my_gen():
    print(item)
