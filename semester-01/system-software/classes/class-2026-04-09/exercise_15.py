ALIQUOTA_IMPOSTO_DE_RENDA = 0.11
ALIQUOTA_INSS = 0.08
ALIQUOTA_SINDICATO = 0.05

# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#       salário bruto.
#       quanto pagou ao INSS.
#       quanto pagou ao sindicato.
#       calcule os descontos e o salário líquido, conforme a tabela abaixo:

#           + Salário Bruto : R$
#           - IR (11%) : R$
#           - INSS (8%) : R$
#           - Sindicato ( 5%) : R$
#           = Salário Liquido : R$

#       Obs.: Salário Bruto - Descontos = Salário Líquido.

print("-- Entrada de salário por hora trabalhada e horas trabalhadas no mês, processamento de salário bruto, descontos de Imposto de Renda, INSS e Sindicato e impressão de salário bruto, descontos e salário líquido para usuário --")

continuar = "s"

while "s" in continuar:
    salHora = float(input("\nDigite quanto você ganha por hora trabalhada (Ex: 24,90): ").replace(' ', '').replace(',', '.'))
    horasTrabalhadas = float(input("Digite a quantidade de horas que você trabalhou no mês (Ex: 180): ").replace(' ', '').replace(',', '.'))

    salBruto = horasTrabalhadas * salHora
    descontoIR = salBruto * ALIQUOTA_IMPOSTO_DE_RENDA
    descontoINSS = salBruto * ALIQUOTA_INSS
    descontoSindicato = salBruto * ALIQUOTA_SINDICATO
    totalDescontos = descontoIR + descontoINSS + descontoSindicato
    salLiquido = salBruto - totalDescontos

    print(f"""
Tabela de salário final e descontos:
          
Salário por hora trabalhada: R$ {salHora:,.2f}.
Horas trabalhadas: {horasTrabalhadas:,g} Horas.

Salário Bruto: R$ {salBruto:,.2f}.
Desconto do Imposto de renda ({ALIQUOTA_IMPOSTO_DE_RENDA * 100:g}%): R$ {descontoIR:,.2f}.
Desconto do INSS ({ALIQUOTA_INSS * 100:g}%): R$ {descontoINSS:,.2f}.
Desconto do Sindicato ({ALIQUOTA_SINDICATO * 100:g}%): R$ {descontoSindicato:,.2f}.

Total de descontos: R$ {totalDescontos:,.2f}.

Salário Líquido: R$ {salLiquido:,.2f}.
""")
    
    continuar = input("Deseja continuar? (s/n): ").strip().lower()

print("\nFim do programa. Obrigado por visitar!")