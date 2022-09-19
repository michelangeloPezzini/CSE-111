# Type of data

a = "Mike"
b = 123
c = True
d = 5.3

print(f"{type(a), a}")
print(f"{type(b), b}")
print(f"{type(c), c}")
print(f"{type(d), d}")

# if... elif... else Statements


cost = float(input("Please enter the cost: "))

if cost < 100:
    rate = 0.10
elif cost < 250:
    rate = 0.15
elif cost < 400:
    rate = 0.18
else:
    rate = 0.20

discount = cost * rate
cost -= discount
print(f"After the discount, you will pay {cost:.2f}")
