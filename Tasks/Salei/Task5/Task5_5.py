# Write a function that takes an ordered list of numbers without duplicates and returns a string with ranges for those numbers, check the example below:
# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"

def get_ranges(numbers):
    ranges = []
    begin = end = numbers[0]
    
    for i in range(1, len(numbers)):
        if numbers[i] == end + 1:
            end = numbers[i]
        else:
            if begin == end:
                ranges.append(str(begin))
            else:
                ranges.append(f"{begin}-{end}")
            begin = end = numbers[i]
    
    if begin == end:
        ranges.append(str(begin))
    else:
        ranges.append(f"{begin}-{end}")
    
    return ", ".join(ranges)

num = [0, 1, 2, 3, 4, 7, 8, 10, 11, 25]
print(f"{get_ranges(num)}.")