# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    gender = input("Please enter your gender (M or F):")
    birthdate = input("Enter your birthdate (YYYY-MM-DD):")
    weight = float(input("Enter your weight in U.S. pounds: "))
    height = float(input("Enter your height in U.S. inches: "))

    age = compute_age(birthdate)
    kilograms = kg_from_lb(weight)
    centimeters = cm_from_in(height)
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.
    BMI = body_mass_index(kilograms, centimeters)
    BMR = basal_metabolic_rate(gender, kilograms, centimeters, age)

    print(f"Age (years): {age}")
    print(f"Weight (kg): {kilograms:.2f}")
    print(f"Height (cm): {centimeters:.1f}")
    print(f"Body mass index: {BMI:.1f}")
    print(f"Basal metabolic rate (kcal/day): {BMR:.0f}")
    pass


def compute_age(birth_str):
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):
    kilograms = pounds * 0.45359237
    return kilograms


def cm_from_in(inches):
    centimeters = inches * 2.54
    return centimeters


def body_mass_index(weight, height):

    BMI = (weight / (height ** 2)) * 10000

    return BMI


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """

    if gender.upper() == "M":
        BMR = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
    elif gender.upper() == "F":
        BMR = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    else:
        print("Type Gender again")
    return BMR


# Call the main function so that
# this program will start executing.

main()
