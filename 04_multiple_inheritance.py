# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance


class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "Class A"


class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "Class B"


class C(A, B):
    def __init__(self):
        super().__init__()

    def show_props(self):
        print(self.foo)
        print(self.bar)
        print(self.name)


c = C()

# python looks up super classes in the order they are defined, hence it will print "Class A" as its name
c.show_props()
# print the __mro__ (method resolution order)
print(C.__mro__) # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
