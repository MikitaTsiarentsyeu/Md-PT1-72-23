import time

class __Time_it:

    def __init__(self) -> None:
        self.__set_neutral()

    def __set_neutral(self):
        self.__start_time = 0
        self.__finish_time = 0
        self.__is_measure = False

    def start(self):
        self.__start_time = time.time()
        self.__is_measure = True

    def finish(self):
        self.__finish_time = time.time()
        res = -1

        if self.__is_measure:
            res = self.__finish_time - self.__start_time

        self.__set_neutral()

        return res

__timer = __Time_it()

def start():
    __timer.start()

def finish():
    return __timer.finish()