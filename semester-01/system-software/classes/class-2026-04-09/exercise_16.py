COBERTURA_TINTA_LITRO_METRO = 3
QUANTIDADE_LITROS_LATA_TINTA = 18
PRECO_LATA_TINTA = 80.00

# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

print("-- Entrada de tamanho de área a ser pintada, processamento de quantidades de latas de tinta e preço total e impressão de resultados para usuário --")

continuar = "s"

while "s" in continuar:
    area = float(input("\nDigite o tamanho da área a ser pintada em metros quadrados (Ex: 10): ").replace(' ', '').replace(',', '.'))

    litrosNecessarios = area / COBERTURA_TINTA_LITRO_METRO
    quantLatasTinta = int(litrosNecessarios / QUANTIDADE_LITROS_LATA_TINTA)

    if litrosNecessarios % QUANTIDADE_LITROS_LATA_TINTA > 0:
        quantLatasTinta = quantLatasTinta + 1

    precoTotal = quantLatasTinta * PRECO_LATA_TINTA

    print(f"""
Resumo de valores:

Tamanho da área: {area:,g} m².
Litros de tinta necessários: {litrosNecessarios:,g} Litros.
Quantidade de latas de tinta: {quantLatasTinta:g}.
Preço da lata de tinta: R$ {PRECO_LATA_TINTA:,.2f}.

Preço total: R$ {precoTotal:,.2f}.
""")

    continuar = input("Deseja continuar? (s/n): ").strip().lower()

print("\nFim do programa. Obrigado por visitar!")