def uppercase_decorator(function):
    def wrapper():
        result = function()
        make_uppercase = result.upper()
        return make_uppercase
    return wrapper


def split_string(function):
    def wrapper():
        result = function()
        splitted_str = result.split()
        return splitted_str
    return wrapper

@split_string
@uppercase_decorator
def say_hi():
    return 'Csao Bella!'


# decorate = uppercase_decorator(say_hi)
# print(decorate())

print(say_hi())
