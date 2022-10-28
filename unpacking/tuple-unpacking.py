fruits = ('orange', 'banana', 'cherry', 'apple')
f1, f2, *others = fruits
print(f1, f2, others)

gen = (i**2 for i in range(3))
a, *more = gen

print(more)
