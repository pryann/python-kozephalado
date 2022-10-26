my_list = ['Oh', 'yeah', 'python', 'is', 'great']

for index in my_list:
    print(index)

for index in range(len(my_list)):
    print(my_list[index])

for key, value in enumerate(my_list):
    print('index: ', key, ' value: ', value)
