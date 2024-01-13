nls = '\n'

def ui():
    try:
        x = input(f"Enter some number:{nls}")
        x = float(x)
        y = input(f"Enter some other number:{nls}")
        y = float(y)
    except (ValueError, TypeError):
        print("please use only digits")

    try:
        res = x/y
    except ZeroDivisionError:
        print("cannot divide by zero")

    return res
    
    
    # except:
    #     print("an error occured")    
def result():
    try:
        res = ui()
    except NameError:
        print("some name error occured")
        res = None
    if res:
        print(f"The result is {res}")

result()

# with open("test.tx") as f:
#     f.read()

# f = open("test.tx")
# f.read()
# f.close()

# try:
#     x = 5/0
#     print(x)
# except:
#     print("an error occured")

# print("The end")


class CustomError(Exception):
    pass

try:
    try:
        try:
            try:
                raise CustomError("Some error to catch later")
            except KeyError:
                print("Oooops")
            finally:
                pass
        except ValueError:
            print("Oooops")
    except CustomError as e:
        print(e)
except ZeroDivisionError:
    print("Oooops")

# raise TypeError("Some very important error")

# try:    
#     f = open("test.txt", 'w')
#     f.read()
# except:
#     print("something went wrong")
# finally:
#     f.close()


# with open("test.txt", 'w') as f:
#     pass

try:
    f = None
    f = open("test.txt", 'r')
except:
    print("file not found")
    print(f)
finally:
    if f:
        f.close()