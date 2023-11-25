def mirror_string(string, n):
    # reversing if line relative to its end
    mirr_str = string[n:]
    # concatenate list of strings
    reversed_mirr_str = ''.join(reversed(mirr_str))
    mirrored_string = reversed_mirr_str
    return mirrored_string

print(mirror_string('yellow, green, red', 0))