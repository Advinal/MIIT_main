t = int(input())
day = input()
if 10 <= t <= 18:
    if day == "Morning":
        Outfit = "Sweatshit"
        Shoes = "Sneakers"
        print("It`s", t ,"degrees, get your", Outfit, "and", Shoes )
    elif day == "Afternoon":
        Outfit = "Shirt"
        Shoes = "Moccasins"
        print("It`s", t ,"degrees, get your", Outfit, "and", Shoes )
    elif day == "Evening":
        Outfit = "Shirt"
        Shoes = "Moccasins"
        print("It`s", t ,"degrees, get your", Outfit, "and", Shoes )
elif 18 <= t <= 24:
    if day == "Morning":
        Outfit = "Shirt"
        Shoes = "Moccasins"
        print("It`s", t ,"degrees, get your", Outfit, "and", Shoes )
    elif day == "Afternoon":
        Outfit = "T-Shirt"
        Shoes = "Sandals"
        print("It`s", t ,"degrees, get your", Outfit, "and", Shoes )
    elif day == "Evening":
        Outfit = "Shirt"
        Shoes = "Moccasins"
        print("It`s", t ,"degrees, get your", Outfit, "and", Shoes )
elif t >= 25:
    if day == "Morning":
        Outfit = "T-Shirt"
        Shoes = "Sandals"
        print("It`s", t ,"degrees, get your", Outfit, "and", Shoes )
    elif day == "Afternoon":
        Outfit = "Swim Suit"
        Shoes = "Barefoot"
        print("It`s", t ,"degrees, get your", Outfit, "and", Shoes )
    elif day == "Evening":
        Outfit = "Shirt"
        Shoes = "Moccasins"
        print("It`s", t ,"degrees, get your", Outfit, "and", Shoes )
else:
    print("Error")
