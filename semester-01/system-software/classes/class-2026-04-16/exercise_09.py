# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que leia três números e mostre-os em ordem decrescente.

print("\n-- Entrada de três números, verifação do maior pro menor número e impressão de resultado para usuário --")

continuar = "s"

while "s" in continuar:
    num1 = float(input("\nDigite o primeiro número: ").replace(' ', '').replace(',', '.'))
    num2 = float(input("Digite o segundo número: ").replace(' ', '').replace(',', '.'))
    num3 = float(input("Digite o terceiro número: ").replace(' ', '').replace(',', '.'))

    if num1 > num2 > num3:
        ordem_decrescente_num = f"Ordem decrescente:\n{num1:,g} > {num2:,g} > {num3:,g}."
    elif num1 > num3 > num2:
        ordem_decrescente_num = f"Ordem decrescente:\n{num1:,g} > {num3:,g} > {num2:,g}."
    elif num2 > num1 > num3:
        ordem_decrescente_num = f"Ordem decrescente:\n{num2:,g} > {num1:,g} > {num3:,g}."
    elif num2 > num3 > num1:
        ordem_decrescente_num = f"Ordem decrescente:\n{num2:,g} > {num3:,g} > {num1:,g}."
    elif num3 > num1 > num2:
        ordem_decrescente_num = f"Ordem decrescente:\n{num3:,g} > {num1:,g} > {num2:,g}."
    elif num3 > num2 > num1:
        ordem_decrescente_num = f"Ordem decrescente:\n{num3:,g} > {num2:,g} > {num1:,g}."

    print(f"""
Resumo dos números
          
Número 1: {num1:,g}.
Número 2: {num2:,g}.
Número 3: {num3:,g}.

{ordem_decrescente_num}
""")
    
    continuar = input("Deseja continuar? (s/n): ").strip().lower()

print("\nFim do programa. Obrigado por visitar!\n")