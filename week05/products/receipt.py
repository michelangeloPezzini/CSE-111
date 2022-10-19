import csv

def main():
  i_number_index = 0
  i_number_name = 1
  products_list = read_dict("D:\Cursos\CSE-111\week05\products\products.csv", i_number_index)
  products_name = read_dict("D:\Cursos\CSE-111\week05\products\products.csv", i_number_name)

  list_of_name = []
  for name in products_name:
    list_of_name.append(name)


  list_of_key = []
  for key in products_list:
    list_of_key.append(key)

  print(list_of_name)
  with open("week05\products\#request.csv", "rt") as request_client:
    reader = csv.reader(request_client)
    next(reader)
    
    for i in reader:
      require = i[0]

      if require in list_of_key:
          new_require = list_of_key[i]
          print(new_require)
      else: print("Nenhum pedido igual") 
     





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