def main():
  new_list_provinces = read_provinces("D:\Cursos\CSE-111\week05\provinces.py\provinces.txt")
  new_list_provinces.pop(0)
  new_list_provinces.pop()
  
  for i in range(len(new_list_provinces)):
    if new_list_provinces[i] == "AB":
      new_list_provinces[i] = "Alberta"
  count = new_list_provinces.count("Alberta")
  print(new_list_provinces)

def read_provinces(filename):
  list_provinces = []
  with open(filename, "rt") as provinces:
    for province in provinces:
      clean_line = province.strip()
      list_provinces.append(clean_line)
  return list_provinces

if __name__ == "__main__":
    main()