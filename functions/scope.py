y = 100


def outer_func():
    print(y)
    x = 200

    def inner_function():
        print(x)
    inner_function()


outer_func()


my_num = 100


def print_my_num():
    global my_num
    print(my_num)


print_my_num()
