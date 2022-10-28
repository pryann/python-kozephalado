def f1():
    x = 10
    return 10


def f2():
    y = f1()
    return y


def f3():
    z = f2()
    return z


f3()

g = 1


def f4():
    x = 10

    def f5():
        y = 11

        def f6():
            print(x, y)
            z = 12


f4()
