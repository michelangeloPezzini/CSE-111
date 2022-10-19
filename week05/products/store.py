import csv

def main():
    product_key = 0
    products_list = read_dict("products.csv", product_key)
    total=0.0
    with open("request.csv", "rt") as request_client:
        reader = csv.reader(request_client)
        next(reader)    

        for i in reader:
            product_ID = i[0]
            quantity=i[1]
            new_require = products_list[product_ID]
            cost=new_require[2]
            product   = new_require[1]
            print(f'{product} {cost} {quantity}') 
            # you are almost there, you  just need to print out your receipt
            # show the product description along with the total price
            # for each item. when this is all working, and a receipt header
            # with your store name and anything else you want to display to the customer.
            #
            # subtotal = cost*quantity 
            # display the product, quantity, and subtotal
            # 
            # keep a running total here of that sub_total, call that total
            # total += subtotal
            #
            # once we are done with this block of code, the for loop 
            # exits when no more requested items are found. Carry on processing as below
        
        # at this point, we should have a total for the whole order
        # multiply that total by the tax, which gives you the grand total, display the grand total
        
        # use the date function now to see what day of the week it is
        # https://www.w3schools.com/python/python_datetime.asp
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