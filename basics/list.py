# Sequence type: list, tuple

my_list = [1, 2, 1, 'banana', False, '1']

print(len(my_list))
my_list.append(10)
print(my_list)
my_list.insert(0, 10)
print(my_list)
print(my_list.count(1))
my_list.extend([20, 30, 40])
print(my_list)
my_list.reverse()
print(my_list)
my_list_nums = [234, 56, 123, 567, 123]
my_list_nums.sort()
print(my_list_nums)
print(my_list[0])
my_list.remove(1)
print(my_list)
print(' '.join(['Oh', 'áááüüűű', 'python', 'is', 'great']))
