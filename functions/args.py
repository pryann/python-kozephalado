def my_fun(*args):
    # print(type(args))
    for arg in args:
        print(arg)


my_fun('oh', 'my', 'God', 'ddfd')


def my_fun_2(arg1, arg2, arg3, arg4):
    print(arg1)
    print(arg2)
    print(arg3)
    print(arg4)


my_list = ['Oh', 'my', 'holy', 'God']
my_fun_2(*my_list)


def my_fun_3(**kwargs):
    for key, value in kwargs.items():
        print(key, ' = ', value)


my_fun_3(first='Gergely', last='Gáll', age=38)


def revert_kwargs(first, last, age):
    print(first)
    print(last)
    print(age)


my_dict = {'first': 'Gergely', 'last': 'Gáll', 'age': 38}
revert_kwargs(**my_dict)
