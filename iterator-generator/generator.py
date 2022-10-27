def generate_abc():
    yield 'a'
    yield 'b'
    yield 'c'


for i in generate_abc():
    print(i)


def generate_ints(n):
    print('start it')
    for i in range(n):
        yield i
    print('end it')


counter = generate_ints(10)
print(next(counter))
print(next(counter))
print(next(counter))


def generate_id(start_value):
    inc = start_value
    while True:
        inc = inc + 1
        yield inc


id = generate_id(10)
print(next(id))
print(next(id))

id2 = generate_id(1)
print(next(id2))
print(next(id2))

print(next(id))

# Lezárás
id.close()
