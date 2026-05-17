# Autor: Guilherme Caetano Lima
# Exercício: Supondo que a população de um país A seja da ordem de 80_000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200_000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento. 

print("-"*50)
print("Processamento de dados, previsão de resultados e impressão de resultado para usuário")
print("-"*50)

populacao_A = 80000
populacao_B = 200000
ano = 0

while populacao_A <= populacao_B:
	populacao_A = populacao_A + (populacao_A * 0.03)
	populacao_B = populacao_B + (populacao_B * 0.015)
	ano += 1
else:
	print(f"""
Resultados

Tamanho original da população A: 80,000
Tamanho original da população B: 200,000

Tamanho final da população A: {populacao_A:,g}
Tamanho final da população B: {populacao_B:,g}

Quantidade de anos para a população A superar a população B: {ano}
""")