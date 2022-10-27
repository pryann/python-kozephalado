my_set = {1, 2, 3, ('banana', 'orange'), 1}
print(my_set, type(my_set))

my_set.add('new item')
print(my_set)

my_set.update([10, 11, 12])
print(my_set)

my_set.remove(1)
print(my_set)

my_set_1 = {1, 2, 3, 4}
my_set_2 = {3, 4, 5, 6}

print(my_set_1.union(my_set_2))
print(my_set_1.difference(my_set_2))
print(my_set_1.intersection(my_set_2))

my_set_3 = {2, 3}
print(my_set_3.issubset(my_set_1))
print(my_set_1.issuperset(my_set_3))

print(list(set([1, 2, 3, 3, 3])))
