from tutorialpackage.Person import Person


class Pzu:

    def __init__(self):
        self.personList = []

    def addPerson(self, person):
        self.personList.append(person)

    def printAllPeople(self):
        for p in self.personList:
            p.displayFirstName()
            # print(p.displayFirstName()) prints NONE since two print functions are called


p0 = Person('A', 'A')
p1 = Person('B', 'B')
p2 = Person('C', 'C')

pzu = Pzu()
pzu.addPerson(p0)
pzu.addPerson(p1)
pzu.addPerson(p2)
pzu.printAllPeople()
