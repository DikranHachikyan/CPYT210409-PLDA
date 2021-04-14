
def foo():
    print('hello python')

if __name__ == '__main__':
    num = float(input('Enter a number:'))
    res = ''

    if num > 0:
        res = 'positive number'
    else:
        res = 'negative number or 0'

    foo()
    print(f'{num} is a {res}')
    print('--- ---')