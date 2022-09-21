import math


def main():
    weight = float(input("Enter your weight in U.S. pounds: "))
    height = float(input("Enter your height in U.S. inches: "))

    kilograms = kg_from_lb(weight)
    centimeters = cm_from_in(height)
    BMI = body_mass_index(kilograms, centimeters)
    print(f"{kilograms:.2f}")
    print(f"{centimeters:.2f}")
    print(BMI)


def kg_from_lb(pounds):
    kilograms = pounds * 0.45359237
    return kilograms


def cm_from_in(inches):
    centimeters = inches * 2.54
    return centimeters


def body_mass_index(weight, height):
    BMI = weight / (math.pow(height, 2))
    return BMI


main()
