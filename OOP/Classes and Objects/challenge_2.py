# Challenge 2: Calculate the Student's Performance

class Student:
    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def totalObtained(self):
        totalMarks = self.phy + self.chem + self.bio
        return totalMarks

    def percentage(self):
        perc = 100 * self.totalObtained() / 300
        return perc

student1 = Student('Maiuna', 90, 78, 70)

print(student1.percentage())