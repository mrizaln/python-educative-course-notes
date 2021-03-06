# composition relationship are Part-of relationships where the part must constitute a segment of the whole object
# we can achieve composition by adding smaller parts of the other classes to make a complex unit

# in composition, the lifetime of the owned object depends on the lifetime of the owner

### exxample ###
# a car is composed of an enging, tires, and doors
# in this case, a xar owned these objects

class Engine:
    def __init__(self, capacity=0):
        self.capacity = capacity

    def printDetails(self):
        print("Engine Details:", self.capacity)

class Tires:
    def __init__(self, tires=0):
        self.tires = tires

    def printDetails(self):
        print("Number of tires:", self.tires)

class Doors:
    def __init__(self, doors=0):
        self.doors = doors

    def printDetails(self):
        print("Number of Doors:", self.doors)

class Car:
    def __init__(self, eng, tr, dr, color):
        self.eObj = Engine(eng)
        self.tObj = Tires(tr)
        self.dObj = Doors(dr)
        self.color = color

    def printDetails(self):
        self.eObj.printDetails()
        self.tObj.printDetails()
        self.dObj.printDetails()
        print("Car Color:", self.color)

car = Car(1600, 4, 2, "Grey")
car.printDetails()
