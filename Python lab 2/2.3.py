zal = input()
x = float(input())
y = float(input())
if x or y < 0:
    print("Error")
elif zal == "Premiere":
    print(f"{x * y * 12:.2f} $")
elif zal == "Normal":
    print(f"{x * y * 7.50:.2f} $")
elif zal == "Discount":
    print(f"{x * y * 5:.2f} $")
else:
    print("Error")