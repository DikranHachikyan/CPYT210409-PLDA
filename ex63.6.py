import re

if __name__ == '__main__':
    names = None

    # pattern = re.compile('^\w+\s+\w+$')
    # pattern = re.compile('^[A-Z][a-z]+\s+[A-Z][a-z]+$')
    pattern = re.compile('^[a-z]+\s+[a-z]+$', re.I)

    while not names:
        names = input('your names (firstname lastname):')
        m = pattern.match(names)
        if not m:
            names = None
            continue
        print(f'names start:{m.start()} end:{m.end()} span:{m.span()}')    

    print('--- ---')