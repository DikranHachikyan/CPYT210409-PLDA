
if __name__ == '__main__':
    config = {
        'title': 'Text Editor',
        'version': '1.2.4',
        'temp' : '/tmp',
        'max_file': 1000
    }

    for item in config.items():
        key, value = item
        print(f'{key} => {value}')
        
 
    print('--- ---')    