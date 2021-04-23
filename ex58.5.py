
# 1. дефиниция на клас

class Point:
    # Конструктор на класа
    def __init__(self, x = 0, y = 0, *args, **kwargs):
        print('Point Ctor')
        # данни класа
        self.__x = x
        self.__y = y

    # Методи на класа
    def draw(self):
        print(f'draw point at: ({self.__x},{self.__y})')

    def move_to(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x
    
if __name__ == '__main__':
    # 2. декларация на променлива от типа
    # клас - Point, обект - p, p1
    p1 = Point()
    p2 = Point(6, 8)

    
    p2.draw()
    p2.set_x(10)
    p2.draw()
    
    print('--- ---')    