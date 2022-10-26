my_tuple = (1, 1, 2, 3)

print(len(my_tuple))
print(my_tuple.count(1))
print(my_tuple.index(2))
# TypeError: 'tuple' object does not support item assignment
# my_tuple[0] = 0

my_tuple = (True)
print(type(my_tuple))

summa = (20 + 30) * 10
print(summa)

my_tuple_x = ('banana', 'apple', 'orange')
b, _, o = my_tuple_x
print(b)
