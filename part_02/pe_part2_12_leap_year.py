# Programming exercise:
# Leap year

leap_year = int(input("Please type in a year: "))

if leap_year % 400 == 0:
    print("That year is a leap year.")
elif leap_year % 100 != 0 and leap_year % 4 == 0: # != 0 para melhorar legibilidade
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")

