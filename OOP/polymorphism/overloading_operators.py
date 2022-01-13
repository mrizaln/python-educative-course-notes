# operators in python can be overloaded to operate in a certain user-defined way

# when class is defined, its objects can interract with each other through the operators
# but it is necessary to define the behaviour of these operators through operator overloading

#### we are going to implement a class that represent a complex number ####

class Com:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):       # overrides the '+' operator
        temp = Com(self.real + other.real, self.imag + other.imag)
        return temp

    def __sub__(self, other):
        temp = Com(self.real - other.real, self.imag - other.imag)
        return temp

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        temp = Com(real, imag)
        return temp

obj1 = Com(3, 7)
obj2 = Com(2, 5)

obj3 = obj1 + obj2
obj4 = obj1 - obj2
obj5 = obj1 * obj2

print("real of obj3:", obj3.real)
print("imag of obj3:", obj3.imag)
print("real of obj4:", obj4.real)
print("imag of obj4:", obj4.imag)
print("real of obj5:", obj5.real)
print("imag of obj5:", obj5.imag)

#### Special functions for some common operators ####
#    +       __add__(self, other)
#    -       __sub__(self, other)
#    /       __truediv__(self, other)
#    *       __mul__(self, other)
#    <       __lt__(self, other)
#    >       __gt__(self, other)
#    ==      __eq__(self, other)
