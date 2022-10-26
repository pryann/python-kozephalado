my_dict = {
    'name': 'Gáll Gergely',
    'age': 38
}

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

print(my_dict['name'])
my_dict['job'] = 'mentor'
print(my_dict)
my_dict.pop('name')
print(my_dict)
my_dict['job'] = 'teacher'
print(my_dict)
my_dict.update({'job': 'frontend dev', 'x': 10})
print(my_dict)
