# Challenge 3: Implement a Calculator Class

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return (self.num1 + self.num2)

    def subtract(self):
        return (self.num2 - self.num1)

    def multiply(self):
        return (self.num1 * self.num2)

    def divide(self):
        return (self.num2 / self.num1)

someNumber = Calculator(10,214)

print(someNumber.add())
print(someNumber.subtract())
print(someNumber.multiply())
print(someNumber.divide())