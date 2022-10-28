# 4 féle import
# import math
# from math import cos, sin, sqrt
# from math import *
# import math as m

#  import time
#  import time as t
#  from time import sleep
#  from time import sleep, localtime
#  from time import sleep as s
#  from math import sqrt
#  from cmath import sqrt as csqrt
#  from package.module import function


from mymodule import print_hi
from mymodule2 import print_hi as print_hi_2
from package.module import log

log()
print_hi('Gergő')
print_hi_2('Gergő')


# csak adott adatok importálása
# Két modulban ugaynolyan néven van függvény, az 1. felülíródik
# from mymodule import print_hi
# from mymodule2 import print_hi

# print_hi('Gergő')

# Teljes modul importálása
# import mymodule

# mymodule.print_hi('Gergő')
# mymodule.print_talk('message')
