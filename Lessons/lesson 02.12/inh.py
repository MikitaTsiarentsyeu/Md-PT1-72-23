class Animal:

    def __init__(self, name):
        self.name = name

    def sleep(self):
        print("I'm sleeping...")

class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)
        # Animal.__init__(self, name)
        self.breed = breed

    def hunt(self):
        print("I'm hunting!")

class Cat(Animal): pass

# a = Animal("some animal")
# d = Dog("Good boy", "pointer")

# print(d.name)
# d.sleep()


class FlyingAnimal(Animal):

    def move(self):
        print("I'm flying")
        
class RunningAnimal(Animal):

    def move(self):
        print("I'm running")

class SwimmingAnimal(Animal):

    def move(self):
        print("I'm swimming")


class Duck(SwimmingAnimal, FlyingAnimal, RunningAnimal):

    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        FlyingAnimal.move(self)
        # super().move()

    def swim(self):
        SwimmingAnimal.move(self)
        # super().move()

    def run(self):
        RunningAnimal.move(self)
        # super().move()

d = Duck("Donald")
print(d.name)
d.fly()
d.swim()
d.run()


class C:

    def method(self):
        print(C)

class A(C):

    def method(self):
        print(A)

class B(C):

    def method(self):
        print(B)

class D(A, B):

    def method(self):
        print(D)

    
print(D.__mro__)

print(dir(object))

class MyClass:

    def __str__(self) -> str:
        return "MyClass object"

mc = MyClass()
print(mc)