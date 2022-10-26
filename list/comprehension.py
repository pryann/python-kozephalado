my_list = [1,2,3,4,5]
# expression for item in iterable if condition is True
doubled_list = [item * 2 for item in my_list]
print(doubled_list)

even_nums = [num for num in my_list if num % 2 == 0]
print(even_nums)

fruits = ['apple', 'banana', 'orange', 'kiwi', 'mango']
new_fruits = [f if f != 'apple' else 'blueberry' for f in fruits]
print(new_fruits)

nums_list = [x for x in range(10)]
print(nums_list)

matrix = [[j for j in range(5)] for i in range(3)]

# matrix = []
# for i in range(3):
#     row = []
#     for j in range(5):
#         row.append(j)
#     matrix.append(row)

print(matrix)

planets = [
  ['Mercury', 'Venus', 'Earth'],
  ['Mars', 'Jupyter', 'Saturn'],
  ['Uranus', 'Neptune', 'Venus']
]

flat_planets = [planet for sublist in planets for planet in sublist if len(planet) < 6]

# flat_planets = []
# for sublist in planets:
#   for planet in sublist:
#     if len(planet) > 6:
#       flat_planets.append(planet)

print(flat_planets)