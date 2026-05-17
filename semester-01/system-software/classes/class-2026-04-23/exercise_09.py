# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

print("-"*50)
print("Processamento de números ímpares dentro de intervalo e impressão de resultado para usuário")
print("-"*50)
print("")

print("Números ímpares:\n")

for num in range(1, 51):
    if num % 2 != 0:
        print(num, end=" ")

print("\n\nFim do programa. Obrigado por usar!\n")