from datetime import date


def get_dob():
    year = int(input('Enter year of birth:'))
    month = int(input('Enter month of birth:'))
    day = int(input('Enter day of birth:'))

    return date(year, month, day)

def get_age(dob):
    today = date.today()
    print(today , dob)
    months_and_days = (today.month, today.day) < (dob.month, dob.day)
    age = today.year - dob.year - months_and_days
    return age

def main():
    date_of_birth = get_dob()
    today = date(2019, 9, 4)

    if(date_of_birth > today):
        print("Your date of birth is invalid...please enter a valid date.")
    else:
        age = get_age(date_of_birth)
        print(f"You are {age} years old.")

if __name__ == '__main__':
    main()
