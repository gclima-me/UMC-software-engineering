# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa para imprimir:
#       1
#       1 2
#       1 2 3
#       .....
#       1 2 3 ... n
#       Para um n informado pelo usuário. Use uma função que receba um valor n inteiro, imprima até a n-ésima linha.

def imprimir_padrao(a):
    for i in range(1, a + 1):
        linha = ''
        for j in range(1, i + 1):
            linha += str(j) + ' '
        print(linha)

print("\n-- Entrada de número de repetições, processamento de números e vezes a repeti-los e impressão de resultado para usuário --")

while True:
    num = int(float(input("\nDigite o número de repetições: ").replace(' ', '').replace(',', '.')))
    print()

    imprimir_padrao(num)

    if input("\nDeseja continuar? (s/n): ").strip().lower() != 's':
        break

print("\nFim do programa. Obrigado por visitar!\n")