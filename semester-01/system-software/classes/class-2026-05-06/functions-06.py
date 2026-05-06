# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que converta a notação de 24 horas para a notação de 12 horas. 
# Use uma função para a conversão e uma para a saída.

def converter_hora(h, m):
    if h == 0:
        return 12, m, 'A'
    elif h == 12:
        return 12, m, 'P'
    elif h > 12:
        return h - 12, m, 'P'
    else:
        return h, m, 'A'

def exibir_hora(h_conv, m_conv, periodo):
    if periodo == 'A':
        sufixo = "A.M."
    else:
        sufixo = "P.M."
    print(f"\nHorário convertido: {h_conv}:{m_conv:02d} {sufixo}")

print("\n-- Entrada de hora no formato 24h, processamento para formato 12h e impressão de resultado para usuário --")

while True:
    h = int(input("\nDigite a hora (0-23): "))
    m = int(input("Digite os minutos (0-59): "))

    h_c, m_c, p = converter_hora(h, m)
    
    exibir_hora(h_c, m_c, p)

    if input("\nDeseja converter novo horário? (s/n): ").strip().lower() != 's':
        break

print("\nFim do programa. Obrigado por visitar!\n")