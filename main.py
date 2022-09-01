# The goal here is to say whether a year is a leap year or not.
# A leap year is an event according to the Gregorian calendar that occurs every 4 years,
# and adds an extra day to the normal calendar year (366 days).

year = int(input("\nWhich year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("\nThis is a Leap Year")
        else:
            print("\nThis is not a Leap year")
    else:
        print("\nThis is a Leap year")
else:
    print("\nThis is no a Leap year")