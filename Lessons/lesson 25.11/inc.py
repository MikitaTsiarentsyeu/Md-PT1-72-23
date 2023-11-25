class Dog:

    def __init__(self, name, breed, color, age):
        self.name = name
        self.breed = breed
        if self.breed == "wss":
            self.color = "white"
        else:
            self.color = color
        self.set_age(age)

    def get_age(self):
        return f"{self.__age} years"

    def set_age(self, age):
        if age < 0:
            age = 0
        self.__age = age

    # def test(self):
    #     print(self, id(self))

d1 = Dog("Zefirka", "wss",  "color", 3)
d2 = Dog("Max", "shepherd", "mixed", 2)

print(Dog.__dict__)
print(d1.__dict__)
print(d2.__dict__)

d1.set_age(10)
print(d1.get_age())