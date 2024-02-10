"""
main() - this function is used to get input from user.
get_quarter() - this function checks in which quarter this month will fall
"""


def main():
    try:
        month = int(input("Enter month between 1 and 12: "))
        quarter = get_quarter(month)
        print(f"Month {month} is in {quarter} quarter")
    except ValueError:
        # for handling invalid input(for instance string entered by user)
        print("Exception occurred: Please Enter Integer")
    except Exception as error:
        # for handling exception thrown incase month is entered out of range.
        print(error)


# list is created for each quarter, given month will fall into one of the quarter. If invalid input exception is thrown
def get_quarter(month):
    if month in [1, 2, 3, 4]:
        return "first"
    elif month in [5, 6, 7]:
        return "second"
    elif month in [8, 9]:
        return "third"
    elif month in [10, 11, 12]:
        return "fourth"
    else:
        raise Exception("Month must be between 1 and 12. Please Rerun the Program")


if __name__ == '__main__':
    main()
