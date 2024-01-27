class Animal:

    def say_something(self):
        print(f"test {self.__class__.__name__}")

    def eat_something(self):
        pass

    def sleep(): pass

class Dog:

    def say_something(self):
        print(f"test bark")

class Cat:

    def say_something(self):
        print(f"test meow")

class Human:

    def say_something(self):
        print(f"test hm")

animals = [Animal(), Dog(), Cat(), Human()]

for a in animals:
    a.say_something()