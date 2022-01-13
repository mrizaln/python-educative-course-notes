# Challenge 2: Implement the Complete Student Class

class Student:                      # tanpa initializer, parameter diset ku setter method
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

    def getRollNumber(self):
        return self.__rollNumber
    
saya = Student()

saya.setName("Morinaka Saya")
saya.setRollNumber(12)

print("Name :", saya.getName(), "\nRoll Number :", saya.getRollNumber())