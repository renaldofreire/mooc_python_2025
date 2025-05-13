a = 5
b = 10

igual = a == b # False
diferente = a != b # True
maior = a > b # False
menor = a < b # True
maior_igual = a >= b # False
menor_igual = a <= b # True

# Condicional
idade = int(input("Qual sua idade?")) 
possui_autorizacao = False

if idade >= 18 or possui_autorizacao:
    print("Entrada permitida.")
else:
    print("Entrega não permitida!")

# Operadores Lógicos
# AND, OR e NOT

# AND lógico - verdadeiro se ambas as condições forem verdadeiras
x = True and False      # False
x = True and True       # True

# OR lógico - verdadeiro se pelo menos uma condição for verdadeira
y = True or False       # True
y = False or False      # False

# NOT lógico - inverte o valor
z = not True            # False
z = not False           # True

