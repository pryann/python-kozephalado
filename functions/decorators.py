def uppercase_decorator(function):
    def wrapper():
        result = function()
        make_uppercase = result.upper()
        return make_uppercase
    return wrapper


def split_string(*args, **kwargs):

    def wrapper(function):
        result = function()
        splitted_str = result.split()
        return splitted_str
    return wrapper


@split_string(test='it works')
def say_hi():
    return 'Csao Bella!'


# decorate = uppercase_decorator(say_hi)
# print(decorate())

print(say_hi())

# def decorator_function(function_name):  
#   print("Inside the Decorator: ")  
   
#   def inner_1(*args, **kwargs):  
#     print("Inside the Inner Function: ")  
#     print("'Decorated the function'")      
#     function_name()  
#   return inner_1  
   
# @decorator_function  
# def function_to():  
#     return 'hi'
   
# function_to()  