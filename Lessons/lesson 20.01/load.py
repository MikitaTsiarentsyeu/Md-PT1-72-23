# import time_it_mod as timeit
import time_it_oop as timeit

start_time = timeit.start()
for i in range(100000):
    i+=1
res = timeit.finish()
print(res)