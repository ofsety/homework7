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
    

student1 = Student("Ivan",14,8,8)
student2 = Student("Maxim",16,10,6)

def main():
    print(student1,student2)
    renew_points_student1=input(f"Input new points for student 1 ({student1.name}) or press enter if you dont want to:")
    renew_points_student2=input(f"Input new points for student 2 ({student2.name}) or press enter if you dont want to:")
    if renew_points_student1:
        student1.medium_point=renew_points_student1
        print(student1,student2)
    if renew_points_student2:
        student2.medium_point=renew_points_student2
        print(student1,student2)
    else:
        print(student1,student2) 


main()