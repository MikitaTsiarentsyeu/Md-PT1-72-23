line = input('Text any string with upper case and lower case in it, please:' )
def count_upper_lower_case(text):
    '''This def takes a string and counts the upper and lower case'''
    upper_case = 0
    lower_case = 0
    for i in range(len(text)):
        if text[i] == text[i].upper() and text[i].isalpha() == True:
            upper_case += 1
        elif text[i] == text[i].lower() and text[i].isalpha() == True:
            lower_case += 1
    print(f'Your line consists of {upper_case} upper case and {lower_case} lower case')

count_upper_lower_case(line)