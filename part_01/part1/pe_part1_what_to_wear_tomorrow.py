# Part1 - Conditional statements
# Programming exercise:
# What to wear tomorrow
print("What is the weather forecast for tomorrow?")
temp = int(input("Temperature: "))
it_rain = input("Will it rain (yes/no): ").lower()

get_shirt = "Wear jeans and a T-shirt"
jumper_well = "I recommend a jumper as well"
take_jacket = "Take a jacket with you"
warn_coat = "Make it a warm coat, actually\nI think gloves are in order"
umbrella = "Don't forget your umbrella!"

if temp > 20:
    answer = print(f"{get_shirt}")

if temp <= 20:
    answer = print(f"{get_shirt}\n{jumper_well}")

if temp <= 10:
    answer = print(f"{take_jacket}")

if temp <= 5:
    answer = print(f"{warn_coat}")

if it_rain == "yes":
    print(umbrella)

