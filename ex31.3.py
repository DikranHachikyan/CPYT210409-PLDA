# глобална променлива
port = 1521
# 1. дефиниция на функцията
def sum_numbers(a, b, *args):
    # c - локална променлива
    print(f'args = {args}')
    c = a + b
    for v in args:
        c += v

    return c
    

if __name__ == '__main__':
    # 2. извикване
    res = sum_numbers(5, 6)
    print(f'sum = {res}')

    x, y, z = 10, 22, 15
    res = sum_numbers(x, y, z)
    print(f'{x} + {y} + {z} = {res}')

    res = sum_numbers(x, y, 5, 6, 7, 8, 9)
    print(f'{x} + {y} + ... = {res}')

    arr = [ v for v in range(3, 15)]
    res = sum_numbers(x, y, *arr)
    print(f'{x} + {y} + ' + ' + '.join(map(str, arr)) + f' = {res}' )
    print('--- ---')    