1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,30

ds = {
    0: "",
    1: ("час", "первого", "одна", "одной"),
    2: ("два", "второго", "две", "двух"),

    12: ("двенадцать", "двкнадцатого", "двенадцать", "двенадцати"),
    13: ("тринадцать", "тринадцати"),
    20: ("", ""),
    30: ("", "")
}

# f"{ds[20][0]} {ds[2][2]}"

i_v = input("enter your value in format hh:mm")

if len(i_v) != 5:
    print("incorrect input, please try again")
    exit()