line = "line 1.\n"

# with open('test.txt', 'r') as init_f:
#     with open('test_res.txt', 'w') as res_f:
#         for line in init_f:
#             res_f.write(line.replace('.', '!'))

with open('test.txt', 'r') as init_f:
    content = init_f.read()

with open('test.txt', 'w') as res_f:
    for line in content.split('\n'):
        res_f.write(line.replace('.', '!')+'\n')