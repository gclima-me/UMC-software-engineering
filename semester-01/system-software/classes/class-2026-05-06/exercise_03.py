# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def somatoria(a, b, c):
    soma = a + b + c
    return soma

print("\n-- Entrada de três números, processamento de soma de números e impressão de resultado para usuário --")

while True:
    num1 = float(input("\nDigite o primeiro número: ").replace(' ', '').replace(',', '.'))
    num2 = float(input("Digite o segundo número: ").replace(' ', '').replace(',', '.'))
    num3 = float(input("Digite o terceiro número: ").replace(' ', '').replace(',', '.'))
    print()

    resultado = somatoria(num1, num2, num3)

    print(f"""
Resumo da Somatória
---------------------------
Número 1: {num1:,g}
Número 2: {num2:,g}
Número 3: {num3:,g}
{num1:,g} + {num2:,g} + {num3:,g} = {resultado:,g}
---------------------------
""")

    if input("Deseja somar novos números? (s/n): ").strip().lower() != 's':
        break

print("\nFim do programa. Obrigado por visitar!\n")