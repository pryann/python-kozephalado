class Person:
    def __init__(self, first_name, last_name, job, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.__salary = salary

    def print_name(self):
        print(self.first_name, self.last_name)

    def set_salary(self, value):
        if (value < self.__salary * 1.1):
            self.__salary *= 1.1
        else:
            self.__salary = value

    def get_salary(self):
        return int(self.__salary)


person_1 = Person('John', 'Doe', 'developer', 50000)
person_1.print_name()

person_2 = Person('Jane', 'Doe', 'administrator', 20000)
person_2.print_name()

person_1.set_salary(5000)
print(person_1.get_salary())
