# Challenge 1: Override a Method using the Super Function

class Shape:
    sname = "Shape"

    def getName(self):
        return sname

class XShape(Shape):
    # initializer
    def __init__(self, name):
        self.xsname = name

    def getName(self):  # overriden method
        return ("{}, {}".format(super().sname, self.xsname))

circle = XShape("Circle")
print(circle.getName())
