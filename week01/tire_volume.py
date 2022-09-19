import math
from datetime import datetime
import string

print("This program can read from the keyboard the three numbers for a tire and computes and outputs the volume of space inside that tire.")

width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the width of the tire in mm (ex 60): "))
diameter = int(input("Enter the width of the tire in mm (ex 15): "))

divider = 10000000000
v = math.pi * (width ** 2) * aspect_ratio * \
    (width * aspect_ratio + 2540 * diameter)
result = v / divider

# By datetime
current_date = datetime.now()
days_of_week = current_date
# print(days_of_week)

print(f"The approximate volume is \033[42m{result:.2f}\033[m liters")

seller = input("Would you like to buy a tire with these dimensions? YES/NO ")
new_seller = seller.upper()
if new_seller == "YES":
    name = input("Whats your name? ")
    phone_number = int(input("What is your phone number? "))
    print("Thanks for shopping with us, bye")
else:
    print("I hope to see you soon, bye!")

with open("CSE 111\week01\list_volumes.txt", "at") as file:
    print(f"{current_date:%Y-%m-%d}", file=file, end=" ")
    print(f"{width} | {aspect_ratio} | {diameter} | {result:.2f}",
          file=file, end=" ")
    print(f"{name} | {phone_number}", file=file)
