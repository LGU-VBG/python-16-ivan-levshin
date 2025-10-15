class Rectangle:
    def __init__(self,length,width):
        self._length = length
        self._width = width

    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self,value):
        self._length = value

    @property
    def widht(self):
        return self._width
    
    @widht.setter
    def widht(self,value):
        self._width = value

    @property
    def perimeter(self):
        return 2 * (self._length + self._width)
    
    @property
    def area(self):
        return self._length + self._width
    
rectangle = Rectangle(4,5)
rectangle._length = 2
rectangle._width = 3
print(rectangle._length)
print(rectangle._width)
print(rectangle.perimeter)
print(rectangle.area)