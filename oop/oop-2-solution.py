class Person:
    def __init__(self, fname, lname, age, address):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.address = address

    def get_name(self):
        return f'{self.fname} {self.lname}'


class Employee(Person):
    def __init__(self, fname, lname, age, address, salary, role, manager=None):
        super().__init__(fname, lname, age, address)
        self.salary = salary
        self.role = role
        self.manager = manager

    def set_manager(self, manager):
        self.manager = manager


class Manager(Person):
    def __init__(self, fname, lname, age, address, employees):
        super().__init__(fname, lname, age, address)
        self.employees = employees

    def print_employees(self):
        for emp in self.employees:
            print(emp.fname)


# END SOLUTION
p1 = Person('Istvan', 'Kiss', 55, '1111, Bp, Nagy Utca 8')
e1 = Employee('Istvan', 'Kiss', 55,
              '1111, Bp, Nagy Utca 8', 1000.0, 'developer')
e2 = Employee('Pista', 'Kiss', 55,
              '1111, Bp, Nagy Utca 8', 1000.0, 'developer')
m1 = Manager('Istvan', 'Kiss', 55, '1111, Bp, Nagy Utca 8', [e1, e2])

m1.print_employees()
