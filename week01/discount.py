from datetime import datetime, date
import calendar

# By calendar
""" d = date.today()
print('Date is:', d)
x = calendar.day_name[d.weekday()]
print('Weekday name is:', x) """

# By datetime
current_date = datetime.now()
days_of_week = current_date.strftime("%A")

subtotal = float(input("Please enter the subtotal: "))


if subtotal >= 50:
    if days_of_week == "Tuesday" or days_of_week == "Wednesday":
        print(f"Subtotal: {subtotal:.2f}")
        discount = subtotal * 10/100
        total_with_discount = subtotal - discount
        print(f"Discount: {discount:.2f}")

    else:
        print(f"Subtotal: {subtotal}")
        sale_tax = subtotal * 6/100
        print(f"Sale tax: {sale_tax}")
        total = subtotal + sale_tax
        print(f"Total: {total}")
else:
    print("Without discount today")


sale_tax = total_with_discount * 6/100
print(f"Sale tax: {sale_tax}")
total = sale_tax + total_with_discount
print(f"Total: {total:.2f}")
