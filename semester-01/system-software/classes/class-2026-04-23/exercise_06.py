# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.

print("-"*50)
print("Impressão de números de 1 a 20 de duas maneiras diferentes para usuário")
print("-"*50)

print("")

for i in range(21):
    print(i)

print("")

for i in range(21):
    print(i, end=" ")