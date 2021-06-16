def test(*args):
    #base method
    i = 0
    for x in args:
        i+=1
        print(f'The array posion {i} is {x} type is {type(x)}')
    print(f'The quantity of this array is {i}')
    #use method in python
    print(f'The quantity of this array is {len(args)}')

test(1, 2, 3.4, 'helu')
