# when the name "method" mentioned anywhere here, it refers to instance method

class Employee():
    # defining initializer of the class
    def __init__(self, ID=None, salary=0, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department

    # defining methods of the class
    def tax(self):
        return (self.salary * 0.2)

    def salaryPerDay(self):
        return (self.salary / 30)

    # method overloading
    def demo(self, a, b, c, d=5, e=None):
        print("a =", a)
        print("b =", b)
        print("c =", c)
        print("d =", d)
        print("e =", e)

Steve = Employee(3789, 2500, "Human Resources")

print("ID                       :", Steve.ID)
print("Salary                   :", Steve.salary)
print("Department               :", Steve.department)
print("Tax paid by Steve        :", Steve.tax())
print("Salary per day of Steve  :", Steve.salaryPerDay())

# printing overloading demo
print("\n")
print("Demo 1")
Steve.demo(1, 2, 3)
print("\n")
print("Demo 2")
Steve.demo(1, 2, 3, 4)
print("\n")
print("Demo 3")
Steve.demo(1, 2, 3, 4, 5)