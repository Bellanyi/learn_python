SHOTS = [
    "Vodka",
    "Martini",
    "Whisky",
    "Pálinka",
    "Whiskey",
]

print(SHOTS)

while print("Whiskey"):
    print(SHOTS)

s = 0

while s < len(SHOTS):
    print(SHOTS[s])
    s = s + 1


PEOPLE = [
    {
        "firstName": "James",
        "lastName": "Bond",
        "favorites": ["Vodka", "Martini"]
    },
    {
        "firstName": "Hans",
        "lastName": "Rehgenkurt",
        "favorites": ["Martini", "Martini"]
    },
    {
        "firstName": "B",
        "lastName": "BÉ",
        "favorites": ["Pálinka"]
    },
]

j = 0

while j < len(PEOPLE):
    firstName = PEOPLE[j]["firstName"]
    lastName = PEOPLE[j]["lastName"]
    favorites = PEOPLE[j]["favorites"]
    print(f"{firstName} {lastName}")

    van = False
    k = 0
    while k < len(favorites):
        l = 0
        while l < len(SHOTS):
            if favorites[k] == SHOTS[l]:
                van = True
            l = l + 1
        k = k + 1
    j = j + 1

    if van:
        print("A szokásosat?")
    else:
        print("A készlet kifogyott!")