# Programming exercise:
# Gift tax calculator

gift_value = int(input("Value of gift: "))

if gift_value < 5000:
    print("No tax!")
elif gift_value >= 5000 and gift_value < 25000:
    tax_calc = (100 + (gift_value - 5000) * 0.08)
    print(f"Amount of tax: {tax_calc} euros")
elif gift_value >= 25000 and gift_value < 55000:
    tax_calc = (1700 + (gift_value - 25000) * 0.10)
    print(f"Amount of tax: {tax_calc} euros")
elif gift_value >= 55000 and gift_value < 200000:
    tax_calc = (4700 + (gift_value - 55000) * 0.12)
    print(f"Amount of tax: {tax_calc} euros")
elif gift_value >= 200000 and gift_value < 1000000:
    tax_calc = (22100 + (gift_value - 200000) * 0.15)
    print(f"Amount of tax: {tax_calc} euros")
else:
    tax_calc = (142100 + (gift_value - 1000000) * 0.17)
    print(f"Amount of tax: {tax_calc} euros")


