class Method():

    def __init__(self, age):
        self.age = age

    def __repr__(self):
        return f'({self.age!r})'

    # instance method
    def reg_method(self):
        return self.stc_method(self.age)

    # class method
    @classmethod
    def cls_method(cls):
        return cls('Class Method')

    # static method
    @staticmethod
    def stc_method(age):
        if age >= 60:
            return 'Senior Citizen'
        else:
            return 'Adult'

obj = Method(60)

print(obj.reg_method())
print(Method.reg_method(obj))


print(obj.cls_method())
print(Method.cls_method())

print(obj.stc_method(20))
print(Method.stc_method(80))

