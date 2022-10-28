# file = open('alorem.txt', 'w')
# file.write('hi')
# file.close()

with open('lorem.txt', 'w', 4096, 'utf-8') as file:
    file.write('new content')

with open('lorem.txt', 'r', 4096, 'utf-8') as file:
    print(file.read())
    file.seek(0)
    print(file.read())
