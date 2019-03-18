# A simple generator function
def my_gen():
    for i in range(3):
        n = i+1
        print('This is printed', n, 'time(s)')
        # Generator contains yield statements
        yield n
    
for item in my_gen():
    print(item)
