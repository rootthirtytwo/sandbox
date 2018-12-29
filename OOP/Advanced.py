import datetime

# parent class
class Employee():

    raise_amt = 1.05
    num_of_emp = 0

    # initializing
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.fullname = self.fname.title()+' '+self.lname.title()
        self.email = self.fname+'.'+self.lname+'@company.com'
        self.pay = pay
        Employee.num_of_emp += 1


    # special method : representation
    def __repr__(self):
        return self.fname.title()+' '+self.lname.title()

    # object method
    def raise_pay(self):
        self.pay = ( self.pay * self.raise_amt )

    # class methods
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_strig(cls, txt):
        fname, lname, pay = txt.split('-')
        return cls(fname, lname, pay)

    # static methods
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# child class of Emplyee
class Developer(Employee):

    raise_amt = 1.10

    # initializing
    def __init__(self, fname, lname, pay, prog_lang):
        super().__init__(fname, lname, pay)
        #super(Developer, self).__init__(fname, lname, pay)
        self.prog_lang = prog_lang

# child class of Employee
class Manager(Employee):

    raise_amt = 1.15

    def __init__(self,fname, lname, pay, employees=None):
        super().__init__(fname, lname, pay)
        if employees is None:
            self.emplyees = []
        else:
            self.emplyees = employees

    # object method to add employee
    def add_employee(self, emp):
        self.emplyees.append(emp)

    # object method to remove employee
    def remove_employee(self, emp):
        self.emplyees.remove(emp)

    # object method to display employee
    def print_employee(self):
        print("Manger: ", self.fullname)
        for emp in self.emplyees:
            print('Dev =>', emp.fullname)

# defining objects for Employee class
emp1 = Employee.from_strig('Ram-Charan-120000')
print(emp1.fullname)
print(emp1.email)


# defining objects for Developer class
dev1 = Developer('John','Kadam', 80000, 'Python')
dev2 = Developer('Dev', 'Patel', 75000, 'Python')
dev3 = Developer('Adam', 'Kurlf', 90000, 'Java')
dev4 = Developer('Kushal', 'Kaur', 95000, '.Net')

# defining object for Manager class
mgr01 = Manager('Kumar','Pai', 120000, [])
print("\nNo developers", sep='\n')
mgr01.print_employee()

print('\nAfter adding developers', sep='\n')
mgr01.add_employee(dev1)
mgr01.add_employee(dev2)
mgr01.add_employee(dev3)
mgr01.print_employee()

print('\nRemoving one developer',sep='\n')
mgr01.remove_employee(dev2)
mgr01.print_employee()

print('\nPrints the number of objects created with the class', sep='\n')
print(mgr01.num_of_emp)

print("\nClass method explained", sep='\n')
print("Before ", Employee.raise_amt)
Employee.set_raise_amt(1.20)
print("After ", Employee.raise_amt)
print("Developer ", dev1.raise_amt)
print("Manager ", mgr01.raise_amt)

# testing the static method
print("\nTesting static method")
curr_time = datetime.date.today()

print('{0} is working day ? {1}'.format(str(curr_time), Employee.is_workday(curr_time)))

