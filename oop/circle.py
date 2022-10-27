from math import pi


class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.__radius = value

    def area(self):
        return self.__radius**2 * pi


c = Circle(10)
# print(c.get_radius())
# c.set_radius(20)
# print(c.get_radius())
print(c.radius)
print(c.area())
