TAXA_IMPOSTO = 0.07

# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa com uma função chamada soma_imposto. A função possui dois parâmetros formais: taxa_imposto, que é a quantia de imposto sobre vendas expressas em porcentagem, e custo, que é o custo de um item antes do imposto. A função "altera" o valor de custo para incluir o imposto sobre vendas.

def soma_imposto(taxa, custo):
    valor_imposto = custo * taxa
    custo_com_imposto = custo + (custo * taxa)
    return custo_com_imposto

print("-- Entrada de custo de item, processamento de imposto sobre item e impressão de resultado para usuário --")

while True:
    custo_inicial = float(input("\nDigite o custo do item (R$): ").replace(' ', '').replace(',', '.'))

    custo_final = soma_imposto(TAXA_IMPOSTO, custo_inicial)

    print(f"""
Resumo de Item
---------------------------
Custo Original: R$ {custo_inicial:,.2f}
Taxa de Imposto: {TAXA_IMPOSTO * 100:,g}%
VALOR FINAL: R$ {custo_final:,.2f}
---------------------------
""")
    
    if input("Deseja calcular novo item? (s/n): ").strip().lower() != 's':
        break

print("\nFim do programa. Obrigado por visitar!\n")