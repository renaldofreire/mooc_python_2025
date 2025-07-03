# Exercício 1: O Próximo Múltiplo de 7 e 11
# Escreva um programa que peça um número ao usuário. O programa deve então encontrar e imprimir o primeiro número maior que o número dado que seja divisível por 7 e 11 ao mesmo tempo.
# Objetivo: treinar while

number = int(input("Insira um número: "))
multiple = number + 1

while True:
    is_multiple = (multiple % 7 == 0 and multiple % 11 == 0)

    if is_multiple:
        print(f"O próximo múltiplo de 7 e 11 que vem após o {number} é o número {multiple}.")
        break

    multiple += 1

