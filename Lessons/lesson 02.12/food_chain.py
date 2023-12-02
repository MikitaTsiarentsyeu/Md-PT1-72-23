class Food:

    def __init__(self, name, f_type):
        self.name = name
        self.type = f_type

    def __str__(self) -> str:
        return self.name
    
class Animal:

    def __init__(self, name) -> None:
        self.name = name

    def eat(self, something):
        print(f"{self.name} eating {something}")

    def phe(self):
        print("phe...")

class Carnivore(Animal):

    eatable_food_types = ["meat"]

    def eat(self, something):
        if self.check_food(something):
            self.base_eat(something)
        else:
            super().phe()

    def check_food(self, food):
        return food.type in Carnivore.eatable_food_types

    def base_eat(self, something):
        Animal.eat(self, something)

class Herbivore(Animal):

    eatable_food_types = ["plant"]

    def eat(self, something):
        if self.check_food(something):
            self.base_eat(something)
        else:
            super().phe()

    def check_food(self, food):
        return food.type in Herbivore.eatable_food_types

    def base_eat(self, something):
        Animal.eat(self, something)

class Omnivore(Carnivore, Herbivore):

    def eat(self, something):
        if Carnivore.check_food(self, something):
            Carnivore.base_eat(self, something)
        elif Herbivore.check_food(self, something):
            Herbivore.base_eat(self, something)
        else:
            super().phe()

stake = Food("stake", "meat")
grass = Food("grass", "plant")

tigger = Carnivore("tigger")
cow = Herbivore("cow")
human = Omnivore("human")

for a in (human,):
    for f in stake, grass:
        a.eat(f)

# print(Omnivore.__mro__)