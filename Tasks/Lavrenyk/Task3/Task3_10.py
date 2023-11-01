from re import findall


def is_prime(n: int) -> bool:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def largest(nums: list):
    large = 0
    for i in nums:
        if (i > 1 and
                is_prime(i)
                and i > large):
            large = i

    if large == 0:
        return 'No prime numbers in list'
    return large


while True:
    user_input = input('Enter the numbers separated by a space: ')

    numbers = list(map(int, findall(r'-?\d+', user_input)))
    if numbers:
        break

print(largest(numbers))
