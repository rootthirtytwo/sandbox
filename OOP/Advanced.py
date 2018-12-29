# parent class
class Employee():

    raise_amt = 1.05

    # initializing
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.fullname = self.fname.title()+' '+self.lname.title()
        self.email = self.fname+'.'+self.lname+'@company.com'
        self.pay = pay

    # representation method
    def __repr__(self):
        return self.fname.title()+' '+self.lname.title()

    # object method
    def raise_pay(self):
        self.pay = ( self.pay * self.raise_amt )

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
        for emp in self.emplyees:
            print('==>', emp.fullname)

# defining objects for Developer class
dev1 = Developer('John', 'Kadam', 80000, 'Python')
dev2 = Developer('Dev', 'Patel', 75000, 'Python')
dev3 = Developer('Adam', 'Kurlf', 90000, 'Java')

# defining object for Manager class
mgr01 = Manager('Kumar','Pai', 120000, [])
print("No developers")
print(mgr01.fullname)
mgr01.print_employee()

print('\nAfter adding developers', sep='\n')
mgr01.add_employee(dev1)
mgr01.add_employee(dev2)
mgr01.add_employee(dev3)
mgr01.print_employee()

print('\nRemoving one developer',sep='\n')
mgr01.remove_employee(dev2)
mgr01.print_employee()

