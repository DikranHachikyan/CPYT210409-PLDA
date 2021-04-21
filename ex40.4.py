def get_squares(n):
    return [ v ** 2 for v in range(n + 1)]

# 1. дефиниция
def generate_squares(n):
    for v in range(n + 1):
        yield v ** 2

if __name__ == '__main__':
    values = get_squares(10)
    print(f'values = {values}')
    
    # 2. присвояване на променлива
    n_sqr = generate_squares(10)

    # 3. взимане на стойностите
    # 
    print(f'1 => {next(n_sqr)}') 
    print(f'2 => {next(n_sqr)}') 
    print(f'3 => {next(n_sqr)}') 
    print(f'4 => {next(n_sqr)}') 
    print(f'5 => {next(n_sqr)}')

    arr = list(n_sqr)
    print(f'arr = {arr}') 

    # print(f'5 => {next(n_sqr)}')
    sqr_5 = generate_squares(5)
    for i in sqr_5:
        print(f'i = {i}')
    print('--- ---')    