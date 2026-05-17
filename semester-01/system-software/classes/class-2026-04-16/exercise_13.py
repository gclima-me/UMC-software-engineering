# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que leia um número e exiba o dia da semana. (1 - Domingo, 2 - Segunda, etc.). Se digitar outro valor, exiba valor inválido.

print("\n-- Entrada de número de dia da semana, verificação de nome de dia da semana equivalente e impressão de resultado para usuário --")

continuar = "s"

while "s" in continuar:
    num_dia = int(float(input("\nDigite o número do dia da semana (apenas números de 1 a 7): ").replace(' ', '').replace(',', '.')))

    if num_dia == 1:
        mensagem = "O dia da semana correspondente para o 1 é: Domingo."
    elif num_dia == 2:
        mensagem = "O dia da semana correspondente para o 2 é: Segunda-feira."
    elif num_dia == 3:
        mensagem = "O dia da semana correspondente para o 3 é: Terça-feira."
    elif num_dia == 4:
        mensagem = "O dia da semana correspondente para o 4 é: Quarta-feira."
    elif num_dia == 5:
        mensagem = "O dia da semana correspondente para o 5 é: Quinta-feira."
    elif num_dia == 6:
        mensagem = "O dia da semana correspondente para o 6 é: Sexta-feira."
    elif num_dia == 7:
        mensagem = "O dia da semana correspondente para o 7 é: Sábado."
    else:
        print("\nERRO: O número não é uma opção válida. Tente algum entre 1 e 7.")
        continue

    print(f"\n{mensagem}")

    continuar = input("\nDeseja continuar? (s/n): ").strip().lower()

print("\nFim do programa. Obrigado por visitar!\n")