
# 1. дефиниция на клас

class Point:
    # Конструктор на класа
    def __init__(self, x = 0, y = 0, *args, **kwargs):
        print('Point Ctor')
        # данни класа
        self.x = x
        self.y = y

    # Методи на класа
    def draw(self):
        print(f'draw point at: ({self.x},{self.y})')

    def move_to(self, dx, dy):
        self.x += dx
        self.y += dy

    @property
    def x(self):
        return self.__x # тук трябва да е __x !!!

    @x.setter
    def x(self, x):
        assert x >= 0, 'x must be positive'
        self.__x = x
    
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        assert y >= 0, 'y must be positive'
        self.__y = y

if __name__ == '__main__':
    # 2. декларация на променлива от типа
    # клас - Point, обект - p, p1
    p1 = Point()
    p2 = Point(6, 8)

    
    p2.draw()
    print(f'dot access: ({p2.x},{p2.y})')
    p2.x = 10
    p2.y = 10
    p2.draw()
    
    print('--- ---')    