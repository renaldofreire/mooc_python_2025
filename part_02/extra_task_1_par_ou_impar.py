# Exercício 1: O Porteiro de Festa (Par ou Ímpar)
# Escreva um programa que pede um número ao usuário. Se o número for par, imprima "Pode entrar pela porta da direita.". Se for ímpar, imprima "Pode entrar pela porta da esquerda.".

numero = int(input("Insira um número: "))

if numero % 2 == 0:
    print("Entre pela porta da direita.")
else:
    print("Entre pela porta da esquerda.")

