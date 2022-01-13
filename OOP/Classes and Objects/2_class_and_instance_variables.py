class Player:
    teamName = "Liverpool"           # class variable
    teamMembers = []

    def __init__(self, name):
        self.name = name             # instance variable
        self.formerTeams = []
        self.teamMembers.append(self.name)

p1 = Player('Mark')
p2 = Player('Steve')

p1.formerTeams.append("Barcelona")
p2.formerTeams.append("Chelsea")

p1.teamName = 'asdfjh'

print('\nplayer name :', p1.name)
print('team name   :', p1.teamName, p1.teamMembers)
print('former teams:', p1.formerTeams)

print('\nplayer name :', p2.name)
print('team name   :', p2.teamName, p2.teamMembers)
print('former teams:', p2.formerTeams)