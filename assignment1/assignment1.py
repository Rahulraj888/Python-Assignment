# assignment 1 - Rahul Reddaveni (C0930162)

"""
function age_calculator() is starting point of the logic. Firstly current_age is taken from the user and
subtracted from target_age this gives number of remaining years.
function calculate_remaining_days_weeks_months(current_age) holds logic for calculating remaining
days/weeks/months.
multiplying remaining age with number of days/weeks/year gives remaining day/weeks/years
"""


def age_calculator():
    try:
        current_age = int(input("What is your current age? "))
        remaining_life = calculate_remaining_days_weeks_months(current_age)
        print(f"You have {remaining_life[0]} days , {remaining_life[1]} weeks and {remaining_life[2]} months left")
    except ValueError:
        # for handling invalid input(for instance string entered by user)
        print("Exception occurred: Please Enter Integer")


def calculate_remaining_days_weeks_months(current_age):
    target_age = 90  # declaring a variable for storing target age
    no_of_months_in_year = 12
    no_of_days_in_year = 365
    no_of_weeks_in_year = 52
    remaining_age = target_age - current_age  # calculating remaining age
    # multiplying remaining age with number of days/weeks/year gives remaining day/weeks/years
    remaining_months = remaining_age * no_of_months_in_year
    remaining_days = remaining_age * no_of_days_in_year
    remaining_weeks = remaining_age * no_of_weeks_in_year
    return remaining_days, remaining_weeks, remaining_months


if __name__ == '__main__':
    age_calculator()



