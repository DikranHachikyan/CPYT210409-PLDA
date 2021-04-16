def show(title, a = 100, *args,kw1 = 'A',kw2='B', **kwargs):
    print(f'positional arg title = {title}')

    print(f'default arg a = {a}')
    print('args')
    for v in args:
        print(f'arg:{v}', end = ' ')
    print()

    print(f'keyword args')
    params = {
        'log': kwargs.get('log','app.log'),
        'path': kwargs.get('path','./')
    }
    print(f'params:{params}')

    print('keyword-only params')
    print(f'kw1 = {kw1}, kw2 = {kw2}')

    print(' - ' * 20)
if __name__ == '__main__':
    show('Text Editor')

    show('Calculator', 1)

    show('Calculator', 1, 10,20,30,40 )

    show('Calculator', 1, 10,20,30,40, path = '/usr/local' )

    config = {
        'app_title': 'Text Editor',
        'version': '1.2.4',
        'temp' : '/tmp',
        'max_file': 1000,
        'path':'/usr',
        'log': 'calculator.log'
    }
    show('Calculator', 1, 10,20,30,40, **config)

    show('Calculator', 1, 10,20,30,40, kw1 = 'X',**config)

    print('--- ---')    