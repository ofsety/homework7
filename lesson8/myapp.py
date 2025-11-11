from random import randint
# global win_counter_global
# global fall_counter_global
win_counter_global=0
fall_counter_global=0


class Point():
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    
    def __str__ (self):
        return f"({self.x},{self.y})"
    
    def falls_in_rectangle(self, point1_coordinate, point2_coordinate):
        self.point1_coordinate  = point1_coordinate
        self.point2_coordinate  = point2_coordinate
        if self.point1_coordinate.x <= self.x <= self.point2_coordinate.x and self.point1_coordinate.y <= self.x <= self.point2_coordinate.y:
            global win_counter_global
            win_counter_global +=1
            print("The point falls in rectangle")
            print(f"Your win counter is {win_counter_global}")
            print (point1_coordinate,point2_coordinate)
            
            

        elif self.point1_coordinate.x >= self.x >= self.point2_coordinate.x and self.point1_coordinate.y >= self.y >= self.point2_coordinate:
            win_counter_global +=1
            print("The point falls in rectangle")
            print(f"Your win counter is {win_counter_global}")
            print (point1_coordinate,point2_coordinate)
             
         
        else:
            global fall_counter_global
            fall_counter_global +=1
            print("The point doesnt fall in rectangle")
            print(f"Your fall counter is {fall_counter_global}")
            print (point1_coordinate,point2_coordinate)
            

termination = "No"


while termination != "Yes":
    point1= Point(randint(-4,4), randint(-4,4))
    point2= Point(randint(-4,4), randint(-4,4))
    x= int(input ("x="))
    y= int(input("y="))
    user_point = Point (x,y)
    user_point.falls_in_rectangle(point1, point2) 
    termination = input("Do you want to end? Please use 'Yes' or 'No'")

if termination == "Yes":
    win_counter_global=0
    fall_counter_global=0