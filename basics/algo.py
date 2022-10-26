# Összegzés

def summarize(values):
    sum_value = 0
    for value in values:
        sum_value += value
    return sum_value


print(summarize([10, 20, 30, 40, 50]))
print(sum([10, 20, 30, 40, 50]))


# Megszámlálás - adott elem hányszor van benne

def count_values(values, search):
    counter = 0
    for value in values:
        if value == search:
            counter += 1
    return counter


print(count_values([1, 1, 2, 3], 1))
print([1, 1, 2, 3].count(1))


# Minimum kiválasztás


def minimum(values):
    min_value = values[0]
    for index in range(1, len(values)):
        if values[index] < min_value:
            min_value = values[index]
    return min_value


print(minimum([10, 20, 30, 40, 50, 1]))
print(min([10, 20, 30, 40, 50, 1]))

# Maximum kiválasztás


def maximum(values):
    max_value = values[0]
    for index in range(1, len(values)):
        if values[index] > max_value:
            max_value = values[index]
    return max_value


print(maximum([10, 20, 30, 40, 50, 1]))
print(max([10, 20, 30, 40, 50, 1]))

# Eldöntés - True, False


def contains_or_not(values, search):
    for value in values:
        if value == search:
            return True
    return False


print(contains_or_not([10, 20, 30, 40, 50, 1], 10))
print(10 in [10, 20, 30, 40, 50, 1])

# Kiválasztás - tudjuk, hogy benne van, az index kell


def get_index(values, element):
    for index in range(len(values)):
        if values[index] == element:
            return index


print(get_index([10, 20, 30, 40, 50, 1], 20))
print([10, 20, 30, 40, 50, 1].index(20))

# Lineáris keresés - adjuk vissza az idnexet, ha benne van


def linear_search(values, element):
    for index in range(len(values)):
        if values[index] == element:
            return index
    return -1


print(get_index([10, 20, 30, 40, 50, 1], 20))
print([10, 20, 30, 40, 50, 1].index(20))
