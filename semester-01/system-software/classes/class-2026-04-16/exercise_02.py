# Autor: Guilherme
# Exercício: Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

print("\n-- Entrada de um número, verificação de se o valor é positivo, negativo ou neutro e impressão de resultado para usuário --")

continuar = "s"

while "s" in continuar:
    num = float(input("\nDigite o número a ser verificado: "))

    if num < 0:
        print(f"\nO número {num:,g} é negativo.")
    elif num == 0:
        print(f"\nO número {num:,g} é neutro.")
    else:
        print(f"\nO número {num:,g} é positivo.")

    continuar = input("\nDeseja continuar? (s/n): ").strip().lower()

print("\nFim do programa. Obrigado por visitar!\n")