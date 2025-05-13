# Part 1 - Conditional statements
# Programming exercise:
# Solving a quadratic equation (Fórmula de Bhaskara)

from math import sqrt

value_a = float(input("Insira o valor de a: "))
value_b = float(input("Insira o valor de b: "))
value_c = float(input("Insira o valor de c: "))

discriminante = value_b**2 - 4*value_a*value_c 

raiz1 = (-value_b + sqrt(discriminante))/(2*value_a)
raiz2 = (-value_b - sqrt(discriminante))/(2*value_a)

print(f"The roots are {raiz1} and {raiz2}")

