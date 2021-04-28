import re

if __name__ == '__main__':
    txt = 'Lorem, ipsum dolor sit amet, consectetur, adipisicing elit, sed' 

    pattern = re.compile(r'[,]')
    result = re.split(pattern, txt)

    print(result)
    print('--- ---')