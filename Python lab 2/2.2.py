prod = input()
day = input()
kg = float(input())
if day in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"):
    if prod == "banana":
        print(f"{kg * 2.50:.2f}")
    elif prod == "apple":
        print(f"{kg * 1.20:.2f}")
    elif prod == "orange":
        print(f"{kg * 0.85:.2f}")
    elif prod == "grapefruit":
        print(f"{kg * 1.45:.2f}")
    elif prod == "kiwi":
        print(f"{kg * 2.70:.2f}")
    elif prod == "pineapple":
        print(f"{kg * 5.50:.2f}")
    elif prod == "grapes":
        print(f"{kg * 3.85:.2f}")
elif day in ("Saturday", "Sunday"):
    if prod == "banana":
        print(f"{kg * 2.70:.2f}")
    elif prod == "apple":
        print(f"{kg * 1.25:.2f}")
    elif prod == "orange":
        print(f"{kg * 0.90:.2f}")
    elif prod == "grapefruit":
        print(f"{kg * 1.60:.2f}")
    elif prod == "kiwi":
        print(f"{kg * 3.00:.2f}")
    elif prod == "pineapple":
        print(f"{kg * 5.60:.2f}")
    elif prod == "grapes":
        print(f"{kg * 4.20:.2f}")
else:
    print("Error")
