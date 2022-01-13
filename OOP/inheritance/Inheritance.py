# Inheritance provides a way to create a new class from an existing class.
# The new class is a specialized version of the existing class such that it inherits 
# all the non-private fields (variables) and methods of the existing class. 

# In inheritance, in order to create a new class based on an existing class, we use the following terminology:

    # 1. Parent Class (Super Class or Base Class): This class allows the reuse of its public properties in another class.
    # 2. Child Class (Sub Class or Derived Class): This class inherits or extends the superclass.

# Basic Syntax:

#     class ParentClass:
#         # attributes of the parent class

#     class ChildClass(ParentClass):
#         # properties of the child class

class Vehicle:
    fuelCap = 90
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model
    
    def printDetails(self):
        print("Manufacturer : ", self.make)
        print("Color        : ", self.color)
        print("Model        : ", self.model)

class Car(Vehicle):
    fuelCap = 20
    def __init__(self, make, color, model, doors):
        super().__init__(make, color, model)                    # sama
        # Vehicle.__init__(self, make, color, model)             # sama
        self.doors = doors

    def printCarDetails(self):
        self.printDetails()
        print("Doors        : ", self.doors)

    def display(self):
        print("Fuel cap of Vehicle class : ", super().fuelCap)
        print("Fuel cap of Car class     : ", self.fuelCap)


sebuah_mobil = Car("Suzuki", "blue", 2015, 4)
sebuah_mobil.printCarDetails()
sebuah_mobil.display()

# =================================================================================
### advantages of inheritance ###
    # reusability         : can used can be used multiple times without duplicating it
    # code modification   : if code is used in several places, it will be easier to modify
    #                       and prevent inconsistencies that can lead to bugs
    # extensibility       : using inheritance one can extend the base class as per requirements
    #                       of the derived class
    # data hiding         : base class can keep some data private by encapsulating it
    #                       thus the derived class can't alter it