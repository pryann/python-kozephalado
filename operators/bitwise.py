# &=	Perform bitwise “AND” operation and assign	x &= y
# |=	Perform bitwise “OR” operation and assign	x |= y
# ^=	Perform bitwise “xOR” operation and assign	x ^= y
# >>=	Perform bitwise “Right Shift” operation and assign	x >>= y
# <<=	Perform bitwise “Left Shift” operation and assign	x <<= y

# In Python, bitwise operations are performed on integers. 
# The integers are first converted into binary format and then operations 
# are performed on every bit. The result is returned in decimal format.

x = 3
y = 2

x &= y
print(x)

# Explanation

# x = 3 --> binary format = 0011
# y = 2 --> binary format = 0010

# x & y = 0011
#          &
#         0010
#       = 0010

x = 3
y = 2

x |= y
print(x)

# x = 3 --> binary format = 0011
# y = 2 --> binary format = 0010

# x & y = 0011
#          |
#         0010
#       = 0011

x = 3
y = 2

x ^= y
print(x)
# x = 3 --> binary format = 0011
# y = 2 --> binary format = 0010

# x & y = 0011
#          ^
#         0010
#       = 0001


x = 3
y = 2

x >>= y
print(x)

# x = 3 --> binary format = 0011
# y = 2 

# x >> y = 0011 >> 2 (Move right by two places)
#        = 0000

x = 3
y = 2

x <<= y
print(x)

# x = 3 --> binary format = 0011
# y = 2 

# x << y = 0011 << 2 (Move left by two places)
#        = 1100

# Walrus Operator
# x = 3
# print(x)

print(x:=3)
