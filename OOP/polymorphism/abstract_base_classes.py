from abc import ABC, abstractmethod


class Shape(ABC):  # Shape is a child class of ABC
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return (self.length * self.length)

    def perimeter(self):
        return (4 * self.length)

#shape = Shape()     # will generate an error


square = Square(4)
# this code will not generate an error since abastract methods have been
# defined in the child class, Square


### by using abstact base classes, we can controll classes whose objects can or cannot be created

### note: methods with @abstactmethod decorators must be defined in the child class
