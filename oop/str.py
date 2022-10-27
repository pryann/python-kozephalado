class Person:
    def __init__(self, fname, lname):
        self.lname = lname
        self.fname = fname

    def __str__(self):
        return f'Person first name: {self.fname}, lastname: {self.lname}'


p = Person('Shaka', 'Zulu')
print(p)
