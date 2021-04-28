
# from draw.point import Point

# с __init__.py
from draw import Point

if __name__ == '__main__':
    # 2. декларация на променлива от типа
    # клас - Point, обект - p, p1
    p1 = Point(16, 8)
    p2 = Point(6, 18)


    print(f'Point:{p2}')
    print(f'count: {Point.count}')
    p1.draw()
    del p1
    print('--- ---')    