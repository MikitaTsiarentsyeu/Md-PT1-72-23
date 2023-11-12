test = "global value"
global_l = []

def test_func():
    test = "local value"
    global_l.append(test)
    print(test)

    def inner_func():
        test = "another local value"
        print(test)

    inner_func()

    test = "another local value"
    print(test)

    return test

test_func()
print(test, global_l)