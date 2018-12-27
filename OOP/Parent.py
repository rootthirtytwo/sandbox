class Parent():

    # Class attribute
    country = 'USA'

    # initializer/Instance attribute
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    #class method
    def get_email(self):
        return self.fname+'.'+self.lname+'@company.com'

    # property decorator
    @property
    def email(self):
        return self.fname+'.'+self.lname+'@company.com'

    # reprentation method definition
    def __repr__(self):
        return self.lname.title()+', '+self.fname.title()

# Instantiating Objects
obj1 = Parent('John', 'legend')

print(obj1.fname, obj1.lname, obj1.country, obj1.get_email())

obj2 = Parent('John', 'Hash')
obj2.country = 'Japan'

# notice you can not override the value of class attribute with assignment operator until unless it is a class method
print(obj1.fname, obj1.lname, obj1.country, obj2.email)

# printing the type of an object
print(type(obj1))

# repr - function usage explained
print(obj1)




