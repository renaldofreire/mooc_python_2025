# Exercício 2: O Conversor de Tempo
# Escreva um programa que pede ao usuário uma quantidade total de segundos (por exemplo, 150). O programa deve calcular e imprimir quantos minutos e segundos isso representa.

segundos = int(input("Insira uma quantidade de segundos: "))

divisao_inteira = segundos // 60
divisao_sobra = segundos % 60

print(f"{segundos} equivalem a {divisao_inteira} minutos e {divisao_sobra} segundos.")

