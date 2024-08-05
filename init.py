class Employee:
    def __init__(self,name,doj,designation,salary):
        self.name=name
        self.doj=doj
        self.designation=designation
        self.salary=salary
    def print_details(self):
        print("Name:",self.name)
        print("Date of Join:",self.doj)
        print("Designation:",self.designation)      
        print("Salary:",self.salary)
        print("---------------------")
emp1=Employee("Riya Patel","2020-01-01","Manager",50000)
emp1.print_details()