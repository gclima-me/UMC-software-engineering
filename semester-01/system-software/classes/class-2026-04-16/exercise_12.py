ALIQUOTA_IMPOSTO_DE_RENDA_1 = 0
ALIQUOTA_IMPOSTO_DE_RENDA_2 = 0.05
ALIQUOTA_IMPOSTO_DE_RENDA_3 = 0.10
ALIQUOTA_IMPOSTO_DE_RENDA_4 = 0.20
ALIQUOTA_SINDICATO = 0.03
ALIQUOTA_INSS = 0.10
ALIQUOTA_FGTS = 0.11

# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do imposto de renda, que depende do salário bruto (conforme tabela abaixo), 3% para o sindicato, 10% para o INSS e FGTS que corresponde a 11% do salário bruto, mas não é descontado (a empresa deposita). O salário líquido corresponde ao salário bruto menos descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

# Desconto do IR:
#       Salário bruto até R$ 900,00 - Isento
#       Salário bruto entre R$ 900,00 e R$ 1500,00 - Desconto de 5%
#       Salário bruto entre R$ 1500,00 e R$ 2500,00 - Desconto de 10%
#       Salário bruto acima de R$ 2500,00 - Desconto de 20%

print("\n-- Entrada de valor da hora trabalhada e horas trabalhadas, processamento de salário mensal e descontos e impressão de resultado para usuário --")

continuar = "s"

while "s" in continuar:
    valor_hora_trabalhada = float(input("\nDigite o valor da hora trabalhada (apenas números): ").replace(' ', '').replace(',', '.'))
    horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas (apenas números): ").replace(' ', '').replace(',', '.'))

    salario_bruto = valor_hora_trabalhada * horas_trabalhadas
    valor_desconto_sindicato = salario_bruto * ALIQUOTA_SINDICATO
    valor_desconto_INSS = salario_bruto * ALIQUOTA_INSS
    valor_FGTS = salario_bruto * ALIQUOTA_FGTS

    if salario_bruto <= 900.00:
        valor_desconto_IR = salario_bruto * ALIQUOTA_IMPOSTO_DE_RENDA_1
        exibir_percentual_IR = ALIQUOTA_IMPOSTO_DE_RENDA_1 * 100
    elif salario_bruto > 900.00 and salario_bruto <= 1500.00:
        valor_desconto_IR = salario_bruto * ALIQUOTA_IMPOSTO_DE_RENDA_2
        exibir_percentual_IR = ALIQUOTA_IMPOSTO_DE_RENDA_2 * 100
    elif salario_bruto > 1500.00 and salario_bruto <= 2500.00:
        valor_desconto_IR = salario_bruto * ALIQUOTA_IMPOSTO_DE_RENDA_3
        exibir_percentual_IR = ALIQUOTA_IMPOSTO_DE_RENDA_3 * 100
    elif salario_bruto > 2500:
        valor_desconto_IR = salario_bruto * ALIQUOTA_IMPOSTO_DE_RENDA_4
        exibir_percentual_IR = ALIQUOTA_IMPOSTO_DE_RENDA_4 * 100

    total_descontos = valor_desconto_sindicato + valor_desconto_INSS + valor_desconto_IR
    salario_liquido = salario_bruto - total_descontos

    print(f"""
Folha de pagamento
          
Valor da hora trabalhada: R$ {valor_hora_trabalhada:,.2f}.
Horas trabalhadas: {horas_trabalhadas:,g} Horas.
Salário bruto: R$ {salario_bruto:,.2f}.

(-) Desconto do IR ({exibir_percentual_IR:,g}%): R$ {valor_desconto_IR:,.2f}.
(-) Desconto do INSS ({ALIQUOTA_INSS * 100:,g}%): R$ {valor_desconto_INSS:,.2f}.
(-) Desconto do sindicato ({ALIQUOTA_SINDICATO * 100:,g}%): R$ {valor_desconto_sindicato:,.2f}.
FGTS ({ALIQUOTA_FGTS * 100:,g}%): R$ {valor_FGTS:,.2f}.

Total de descontos: R$ {total_descontos:,.2f}.
Salário líquido: R$ {salario_liquido:,.2f}.
""")
    
    continuar = input("Deseja continuar? (s/n): ").strip().lower()

print("\nFim do programa. Obrigado por visitar!\n")