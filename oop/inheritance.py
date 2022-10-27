class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.__lname = lname

    def print_name(self):
        print(self.fname, self.__lname)


class Student(Person):
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname)
        self.age = age

    def welcome(self):
        print('Welcome', self.fname)

    def print_name(self):
        super().print_name()
        print('Print student name: ', self.fname, self._Person__lname)


p1 = Person('Gergely', 'Gáll')
p1.print_name()

s1 = Student('John', 'Doe', 33)
s1.print_name()
s1.welcome()
