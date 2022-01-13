class myClass:
    pass

obj = myClass()

print("\n\n")

class Employee():
    # defining initializer of a class
    def __init__(self, ID=None, salary=0, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department


### ngajieun object anu class na tanpa __init__ atau __init__ na make default value
# creating an object
Alex = Employee()

# assigning values to Alex object
Alex.ID = 3319
Alex.salary = 2000
Alex.department = "Human Resources"
# creating new attribute to Alex
Alex.title = "Vice Manager"

print("ID :", Alex.ID)
print("Salary :", Alex.salary)
print("Department :", Alex.department)
print("title :", Alex.title)
print()

# creating object + langsung ngeusian attributna pake __init__
Steve = Employee(3789, 2500, "Human Resources")

print("ID :", Steve.ID)
print("salary :", Steve.salary)
print("department :", Steve.department)

