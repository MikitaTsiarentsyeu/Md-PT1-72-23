limit = 100

class LimitOver(Exception): pass

while True:
    x = input(f"Enter the integer value which is lower than {limit}\n")
    try:
        validation_error = True
        x = int(x)
        if x >= limit:
            raise LimitOver("entered value is higher than the limit")
    except ValueError:
        print("entered value is not an integer number")
        continue
    except LimitOver as e:
        print(e)
        continue
    except:
        print("something went wrong")
        continue
    else:
        validation_error = False
        break
    finally:
        if validation_error:
            print("please try again")