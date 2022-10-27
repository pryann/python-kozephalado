my_str = 'Banana'
my_str_iterator = iter(my_str)

print(next(my_str_iterator))
print(next(my_str_iterator))
print(next(my_str_iterator))
print(next(my_str_iterator))
print(next(my_str_iterator))
print(next(my_str_iterator))
# print(next(my_str_iterator))  # Error

my_tuple = ('apple', 'banana', 'orange')
my_tuple_iterator = iter(my_tuple)
print(next(my_tuple_iterator))
