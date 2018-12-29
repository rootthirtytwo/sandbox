class Parent():

    # Class attribute
    country = 'USA'

    # Initializer/Instance attribute
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.country = 'Canada'

    #class method
    def get_email(self):
        return self.fname+'.'+self.lname+'@company.com'

    # representation method definition
    def __repr__(self):
        return self.lname.title()+', '+self.fname.title()

class Child(Parent):

    def __init__(self,fname, lname, sex):
        super().__init__(fname,lname)
        self.sex = sex

    def get_age(self, sex):
        return '{0} age is {1}'.format(self.fname, sex)

    def __repr__(self):
        return '{0} {1} is a {2}'.format(self.fname,self.lname, self.sex)

class Sibling(Parent):
    # overriding class attribute
    country = 'Canada'
    pass

# Instantiating Objects
obj1 = Parent('John', 'legend')

print(obj1.fname, obj1.lname, obj1.country, obj1.get_email())

obj2 = Parent('John', 'Hash')
obj2.country = 'Japan'

# notice you can not override the value of class attribute with assignment operator until unless it is a class method
print(obj1.fname, obj1.lname, obj1.country, obj2.get_email())

# printing the type of an object
print(type(obj1))

# repr - function usage explained
print(obj1)

# Object from child class
obj3 = Child('Shan', 'Davis', 'Boy')
print(obj3.get_email())
print(obj3.get_age(20))
print(obj3)

# check whether the object created with child class is instance of Parent
print(isinstance(obj3, Parent))


obj4 = Sibling('Adam','Guy')
# Sibling inherits Parent not the child and this can not access the attributes or methods from Child class
print(isinstance(obj4, Child))

# overriding
print(obj4.country)

