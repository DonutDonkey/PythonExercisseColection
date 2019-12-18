from inheritance.animal.Animal import Animal
from inheritance.animal.mammals.Mammal import Mammal


def print_list(animal):
    animal.print_name()


a1 = Animal("a1")
m1 = Mammal("m1", "species")


animals = [a1, m1]

for a in animals:
    print_list(a)
