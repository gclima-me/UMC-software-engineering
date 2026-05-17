# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que peça uma data no formato "dd/mm/aaaa" e determine se a mesma é uma data válida.

print("\n-- Entrada de data no formato dd/mm/aaaa, verificação de se é uma data válida e impressão de resultado para usuário --")

continuar = "s"

while "s" in continuar:
    dia = int(float(input("\nDigite o dia (apenas números): ").replace(' ', '')))
    mes = int(float(input("Digite o mês (apenas números): ").replace(' ', '')))
    ano = int(float(input("Digite o ano (apenas números): ").replace(' ', '')))

    valida = False

    if 1 <= mes <= 12:
        if mes in [1, 3, 5, 7, 8, 10, 12]:
            if 1 <= dia <= 31:
                valida = True
        
        elif mes in [4, 6, 9, 11]:
            if 1 <= dia <= 30:
                valida = True

        elif mes == 2:
            if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
                limite_fevereiro = 29
            else:
                limite_fevereiro = 28

            if 1 <= dia <= limite_fevereiro:
                valida = True

    if valida:
        print(f"\nA data {dia}/{mes}/{ano} é válida.")
    else:
        print(f"\nA data {dia}/{mes}/{ano} é inválida.")

    continuar = input("\nDeseja continuar? (s/n): ").strip().lower()

print("\nFim do programa. Obrigado por visitar!\n")