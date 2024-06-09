# Створи абстрактний клас 
# Shape та додай метод area, успадкуйся від цього класу та створи два класи 
# Rectangle та Circle реалізувавши метод area. 
# Створи інстанси класів Circle та Rectangle та виклич метод area.
from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
    
class Rectangle(Shape):
    
    def __init__(self, width, height):
        self.check_correct_paramaters(width, height)
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

    @staticmethod
    def check_correct_paramaters(width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Weight and Height must be more than zero")


class Circle(Shape):
    
    def __init__(self, radius):
        self.check_radius(radius)
        self.radius = radius
        
    def area(self):
        return 2*pi*self.radius
    
    @staticmethod
    def check_radius(radius):
        if radius <= 0:
            raise ValueError("Radius cannot be less or equal than zero")
    

rectangle = Rectangle(3,4)
circle = Circle(5)

print(circle.area())
print(rectangle.area())
