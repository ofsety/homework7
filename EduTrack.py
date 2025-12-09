class Student():
    def __init__(self, name, age, clas, medium_point):
        self.name= name 
        self.age= age
        self.clas=clas
        self.medium_point=medium_point
    
    def __str__ (self):
        return (f"""
                Name:{self.name} 
                Age:{self.age}
                Clas:{self.clas} 
                Medium Point:{self.medium_point}

                """)
    
# Я тут робив інтерактив але ви сказали що не треба

# Termination= "Yes"

# while termination != "No":
#     Student_Name= input("Please input students name:")
#     termination= input("Dp you want to see others students information? Please use 'Yes' or 'No'")
#     input("Please input students name:")= Student()

student1 = Student("Ivan",14,8,8)
student2 = Student("Maxim",16,10,6)

def main():
    renew_points=input("Input new points or press enter if you dont:")
    if renew_points:
        student1.medium_point=renew_points
        student2.medium_point=renew_points
        print(student1,student2)
    else:
       print(student1,student2) 


main()