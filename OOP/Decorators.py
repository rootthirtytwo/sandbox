# parent class
class Employee():

    raise_amt = 1.05
    num_of_emp = 0

    # initializing
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        Employee.num_of_emp += 1

    @property
    def email(self):
        return self.fname+'.'+self.lname+'@company.com'

    @property
    def fullname(self):
        return self.fname.title()+' '+self.lname.title()

    @fullname.setter
    def fullname(self,name):
        self.fname, self.lname = name.split(' ')

    @fullname.deleter
    def fullname(self):
        print('Deleted the name')
        self.fname, self.lname = None, None

print('\nInitial values', sep='\n')
emp1 = Employee('John', 'Raid', 100000)
print(emp1.fullname)

print('\nAfter new values', sep='\n')
emp1.fname = 'Kirk'
print(emp1.fullname)
print(emp1.email)

print('\nExplaining setter', sep='\n')
emp1.fullname = 'Ram Charan'
print(emp1.fullname)
print(emp1.email)

print('\nExplaining deleter', sep='\n')
del emp1.fullname
