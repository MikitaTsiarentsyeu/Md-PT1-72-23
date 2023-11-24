sentence = input()

def f(sentence):
    if not sentence:
        return 0
    return (1 if sentence[0] == 'l' else 0) + f(sentence[1:])
print(f(sentence))
