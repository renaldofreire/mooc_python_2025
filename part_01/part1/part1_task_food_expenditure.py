# TASK Food expenditure
student_cafe_week = int(input("How many times a week do you eat at the student cafeteria? "))
student_cafe_price = float(input("The price of a typical student lunch? "))
groceries_week = float(input("How much money do you spend on groceries in a week? "))

student_food = student_cafe_week * student_cafe_price
food_average = (student_food + groceries_week) / 7
food_week = student_food + groceries_week

print(f"Average food expenditure:\n Daily: {food_average} euros\n Weekly: {food_week} euros")


