import time

class __Time_it:

    # def __init__(self) -> None:
    #     self.__set_neutral()

    # __start_time = 0
    # __finish_time = 0
    # __is_measure = False

    @classmethod
    def set_neutral(parent):
        parent.__start_time = 0
        parent.__finish_time = 0
        parent.__is_measure = False

    @classmethod
    def start(parent):
        parent.__start_time = time.time()
        parent.__is_measure = True

    @classmethod
    def finish(parent):
        parent.__finish_time = time.time()
        res = -1

        if parent.__is_measure:
            res = parent.__finish_time - parent.__start_time

        parent.set_neutral()

        return res

# __timer = __Time_it()

def __init():
    __Time_it.set_neutral()

def start():
    __Time_it.start()

def finish():
    return __Time_it.finish()

__init()