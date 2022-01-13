# Challenge 1: Implement Rectangle Class Using the Encapsulation

class Rectangle:
    def __init__(self, length=None, width=None):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)

sebuah_kotak = Rectangle(12,124)

print(sebuah_kotak.area())
print(sebuah_kotak.perimeter())