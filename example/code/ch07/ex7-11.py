# file
try:
    with open('data.txt', 'xt') as fp:
        fp.write('File write test')
except FileExistsError:
    print('File already exist, cannot overwrite')
