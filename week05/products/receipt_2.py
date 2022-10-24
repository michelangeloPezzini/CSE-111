import csv
from datetime import datetime
'''
-Print the store name at the top of the receipt.
-Print the list of ordered items.
-Sum and print the number of ordered items.
-Sum and print the subtotal due.
-Compute and print the sales tax amount. Use 6% as the sales tax rate.
-Compute and print the total amount due.
-Print a thank you message.
-Get the current date and time from your computer's operating system and print the current date and time.
Include a try block and except blocks to handle FileNotFoundError, PermissionError, and KeyError.
'''
def main():
    store_name = "Cokies Dream"
    product_key = 0
    subtotal = 0.0
    total = 0.0
    sale_tax = 0
    number_items = 0
    sale_tax = subtotal * 6/100
    total = subtotal + sale_tax
    current_date_and_time = datetime.now()

    try:
        products_list = read_dict("D:\Cursos\CSE-111\week05\products\products.csv", product_key)   
        with open("week05\products\#request.csv", "rt") as request_client:
            reader = csv.reader(request_client)
            next(reader)    
            print("=-" * 10)
            print(store_name)
            print("=-" * 10)
            print(f"Ordered items: \n")
            for i in reader:
                product_ID = i[0]
                quantity=i[1]
                new_require = products_list[product_ID]
                cost = new_require[2]
                subtotal = subtotal + (float(cost) * int(quantity))
                product = new_require[1]
                number_items = number_items + int(quantity)
                print(f"{product} {cost} {quantity}")
            

    except FileNotFoundError as file__not_found:
        print(file__not_found)
    except PermissionError as permission_err:
        print(permission_err)
    except KeyError as key_err:
        print(key_err)  
      
    finally:
        print(f"\nNumber of items: {number_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sale tax: {sale_tax:.2f}")
        print(f"Total: {total:.2f}")
        print("Thank for shopping with us!")
        print(f"{current_date_and_time:%A %I:%M %p}")
        
        # at this point, we  can test if today is a discount day or not, 
        # if it is multiply by the discount rate to reduce the grand total
        
        

def read_dict(filename, key_column_index):
    key_products = {}
    with open(filename, "rt") as products_list:
        reader = csv.reader(products_list)
        next(reader)
        for i in reader:
            key = i[key_column_index]
            key_products[key] = i
    return key_products


if __name__ == "__main__":
    main()