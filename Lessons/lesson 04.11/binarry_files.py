import time

chunk_size = 100000000
count = 0

start = time.time()
with open('test.pdf', 'rb') as init_f:
    with open('test_copy.pdf', 'wb') as res_f:
        chunk = True
        while chunk:
            chunk = init_f.read(chunk_size)
            res_f.write(chunk)
            count += 1
            if chunk:
                print(count)
print(time.time()-start)