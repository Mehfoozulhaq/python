class Student:
    def __init__(self,name,school):
        self.name=name
        self.school=school
        self.marks=[]
    def average(self):
        return f"Average Marks:{sum(self.marks)/len(self.marks)}"
    
Rolf= Student("Rolf","MIT")
Rolf.marks.append(87)
Rolf.marks.append(77)
Rolf.marks.append(85)
Rolf.marks.append(96)
print(Rolf.name,Rolf.school,Rolf.average())

class Workingstudent(Student):
     def __init__(self, name, school,salary):
         super().__init__(name, school)
         self.salary=salary
     def monthlysalary(self):
         return f"Monthly Salary :{self.salary*30}"

Harsh = Workingstudent('Harsh','IUST',30.5)
print(Harsh.name,Harsh.school,Harsh.salary,Harsh.monthlysalary())