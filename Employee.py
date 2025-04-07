class Employee:
    def __init__(self, salary, department, name):
        self.__salary = salary
        self._department = department
        self.name = name

    def get__salary(self):
        return self.__salary

    def set__salary(self, salary):
        if isinstance(salary, int) and salary >= 0:
            self.__salary = salary
        else:
            print("Your argument isn't right!\nSalary doesn't change.")    

    def promote(self, percentage):
        if isinstance(percentage, int) and percentage >= 0:
            self.__salary = self.__salary + (self.__salary * percentage) / 100
            return self.__salary
        else:
            print("Write the right percentage!")

    def transfer_department(self, department):
        if isinstance(department, str):
            self._department = department
        else:
            print("Your argument isn't right!\nDepartment doesn't change.")

    def display_info(self):
        return f"{self.__salary} {self._department} {self.name}"
    
a = Employee(100000, "Finance", "Anush")
m = Employee(100000,"IT", "Margo")
a.salary = 80000
print(a.__dict__)
a.set__salary(120000)
a.promote(10)
print(a.get__salary())
m.transfer_department("HR")
print(a.display_info())
print(m.display_info())
 
class Manager(Employee):
    
    def __init__(self, salary, department, name, team_size):
        super().__init__(salary, department, name)
        self.team_size = team_size

l = Manager(200000, "leader", "Lilit", 2)        
l.promote(10)
print(l.get__salary())
print(l.display_info())
