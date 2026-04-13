# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:
#       O produto do dobro do primeiro com metade do segundo.
#       A soma do triplo do primeiro com o terceiro.
#       O terceiro elevado ao cubo.

print("-- Entrada de dois números inteiros e um real, processamento do produto do dobro do primeiro com metade do segundo, soma do triplo do primeiro com terceiro e terceiro elevado ao cubo e impressão de resultados para usuário --")

continuar = "s"

while "s" in continuar:
    num1 = int(float(input("\nDigite o primeiro número (somente números inteiros): ").replace(' ', '').replace(',', '.')))
    num2 = int(float(input("Digite o segundo número (somente números inteiros): ").replace(' ', '').replace(',', '.')))
    num3 = float(input("Digite o terceiro número (somente números reais): ").replace(' ', '').replace(',', '.'))

    print(f""""
Resumo das operações:
          
Número 01 = {num1:,}
Número 02 = {num2:,}
Número 03 = {num3:,g}

Operação 01:
{num1 * 2:,} * {num2 / 2:,g} = {(num1 * 2) * (num2 / 2):,g}
Operação 02:
{num1 * 3:,} + {num3:,g} = {(num1 * 3) + num3:,g}
Operação 03:
{num3:,g}³ = {num3 ** 3:,g}
""")
    
    continuar = input("Deseja continuar? (s/n): ").strip().lower()

print("\nFim do programa. Obrigado por visitar!")