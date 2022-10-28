import sys


print(sys.getsizeof({}))
a = 'loremsdsdsd ipsum dolor blabla'
print(sys.getsizeof(a))
print(sys.getrefcount(a))
