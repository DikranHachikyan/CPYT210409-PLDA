# глобална променлива
c = 1521

# 1. дефиниция на функцията
def show():
    global c
    c = 20
    print(f'c = {c}')
    

if __name__ == '__main__':
    # 2. извикване
    print(f'before show c = {c}')
    show()    
    print(f'after show c = {c}')

    print('--- ---')    