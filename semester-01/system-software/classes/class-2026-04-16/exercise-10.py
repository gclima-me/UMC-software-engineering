opcoes_periodo = ['M', 'V', 'N']

# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que pergunte em que turno você estuda. Peça para digitar:

#       M - Matutino.
#       V - Vespertino.
#       N - Noturno.

#Imprima a mensagem "Bom dia!", "Boa tarde!", "Boa noite!" ou "Valor inválido" conforme o caso.

print("\n-- Entrada de letra referente a turno de estudos, verificação de valor e impressão de resultado para usuário --")

continuar = "s"

while "s" in continuar:
    opcao = input("""
Digite a opção referente ao seu turno de estudos (apenas letra):
M - Matutino
V - Vespertino
N - Noturno
                    
Opção: """).strip().upper()
    
    if opcao in opcoes_periodo:
        if opcao == "M":
            confirmar = input('\nVocê escolheu o período: "M - Matutino".\n\nConfirmar escolha? (s/n): ').strip().lower()
            if confirmar == "s":
                print('\nVocê definiu o período como "M - Matutino". Bom dia!')
            else:
                continue

        elif opcao == "V":
            confirmar = input('\nVocê escolheu o período: "V - Vespertino".\n\nConfirmar escolha? (s/n): ').strip().lower()
            if confirmar == "s":
                print('\nVocê definiu o período como "V - Vespertino". Boa tarde!')
            else:
                continue

        elif opcao == "N":
            confirmar = input('\nVocê escolheu o período: "N - Noturno".\n\nConfirmar escolha? (s/n): ').strip().lower()
            if confirmar == "s":
                print('\nVocê definiu o período como "N - Noturno". Boa noite!')
            else:
                continue

    else:
        print("\nERRO: Valor inválido. Digite apenas uma das opções disponíveis.")
        continue

    continuar = input("\nDeseja continuar? (s/n): ").strip().lower()

print("\nFim do programa. Obrigado por visitar!\n")