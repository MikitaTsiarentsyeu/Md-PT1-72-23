global_val = "global value"

def test_func():
    local_val = "local value"

    # global global_val
    # global_val = "new valaue from test_func"
    print(global_val)

    def inner_func():
        inner_local_val = "inner local value"

        nonlocal local_val
        local_val = "inner local value from nonlocal"

        global global_val
        global_val = "new value from inner_func"
        print(global_val)

    inner_func()
    print(local_val)

test_func()
print(global_val)