import math
from datetime import datetime

def main():
    gender = input("Please enter your gender(M or F): ")
    birthdate = input("Please enter your birthdate(YYYY-DD-MM): ")
    pounds = float(input("Please enter yur weight in U.S pounds: "))
    inches = float(input("Please enter your height in U.S. inches: "))

    weight = kg_from_lb(pounds)
    height = cm_from_in(inches)
    
    age = compute_age(birthdate)
    bmi_ = body_mass_index(weight, height)
    bmr_ = basal_metabolic_rate(gender, weight, height, age)
    
    print(f"Age (years): {age}\nWeight (kg): {weight:.2f}\nHeight (cm): {height:.1f}\nBody mass index: {bmi_:.1f}\nBasal metabolic rate (kcal/day): {bmr_:.0f}")

    pass 

def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()
    years = today.year - birthdate.year

    # Compute the difference between today and the
    # person's birthdate in years.

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years

def kg_from_lb(pounds):
    
    kilo = pounds / 2.2046

    return kilo

def cm_from_in(inches): 
    
    cm = 2.54 * inches

    return cm


def body_mass_index(weight, height):
    
    bmi = 10000 * weight / (height ** 2)
    
    return bmi

def basal_metabolic_rate(gender, weight, height, age):
    if gender.lower() == "f":
        
        bmr = 447.593 + 9.247 * (weight) + 3.098 * (height) - 4.330 * (age)
    elif gender.lower() == "m":
        bmr = 88.362 + 13.397 * (weight) + 4.799 * (height) - 5.677 * (age)
    return bmr

main()