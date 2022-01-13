class Player:
    teamName = "Liverpool"           # class variable
    teamMembers = []

    def __init__(self, name):
        self.name = name             # instance variable
        self.formerTeams = []
        self.teamMembers.append(self.name)

    # a class method to get team name from class variable
    @classmethod
    def getTeamName(cls):
        return cls.teamName

    # a static method
    @staticmethod
    def demo():
        print("I am a static method!")

p1 = Player("lol")

print(p1.name)

# calling class method
print(Player.getTeamName())
print()

# calling static method
p1.demo()           # static method can be called by its object name 
Player.demo()       # or its class name
print("\n")

#============================================================================================================
# Static methods do not know anything about the state of the class, i.e., they cannot modify class attributes
# The purpose of a static method is to use its parameters and produce a useful result
#============================================================================================================

class BodyInfo:

    @staticmethod
    def bmi(weight, height):
        return weight / (height**2)


weight = 75
height = 1.8
print(BodyInfo.bmi(weight, height))