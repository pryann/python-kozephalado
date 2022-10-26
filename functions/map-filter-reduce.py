from functools import reduce


my_list = [1,5,4,6,11,3,2]
my_doubles_list = list(map(lambda x: x * 2, my_list))

print(my_doubles_list)

even_list = list(filter(lambda x: (x % 2 == 0), my_list))
print(even_list)

sum_list = reduce(lambda a,b: a+b, my_list)
print(sum_list)