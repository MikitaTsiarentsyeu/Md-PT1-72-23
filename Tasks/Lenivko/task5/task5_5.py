li = [2, 3, 8, 9]

def get_ranges(li):
    if len(li) == 0:
        return "Oops! It's empty list"
    else:
        start_value = li[0]
        end_value = li[0]
        result_li = []
        for num in li[1:]:
            if num == end_value + 1:
                end_value = num
            else:
                if start_value == end_value:
                    result_li.append(str(end_value))
                else:
                    result_li.append(f"{start_value}-{end_value}")
                start_value = end_value = num
    # for last number
        if start_value == end_value:
            result_li.append(str(end_value))
        else:
            result_li.append(f'{start_value}-{end_value}')
        print(", ".join(result_li))
get_ranges(li)