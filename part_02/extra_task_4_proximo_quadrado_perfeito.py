# Exercício 2: O Próximo Quadrado Perfeito
# Escreva um programa que peça um número e encontre o primeiro quadrado perfeito estritamente maior que o número fornecido.

number = int(input("Insira um número: "))
next_number = number + 1

while True:
    square = next_number ** 0.5
    if square == int(square):
        print(f"O próximo quadrado perfeito depois de {number} é {next_number}")
        break

    next_number += 1

