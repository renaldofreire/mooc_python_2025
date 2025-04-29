# Programming exercise:
# Orwell
# get_num = int(input("Insira um número: "))

# if get_num == 1984:
#     print("Orwell")

# Programming exercise:
# Absolute value
# num = int(input("Please type in a number: "))
#
# if num < 0:
#     print(f"The absolute value of this number is {num * -1}")

# Programming exercise:
# Soup or no soup
# name = input("Please tell me your name:")
# portion_price = 5.90
#
# if name != "Jerry":
#     num_portions = float(input("How many portions of soup?"))
#     print(f"The total cost is {num_portions * portion_price}")
# print("Next please!")

# Programming exercise:
# Order of magnitude
# number = int(input("Please type in a number: "))
#
# if number <= 999:
#     print("This number is smaller than 1000")
#
# if number <= 99:
#     print("This number is smaller than 100")
#
# if number <= 9:
#     print("This number is smaller than 10")
#
# print("Thank you!")

# Programming exercise:
# Calculator
# num1 = int(input("Number 1: "))
# num2 = int(input("Number 2: "))
# operation = input("Operation: ")
#
# if operation == "add":
#     print(f"{num1} + {num2} = {num1+num2}")
#
# if operation == "multiply":
#     print(f"{num1} * {num2} = {num1*num2}")
#
# if operation == "subtract":
#     print(f"{num1} - {num2} = {num1-num2}")
#
# print("")
#

# Programming exercise:
# Temperatures
# fahrenheite_temp = float(input("Please type in a temperature (F)"))
# celcius_calc = 0.555555555556 * (fahrenheite_temp - 32.0)
#
# print(f"{fahrenheite_temp} degrees Fahrenheit equals {celcius_calc} degrees Celsius")
#

# Programming exercise:
# Daily wages
# hourly_wage = float(input("Hourly wage: "))
# hours_worked = float(input("Hours worked : "))
# day_week = input("Day of the week: ")
#
# daily_wages = hourly_wage * hours_worked
#
# if day_week == "Sunday":
#     daily_wages *= 2
# print(f"Daily wages: {daily_wages} euros")
#

# Programming exercise:
# Loyalty bonus

# points = int(input("How many points are on your card? "))
# if points < 100:
#     percent = 1.10
#     print("Your bonus is 10 %")
#
# if points >= 100:
#     percent = 1.15
#     print("Your bonus is 15 %")
#
# points *= percent
# print("You now have", points, "points")

# Programming exercise:
# What to wear tomorrow

temp = int(input("Temperature: "))
rain = input("Will it rain (yes/no): ")

temp_one = "Wear jeans and a T-shirt"
temp_two = "I recommend a jumper as well"
temp_three = "Take a jacket with you"
temp_four = "Make it a warm coat, actually\n I think gloves are in order"
temp_rain = "Don't forget your umbrella!"

if temp < 5:
    temp_four

if temp > 20:
    the_temp = "Wear jeans and a T-shirt"

if temp > 10:
    the_temp = "I recommend a jumper as well"

if temp < 10:
    the_temp = "Take a jacket with you"


print(the_temp)

if rain == "yes":
    print("Don't forget your umbrella!")





