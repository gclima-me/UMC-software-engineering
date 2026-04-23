# Autor: Guilherme Caetano Lima
# Exercício: Fazer um programa que verifique se um número é maior que 10 ou menor que 5.

print("\n-- Entrada de número, verificação de se número é maior ou menor que valor definido e impressão de resultado para o usuário --")

continuar = "s"

while "s" in continuar:
    num1 = float(input("\nDigite o número 1: ").replace(' ', '').replace(',', '.'))
    num2 = float(input("Digite o número 2: ").replace(' ', '').replace(',', '.'))

    if num1 > num2:
        print(f"\nO número 1 ({num1:,g}) é maior que o número 2 ({num2:,g}).")
    elif num2 > num1:
        print(f"\nO número 2 ({num2:,g}) é maior que o número 1 ({num1:,g}).")
    else:
        print(f"\nTanto o número 1 ({num1:,g}) quanto o número 2 ({num2:,g}) são iguais.")

    continuar = input("\nDeseja continuar? (s/n): ").strip().lower()

print("\nFim do programa. Obrigado por visitar!\n")