# Autor: Guilherme Caetano Lima
# Exercício: Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação. 

print("-"*50)
print("Processamento de dados, previsão de resultados e impressão de resultado para usuário")
print("-"*50)

while True:
	populacao_A = float(input("\nDigite o tamanho da população A: ").replace(' ', '').replace(',', '.'))
	populacao_B = float(input("\nDigite o tamanho da população B: ").replace(' ', '').replace(',', '.'))
	taxa_crescimento_A = float(input("\nDigite a taxa de crescimento anual da população A (%): ").replace(' ', '').replace(',', '.')) / 100
	taxa_crescimento_B = float(input("\nDigite a taxa de crescimento anual da população B (%): ").replace(' ', '').replace(',', '.')) / 100

	populacao_A_inicial = populacao_A
	populacao_B_inicial = populacao_B
	ano = 0

	if populacao_A < populacao_B and taxa_crescimento_A < taxa_crescimento_B:
		print("\nA população A nunca alcançará a população B com essas taxas de crescimento anuais.\n")
	else:
		while populacao_A <= populacao_B:
			populacao_A = populacao_A + (populacao_A * taxa_crescimento_A)
			populacao_B = populacao_B + (populacao_B * taxa_crescimento_B)
			ano += 1
		else:
			print(f"""
Resultados

Tamanho original da população A: {populacao_A_inicial:,g}
Tamanho original da população B: {populacao_B_inicial:,g}

Tamanho final da população A: {populacao_A:,g}
Tamanho final da população B: {populacao_B:,g}

Quantidade de anos para a população A superar a população B: {ano}
""")

	continuar = input("Deseja realizar outro cálculo? (s/n): ").strip().lower()
	if continuar != 's':
		break

print("\nFim do programa. Obrigado por visitar!")