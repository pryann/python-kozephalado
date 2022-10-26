def increment(arg):
    return arg+1


def decrement(arg):
    return arg-1


def chain(start, *funcs):
    result = start
    for func in funcs:
        result = func(result)
    return result


print(chain(1, increment, increment, increment, decrement))

# NOOO WAY
# val = 1
# val_2 = decrement(increment(increment(val)))
