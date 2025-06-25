# Programming exercise:
# Repeat password

user_password = input("Password: ")

while True:
    check_password = input("Repeat password: ")
    if user_password == check_password:
        break
    print("They do not match!")

print("User account created!")
