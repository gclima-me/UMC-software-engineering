# Autor: Guilherme Caetano Lima
# Exercício 8: Faça um programa que receba um número do usuário e imprima todos os números de 0 até ele.

print("\n-- Entrada de número limite, processamento de contagem com while e impressão de resultado --")

while True:
    try:
        limite = int(input("\nDigite um número inteiro positivo: "))

        if limite < 0:
            print("\nERRO: O número deve ser maior ou igual a zero.")
            continue

        print(f"\nSequência de 0 até {limite}:\n")
        
        i = 0
        while i <= limite:
            print(i, end=" ")
            i += 1
        
        print()

    except ValueError:
        print("\nERRO: Digite apenas números inteiros.")
        continue

    if input("\nDeseja ver outra sequência? [s/n]: ").strip().lower() != 's':
        break

print("\nFim do programa. Obrigado por visitar!\n")