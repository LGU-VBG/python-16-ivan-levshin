from math import pi


class Circle:
    def __init__(self,radius):
        self._radius = radius
        self._diameter = 2 * self._radius
        self._area = pi * radius ** 2

    @property
    def radius(self):
        return self._radius
    
    @property
    def area(self):
        return self._area
    
    def get_radius(self):
        return self._radius
    
    def get_diameter(self):
        self._diameter = 2*self._radius
        return self._diameter
    
    def get_area(self):
        self._area = pi * self._radius ** 2
        return self._area
    

circle = Circle(5)
print(circle.get_radius())
print(circle.get_diameter())
print(circle.get_area())