import time

start_time = 0
measure = False

def start():
    global start_time
    global measure
    start_time = time.time()
    measure = True

def finish():
    global start_time
    global measure
    res = -1

    if measure:
        res = time.time() - start_time
        start_time = 0
        measure = False

    return res

print(__name__)
if __name__ == "__main__":
    with open("measure.txt", 'w') as f:
        pass