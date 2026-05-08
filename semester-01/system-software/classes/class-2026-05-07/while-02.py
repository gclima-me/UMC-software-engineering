# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa, utilizando while, que mostre na tela de 0 até N, em que N é i limite inserido pelo usuário.

print("\n-- Entrada de limite para laço de repetição de impressão de números de 0 a 100 e impressão de resultado para usuário --")

while True:
    try:
        num = 0

        limite = int(input("\nDigite o limite do laço de repetição (apenas números inteiros): ").replace(' ', '').replace(',', '.'))

        print("\n-- Imprimindo números --\n")

        while num < limite + 1:
            print(num, end=" ")
            num += 1

        if input("\n\nDeseja imprimir mais números? [s/n]: ").strip().lower() != 's':
            break

    except ValueError:
        print("\nERRO: Digite apenas números inteiros.")
        continue

print("\nFim do programa. Obrigado por visitar!\n")