PERCENTUAL_AUMENTO_1 = 0.20
PERCENTUAL_AUMENTO_2 = 0.15
PERCENTUAL_AUMENTO_3 = 0.10
PERCENTUAL_AUMENTO_4 = 0.05

# Autor: Guilherme Caetano Lima
# Exercício: As organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

#       Salários até R$ 280,00 (incluindo): Aumento de 20%
#       Salários entre R$ 280,00 e R$ 700,00: Aumento de 15%
#       Salários entre R$ 700,00 e R$ 1500,00: Aumento de 10%
#       Salários entre R$ 1500,00 em diante: Aumento de 5%

# Após o aumento ser realizado, informe na tela:

#       O salário antes do reajuste
#       O percentual de aumento realizado
#       O valor do aumento
#       O novo salário, apoś o aumento

print("\n-- Entrada de salário de colaborador, processamento de descontos e impressão de resultado para usuário --")

continuar = "s"

while "s" in continuar:
    salario_antes = float(input("\nDigite o salário do colaborador (somente números): ").replace(' ', '').replace(',', '.'))

    if salario_antes <= 280.00:
        valor_aumento = salario_antes * PERCENTUAL_AUMENTO_1
        salario_novo = salario_antes + valor_aumento
        exibir_percentual_aumento = PERCENTUAL_AUMENTO_1 * 100
        

    elif salario_antes > 280.00 and salario_antes <= 700.00:
        valor_aumento = salario_antes * PERCENTUAL_AUMENTO_2
        salario_novo = salario_antes + valor_aumento
        exibir_percentual_aumento = PERCENTUAL_AUMENTO_2 * 100

    elif salario_antes > 700.00 and salario_antes <= 1500.00:
        valor_aumento = salario_antes * PERCENTUAL_AUMENTO_3
        salario_novo = salario_antes + valor_aumento
        exibir_percentual_aumento = PERCENTUAL_AUMENTO_3 * 100

    elif salario_antes > 1500.00:
        valor_aumento = salario_antes * PERCENTUAL_AUMENTO_4
        salario_novo = salario_antes + valor_aumento
        exibir_percentual_aumento = PERCENTUAL_AUMENTO_4 * 100

    print(f"""
Tabela de ajustes
              
Salário antes: R$ {salario_antes:,.2f}.
Percentual de aumento: {exibir_percentual_aumento:,g}%.
Valor do aumento: R$ {valor_aumento:,.2f}.

Salário novo: {salario_novo:,.2f}.
""")
        
    continuar = input("Deseja continuar? (s/n): ").strip().lower()

print("\nFim do programa. Obrigado por visitar!\n")