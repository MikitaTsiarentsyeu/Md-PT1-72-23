class OmniParent:

    def test(self):
        print(f"test from {OmniParent.__name__}")

class Parent1(OmniParent):

    def test(self):
        print(f"test from {Parent1.__name__}")
        super().test()

class Parent2(OmniParent):

    def test(self):
        print(f"test from {Parent2.__name__}")
        super().test()

class Child(Parent2, Parent1):
    
    def test(self):
        print(Child.mro())
        print(getattr(Child, "test"))
        super().test()

c = Child()
c.test()

instances = []

for i in OmniParent, Parent1, Parent2, Child:
    instance = i()
    instances.append(instance)

print(instances)


