b = int(input())
s = input()
h = int(input())
if s == "Spring":
    x = 3000
elif s == "Summer":
    x = 4200
elif s == "Autumn":
    x = 4200 
elif s == "Winter":
    x = 2600
else:
    print("Error")
if not (1 <= b <= 8000) or not(4 <= h <= 18):
    print("Error") 
if h <= 6:
    x *= 0.9
if 7 <= h <= 11:
    x *= 0.85
if h >= 12:
    x *= 0.75
if h % 2 == 0 and not s == "Autumn":
    x *= 0.95
if x > b:
    print(f"Not enough money! You need {x - b:.2f} rubles")
elif x < b:
    print(f"Yes! You have {b - x:.2f} rubles left")