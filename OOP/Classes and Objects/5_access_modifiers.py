#========================================================================================================================
# In Python, we can impose access restrictions on different data members and member functions
# The restrictions are specified through access modifiers
# Access modifiers are tags we can associate with each member to define which parts of the program can access it directly
#========================================================================================================================

### Public attributes ###
# Public attributes are those that can be accessed inside the class and outside the class
# Technically in Python, all methods and properties in a class are publicly available by default

class Employee:
    def __init__(self, ID, salary):
        # all properties are public
        self.ID = ID
        self.salary = salary    # salary is a public property

    def displayID(self):
        print("ID:", self.ID)


Steve = Employee(3789, 2500)
Steve.displayID()
print(Steve.salary)

### Private attributes (and methods) ###
# Private attributes cannot be accessed directly from outside the class but can be accessed from inside the class
# We can make members private using the double underscore __ prefix
# Methods are usually public since they provide an interface for the class properties and the main code to interact \
# with each other.

class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # salary is a private property

    def displaySalary(self):  # displaySalary is a public method
        print("Salary:", self.__salary)

    def __displayID(self):  # displayID is a private method
        print("ID:", self.ID)


Steve = Employee(3789, 2500)
print("ID:", Steve.ID)

try:
    print("Salary:", Steve.__salary)  # this will cause an error
except:
    print("there's an error")

print()
Steve.displaySalary()

try:
    Steve.__displayID()  # this will generate an error
except:
    print("there's an error")

# accessing a private property, (notice the underscore then classname before the private attribute; <_Employee> as prefix)
print()
print(Steve._Employee__salary)  # accessing a private property