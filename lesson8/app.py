from random import randint

print(randint(3,5))

class Point():

    def __init__(self, x, y):

        self.x = x

        self.y = y

    def __str__(self):

        return f"({self.x}, {self.y})"

point_1 = Point(3, 9)

print(point_1.x)

print(point_1.y)

print(type(point_1))

 

point_2 = Point(4, 8)

print("point", point_2)
        


