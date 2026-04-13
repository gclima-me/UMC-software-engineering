# Autor: Guilherme Caetano Lima
# Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes.

print("-- Entrada de tamanho de arquivo em Gigabytes, processamento de conversão para Megabytes e Kilobytes e impressão de resultados para usuário --")

continuar = "s"

while "s" in continuar:
    gb = float(input("\nDigite o tamanho do arquivo (GB): ").replace(' ', '').replace(',', '.'))

    print(f"""
Resumo das conversões:

Quantidade de Gigabytes: {gb:,g} GB

Conversão para Megabytes:
{gb:g} * 1024 = {gb * 1024:,g} MB

Conversão para Kilobytes:
{gb:g} * 1024 * 1024 = {gb * 1024 * 1024:,g} KB
""")

    continuar = input("Deseja continuar? (s/n): ").strip().lower()

print("\nFim do programa. Obrigado por visitar!")