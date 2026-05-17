# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

print("\n-- Entrada de ano, verificação se é ou não bissexto e impressão de resultado para usuário --")

continuar = "s"

while "s" in continuar:
    ano = int(float(input("\nDigite o ano para a verificação (somente números): ").replace(' ', '').replace(',', '.')))

    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f'\nO ano "{ano}" é bissexto.')
    else:
        print(f'\nO ano "{ano}" não é bissexto.')

    continuar = input("\nDeseja continuar? (s/n): ").strip().lower()

print("\nFim do programa. Obrigado por visitar!\n")