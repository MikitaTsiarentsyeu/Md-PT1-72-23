def rec_reverse(in_str, left=0, right=None, in_list=None):  # reverse using list
    if in_list is None:
        in_list = list(in_str)
        right = len(in_str) - 1
    if left >= right:
        return ''.join(in_list)
    else:
        in_list[left], in_list[right] = in_list[right], in_list[left]

        return rec_reverse(in_str, left + 1, right - 1, in_list)


def rec_rev(in_str, out_str='', i=0):  # reverse using concat
    if i == len(in_str):
        return out_str
    else:
        return rec_rev(in_str, in_str[i] + out_str, i + 1)
