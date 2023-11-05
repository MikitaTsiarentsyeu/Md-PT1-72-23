import os

# path = "level 1\level 2\level 3"

print(os.name)

# sep = '\\' if os.name == 'nt' else '/'
levels = ["lvl 1", "lvl 2", "lvl 3"]
print(os.sep.join(levels), os.sep)

path = os.path.join("lvl 1", "lvl 2", "lvl 3")
print(path)

print(os.getcwd())

# os.makedirs(path)
# os.chdir(path)
# open("test.txt", 'w')

# print(os.listdir())
for i in os.walk(os.getcwd()):
    print(i)

# os.chdir(path)
# os.remove('test.txt')

# os.removedirs(path)
