# hozzárendelhető változóhoz
def plus_one(number):
    return number+1


plus_one_var = plus_one
print(plus_one_var(10))

# átadható paraméterként


def function_call(func):
    number = 5
    return func(number)


print(function_call(plus_one))

# lehet visszatérési érték


def message():
    def say_hi(name):
        print('Hi ', name)
    return say_hi


result = message()
result('Gergő')
message()('Gergő')
