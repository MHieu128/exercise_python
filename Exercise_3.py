def test(**kwargs):
    i = 0
    for k, v in kwargs.items():
        i+=1
        print(f'The array posion {i} is {k}:{v}')
    print(f'The quantity of this array is {len(kwargs)}')

test(a = 1, b = 2, c = 3.4, d = 'helu')