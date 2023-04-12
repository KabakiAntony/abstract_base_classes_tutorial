from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
	
    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)


class Square(Shape):
    def __init__(self, side_length):
    	self.side_length = side_length
    
    def area(self):
        return self.side_length ** 2
    
    def perimeter(self):
    	return 4 * self.side_length

              
def print_shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

square = Square(5)
rectangle = Rectangle(3,5)

print_shape_info(square)
print_shape_info(rectangle)
