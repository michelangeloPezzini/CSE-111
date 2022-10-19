import csv

def main():
  product_key = 0
  products_list = read_dict("D:\Cursos\CSE-111\week05\products\products.csv", product_key)

  with open("week05\products\#request.csv", "rt") as request_client:
    reader = csv.reader(request_client)
    next(reader)    

    for i in reader:
      require_client = i[0]
      new_require = products_list[require_client]
      print(new_require)

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