pb = {9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}


nmbr = int(input("Enter a phone number:\n"))

# if nmbr in pb:
#     print(pb[nmbr])
# else:
#     print("can't find anything")

res = pb.get(nmbr, "can't find anything")
print(res)

res = f"{res[0][1]} {res[0][0]} from {res[1][0]}, {res[1][1]}" if not isinstance(res, str) else res
print(res)