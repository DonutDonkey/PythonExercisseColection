from inheritance.animal.Animal import Animal


class Mammal(Animal):

    def __init__(self, name, species):
        super().__init__(name)
        self.species = species

    def print_species(self):
        print(self.species)

    def print_name(self):
        print(self.name + ' is a ' + self.species)