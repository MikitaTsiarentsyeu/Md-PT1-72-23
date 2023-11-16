def level1():
    print("start of the level 1")
    level2()
    print("end of the level 1")

def level2():
    print("\tstart of the level 2")
    level3()
    print("\tend of the level 2")

def level3():
    print("\t\tstart of the level 3")
    level4()
    print("\t\tend of the level 3")

def level4():
    print("\t\t\tstart of the level 4")
    # level1()
    print("\t\t\tend of the level 4")

# level1()

def level(n, i=0):
    if i == n:
        return
    print('\t'*i+f" start of the level {i+1}")
    # if n > 0:
    #     level(n-1)
    level(n, i+1)
    print('\t'*i+f" end of the level {i+1}")

level(5)

print("the end")