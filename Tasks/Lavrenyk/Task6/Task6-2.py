def is_palindrome(in_str, left=0, right=None):
    if right is None:
        right = len(in_str) - 1

    if left >= right:
        return True
    else:
        if in_str[left] != in_str[right]:
            return False

        return is_palindrome(in_str, left + 1, right - 1)
