import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Rectangle:
    def __init__(self):
        # Случайные координаты для двух углов
        self.x1 = random.randint(0, 9)
        self.y1 = random.randint(0, 9)
        self.x2 = random.randint(0, 9)
        self.y2 = random.randint(0, 9)

        # Нормализация (чтобы x1, y1 – нижний левый, x2, y2 – верхний правый)
        self.low_x = min(self.x1, self.x2)
        self.high_x = max(self.x1, self.x2)
        self.low_y = min(self.y1, self.y2)
        self.high_y = max(self.y1, self.y2)

    def contains(self, point):
        # Проверка, точка ли внутри прямоугольника
        return (self.low_x <= point.x <= self.high_x) and (self.low_y <= point.y <= self.high_y)

    def draw(self, point=None):
        # Рисует поле 10x10
        for y in range(9, -1, -1):  # від 9 до 0
            for x in range(10):
                # Если точка пользователя совпадает с текущими координатами
                if point and point.x == x and point.y == y:
                    print('X', end=' ')
                # Если это угол прямоугольника
                elif [x, y] in [[self.x1, self.y1], [self.x2, self.y2]]:
                    print('+', end=' ')
                # Если точка внутри прямоугольника
                elif self.low_x <= x <= self.high_x and self.low_y <= y <= self.high_y:
                    print('*', end=' ')
                # Пустое место
                else:
                    print('-', end=' ')
            print()


# Основная часть программы
rect = Rectangle()
print("Прямокутник створено зі випадковими координатами!")
print("(Ти цього не бачиш, поки не зробиш хід)")

# Запрос координат пользователя
x = int(input("Введи X (0-9): "))
y = int(input("Введи Y (0-9): "))

point = Point(x, y)
rect.draw(point)

if rect.contains(point):
    print("Попал в прямоугольник!")
else:
    print("Промазал!")