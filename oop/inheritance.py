class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def print_name(self):
        print(self.fname, self.lname)


class Student(Person):
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname)
        self.age = age

    def welcome(self):
        print('Welcome', self.fname)

    def print_name(self):
        print('Print student name: ', self.fname)


p1 = Person('Gergely', 'Gáll')
p1.print_name()

s1 = Student('John', 'Doe', 33)
s1.print_name()
s1.welcome()
