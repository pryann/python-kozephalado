x = 1
y = 1
z = x

print('x', hex(id(x)))
print('y', hex(id(y)))
print('z', hex(id(z)))

z = 10
print('z', hex(id(z)))

my_list = [x, 1, 2]
print(hex(id(my_list[0])))

print(1 == 1)
# print(1 is 1)
