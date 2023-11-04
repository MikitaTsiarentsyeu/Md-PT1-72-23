# f = open('test.txt')
# print(f.read())
# f.close()

# path = r'C:\Drive D\Projects\IT Academy\Python\Md-PT1-72-23\repo\Md-PT1-72-23\Lessons\lesson 04.11\test.txt'
# print(path)
# with open(path) as f:
#     print(f.read())

# with open('test.txt', 'r') as f:
#     print(f.read())
    # f.write(" test")

with open('test.txt', 'w') as f:
    f.write("test line\n")
    f.writelines(['line 1\n', 'line 2\n', 'line 3\n'])

with open('test.txt', 'r') as f:
    for line in f:
        print(repr(line))
    # for line in f.readlines():
    #     print(repr(line))
    # print(repr(f.read()))
    # f.seek(10)
    # print(repr(f.read()))

    # print(repr(f.read(10)))
    # print(repr(f.read(10)))
    # print(repr(f.read(10)))
    # print(repr(f.read(10)))
    # print(repr(f.read(10)))
    # print(repr(f.read(10)))

with open('test.txt', 'a') as f:
    f.write("new line from 'append'\n")
    f.seek(0)
    f.write("new first line\n")

with open('test.txt', 'a+') as f:
    f.write("new line from 'append+'\n")
    f.seek(0)
    # print(repr(f.read()))
    f.write("new first line\n")

with open('test.txt', 'r+') as f:
    # for line in f:
    #     print(repr(line))
    f.write("new line from 'read+'\n")

with open('test.txt', 'w+') as f:
    f.write("new line from 'write+'\n")
    f.seek(0)
    # print(repr(f.read()))
    f.write("second line???")