class Simpleton:

    test_attr = "test"
    new_attr = "new value"


def test():

    test = "test"

print(type(Simpleton), type(Simpleton()))

print(Simpleton.test_attr)

print(Simpleton.__dict__)

# namespace

# 3+5
print(int(3).__add__(5))
# "test"+" str"
print("test".__add__(" str"))

# print+print

print(dir(int))
print(dir(str))

# print(Simpleton.test_attr)
print(Simpleton.__getattribute__(Simpleton, "test_attr"))

# Simpleton.var
# print(Simpleton.__getattribute__(Simpleton, "var"))
# getattr(Simpleton, "var")


# Simpleton.__setattr__(Simpleton, "test_attr", "new value from setattr")
setattr(Simpleton,  "test_attr", "new value from setattr")
print(Simpleton.test_attr)
# Simpleton.test_attr = "test"

d = {"test_atr": "test"}
d["test_attr"] = "new value from setattr"
d["new_key"] = "new value"

# setattr(Simpleton, "new_key", "new_value")
# print(Simpleton.__dict__)
# print(getattr(Simpleton, "new_key"))


# MONKEY PATCHING
Simpleton.new_key = "new_value"
print(Simpleton.new_key)

s = Simpleton()
print(s.__dict__)
print(s.new_attr, s.new_key)

s.new_attr = "instance value"
print(s.__dict__)
print(s.new_attr, s.new_key)

# MONKEY PATCHING
s.new_instance_key = "new_value"
print(s.new_instance_key)
print(Simpleton.__dict__)
print(s.__dict__)

s2 = Simpleton()
s2.new_attr = "s2 instance value"

print(Simpleton.__dict__)
print(s.__dict__)
print(s2.__dict__)

