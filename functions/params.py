def print_person(name, age):
    print('name: ', name)
    print('age: ', age)


print_person(age=38, name='Gergő')


def def_param(a, b=0):
    return a + b


print(def_param(10))
