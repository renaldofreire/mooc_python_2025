# Programming exercise:
# Fix the syntax
number = int(input("Please type in a number: "))

if number > 100:
    print("The number was greater than one hundred")
    print("Now its value has decreased by one hundred")
    number -= 100
    print("Its value is now", number)

print(number, " must be my lucky number!")
print("Have a nice day!")
