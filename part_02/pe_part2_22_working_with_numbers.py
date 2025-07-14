# Programming exercise:
# Working with numbers

print("Please type in integer numbers. Type in 0 to finish.")
count = 0
sum_number = 0
is_positive = 0
is_negative = 0

while True:
    number = int(input("Number: "))

    if number == 0:
        break
    elif number > 0:
        is_positive += 1
    elif number < 0:
        is_negative += 1

    sum_number += number
    count += 1

average_number = sum_number / count

print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {sum_number}")
print(f"The mean of the numbers is {average_number}")
print(f"Positive numbers {is_positive}")
print(f"Negative numbers {is_negative}")

