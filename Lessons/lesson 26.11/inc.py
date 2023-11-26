class Dog:

    __breeds = ['wss', 'shepherd', 'dog', 'setter', 'pointer']
    __default_breed_number = -1

    def __init__(self, name, breed, color, age):
        self.name = name
        self.__dog_breed = breed
        if self.__dog_breed == "wss":
            self.color = "white"
        else:
            self.color = color
        self.__set_age(age)

    def __set_breed(self, breed):
        if breed in Dog.__breeds:
            self.__breed = breed
        else:
            self.__breed = Dog.__breeds[Dog.__default_breed_number]

    def get_breed(self):
        return self.__breed

    __dog_breed = property(get_breed, __set_breed)
    breed = property(get_breed)

    def get_age(self):
        return f"{self.__age} years"

    def __set_age(self, age):
        if age < 0 and age > 25:
            age = 0
        self.__age = age

    def add_year(self):
        self.__age += 1

    # def test(self):
    #     print(self, id(self))

d1 = Dog("Zefirka", "wss",  "color", 3)
d2 = Dog("Max", "shepherd", "mixed", 2)

print(Dog.__dict__)
print(d1.__dict__)
print(d2.__dict__)

# d1.__set_age(10)
print(d1.get_age())

d1.add_year()
print(d1.get_age())

# d1.set_breed("dog")
# print(d1.get_breed())

d1.breed = "dog"
print(d1.breed)