list = [1,2,3,4,5]
try:
    print(list[6])
except IndexError:
    print('This index is out of list')