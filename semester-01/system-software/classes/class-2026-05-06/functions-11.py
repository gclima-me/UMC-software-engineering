# Autor: Guilherme Caetano Lima
# Exercício 11: Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mês_por_extenso de AAAA. 
# Opcionalmente, valide a data e retorne Nome caso a data seja inválida.

def data_por_extenso(data):
    meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    
    dia = data[0:2]
    mes_num = int(data[3:5])
    ano = data[6:10]

    if mes_num < 1 or mes_num > 12:
        return "Nome"
    
    nome_mes = meses[mes_num - 1]
    
    return f"{dia} de {nome_mes} de {ano}"

print("\n-- Entrada de data em formato numérico, processamento de conversão de mês e impressão de resultado para usuário --")

while True:
    data_input = input("\nDigite a data (DD/MM/AAAA): ").strip()

    resultado = data_por_extenso(data_input)
    print(f"Data formatada: {resultado}")

    if input("\nDeseja continuar? (s/n): ").strip().lower() != 's':
        break

print("\nFim do programa. Obrigado por visitar!\n")