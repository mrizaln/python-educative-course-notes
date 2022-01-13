# There are 5 types of inheritance
    # 1 single
    # 2 multi-level
    # 3 hierarchical
    # 4 multiple 
    # 5 hybrid

# =================================================================================
### single ###
    # there is only single class extending from another class

class Vehicle:
    def setTopSpeed(self, speed):
        self.topSpeed = speed
        print("Top speed is set to", self.topSpeed)

class Car(Vehicle):
    def openTrunk(self):
        print("Trunk is now open")

corolla = Car()
corolla.setTopSpeed(220)
corolla.openTrunk()
print()

# =================================================================================
### multi-level ###
    # when a class is derived from a class that is derived from another class

class Hybrid(Car):
    def turnOnHybrid(self):
        print("Hybrid mode is now turned on")

priusPrime = Hybrid()
priusPrime.setTopSpeed(250)
priusPrime.openTrunk()
priusPrime.turnOnHybrid()
print()

# =================================================================================
### hierarchical ###
    # more than one class extend from the same base class

class Truck(Vehicle):       # Truck class derived from Vehicle class but also Car class
    def setMaxLoad(self, load):
        self.maxLoad = load
        print("This truck maximum load is set to", self.maxLoad, "kg")

volvo = Truck()
volvo.setTopSpeed(120)
volvo.setMaxLoad(1012)
print()

# =================================================================================
### multiple inheritance ###
    # when a class is derived from more than one base class

class CombustionEngine:
    def setTankCapacity(self, tankCapacity):
        self.tankCapacity = tankCapacity

class ElectricEngine:
    def setChargeCapacity(self, chargeCapacity):
        self.chargeCapacity = chargeCapacity

class HybridEngine(CombustionEngine, ElectricEngine):
    def printDetails(self):
        print(f"Tank capacity   : {self.tankCapacity}")
        print(f"Charge capacity : {self.chargeCapacity}")

areils = HybridEngine()
areils.setTankCapacity("20 L")
areils.setChargeCapacity("250 W")
areils.printDetails()
print()

# =================================================================================
### hybrid inheritance ###
    # type of inheritance that is a combination of multi-level and multiple inheritance

class Engine:  # Parent class
    def setPower(self, power):
        self.power = power


class CombustionEngine(Engine):  # Child class inherited from Engine
    def setTankCapacity(self, tankCapacity):
        self.tankCapacity = tankCapacity


class ElectricEngine(Engine):  # Child class inherited from Engine
    def setChargeCapacity(self, chargeCapacity):
        self.chargeCapacity = chargeCapacity

# Child class inherited from CombustionEngine and ElectricEngine


class HybridEngine(CombustionEngine, ElectricEngine):
    def printDetails(self):
        print("Power:", self.power)
        print("Tank Capacity:", self.tankCapacity)
        print("Charge Capacity:", self.chargeCapacity)


Ediosoin = HybridEngine()
Ediosoin.setPower("2000 CC")
Ediosoin.setChargeCapacity("250 W")
Ediosoin.setTankCapacity("20 Litres")
Ediosoin.printDetails()