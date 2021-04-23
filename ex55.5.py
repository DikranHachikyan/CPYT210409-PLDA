
# 1. дефиниция на клас

class Point:
    # Конструктор на класа
    def __init__(self):
        print('Point Ctor')
        # данни класа
        self.x = 20
        self.y = 30

    # Методи на класа
    def draw(self):
        print(f'draw point at: ({self.x},{self.y})')
    
if __name__ == '__main__':
    # 2. декларация на променлива от типа
    # клас - Point, обект - p, p1
    p = Point()
    p1 = Point()

    p1.x = 2
    p1.y = 4


    print(f'Point:({p.x}, {p.y})')
    print(f'Point 1:({p1.x}, {p1.y})')

    p.draw()
    p1.draw()
    
    print('--- ---')    