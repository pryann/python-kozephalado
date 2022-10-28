def generate_ints(n):
    for i in range(n):
        yield i


[*others] = generate_ints(10)
print(others)
