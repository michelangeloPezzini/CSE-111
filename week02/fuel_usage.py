def main():
    start_miles = int(input("Enter the starting odometer value in miles: "))
    end_miles = int(input("Enter the ending odometer value in miles: "))
    amount_gallons = float(input("Enter the amount of fuel used (gallons): "))

    mpg = miles_per_gallon(start_miles, end_miles, amount_gallons)
    lp100k = lp100k_from_mpg(mpg)

    print(f"{mpg:.2f} miles per gallon")
    print(f"{lp100k:.2f} liters per 100 kilometers")


def miles_per_gallon(start_miles, end_miles, amount_gallons):
    fuel_efficiency = (end_miles - start_miles) / amount_gallons
    return fuel_efficiency


def lp100k_from_mpg(mpg):
    lp100k = 235.215 / mpg
    return lp100k


main()
