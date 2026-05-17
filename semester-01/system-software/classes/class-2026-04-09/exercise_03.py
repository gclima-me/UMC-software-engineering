# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que peça dois números e imprima a soma.

print("-- Entrada de dois números, processamento de soma e impressão de resultado para usuário --")

continuar = "s"

while "s" in continuar:
    num1 = float(input("\nDigite o primeiro número: ").replace(' ', '').replace(',', '.'))
    num2 = float(input("Digite o segundo número: ").replace(' ', '').replace(',', '.'))
    
    print(f"\nO resultado da soma é: {num1:,g} + {num2:,g} = {num1 + num2:,g}.")

    continuar = input("\nDeseja continuar? (s/n): ").strip().lower()

print("\nFim do programa. Obrigado pela visita!")