class Shape:
    def __init__(self):
        self.sides = 0

    def getArea(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.sides = 4

    def getArea(self):                      # override parent's method
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.sides = 0

    def getArea(self):                      # override parent's method
        return self.radius * self.radius * 3.142

shapes = [Rectangle(6, 10), Circle(7)]
print("Area of rectangle is:", str(shapes[0].getArea()))
print("Area of circle is:", str(shapes[1].getArea()))

# Advantages and key features of method overriding
    # 1 the derived classes can give their own specific implementations to inherited methods
    #   without modifying the parent class methods
    # 2 for any method, a child class can use the implementation in the parent class or make
    #   its own implementation
    # 3 method overriding needs inheritance, and there should be at least one derived class
    #   to implement it
    # 4 the methods in the derived classes usually have a dissimilar implementation
