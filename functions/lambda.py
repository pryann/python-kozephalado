def add_one(numbers_list):
    result = []
    for number in numbers_list:
        atomic_result = number + 1
        result.append(atomic_result)
    return result


print(add_one([1, 2, 3]))


def apply(numbers_list, function):
    result = []
    for number in numbers_list:
        atomic_result = function(number)
        result.append(atomic_result)
    return result


def multiply(number):
    return number*2


def increase(number):
    return number+1


print(apply([1, 2, 3, 4, 5], multiply))
print(apply([1, 2, 3, 4, 5], increase))


# def doubled(a):
#   return a*2

doubled = lambda a : a*2 
print(doubled(5))

summarize = lambda a,b : a+b
print(summarize(10,1))

def make_incrementor(n):
  return lambda x: x+n

print(make_incrementor(42)(3))