# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

print("-- Entrada de ganhos por hora, número de horas trabalhadas e dias do mês, processamento do salário final do mês e impressão de salário final para usuário --")

continuar = "s"

while "s" in continuar:
    horas = float(input("\nDigite o número de horas trabalhadas no mês (contando com fins de semana e feriados/folgas remunerados(as)): ").replace(' ', '').replace(',', '.'))
    salHora = float(input("Digite o seu salário por hora trabalhada (Ex: R$ 00,00): ").replace(' ', '').replace(',', '.'))

    print(f"""
Resumo do mês:
Número de horas trabalhadas no mês: {horas:,g} horas.
Salário por hora trabalhada: R$ {salHora:,.2f}.
Salário final: R$ {salHora * horas:,.2f}.
""")
    
    continuar = input("Deseja continuar? (s/n): ").strip().lower()

print("\nFim do programa. Obrigado por visitar!")