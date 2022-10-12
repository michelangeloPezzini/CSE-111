import csv

company_name = 0
num_employees = 3
num_patients = 4

def main():
  with open("D:\Cursos\CSE-111\week05\dentists_exemple\dentists.csv", "rt") as dentists_file:
    reader = csv.reader(dentists_file)
    next(reader)
    running_max = 0
    most_office = None

    for row_list in reader:
      company = row_list[company_name]
      employees = int(row_list[num_employees])
      patients = int(row_list[num_patients])

      patients_per_emp = patients / employees

      if patients_per_emp > 0:
        running_max = patients_per_emp
        most_office = company

    print(f"{most_office} has {running_max:.1f}"
            " patients per employee")
    
if __name__ == "__main__":
   main()