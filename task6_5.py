# n is a digit
# N is a number (position) of digit in the sequence
# !numbering of numbers in the sequence starts from 1!
#0, 1, 1, 2, 3, 5, 8, 13, 21
#for exemple: n = 6 => N = 5

def Fibonacci_seq(N):
    if N == 1:
        return 0
    if N == 2:
        return 1
    elif N == 3:
        return 1
    elif N >= 4:
        return (Fibonacci_seq(N - 1) + Fibonacci_seq(N - 2))
    else:
        return False
N = int(input("Enter: N ="))
#a = 'the first number of digit N = 1! Enter a number > 0'
#b = '1 in case of number N=2 or N=3'

print('n =',Fibonacci_seq(N))