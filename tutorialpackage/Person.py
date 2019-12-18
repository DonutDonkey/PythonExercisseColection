class Person:
    personCount = 0

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        Person.personCount += 1

    def displayFirstName(self):
        print(self.firstName)

    @staticmethod
    def staticShit():
        print('some static shit')


p1 = Person('Jan', 'Kowalski')
p2 = Person('Bartosz', 'Flipsiarski')

print(Person.personCount)
Person.staticShit()
p1.displayFirstName()
