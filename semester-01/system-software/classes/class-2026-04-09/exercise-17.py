COBERTURA_TINTA_LITRO_METRO = 6
QUANTIDADE_LITROS_LATA_TINTA = 18
PRECO_LATA_TINTA = 80.00
QUANTIDADE_LITROS_GALAO_TINTA = 3.6
PRECO_GALAO_TINTA = 25.00
MARGEM_FOLGA = 1.10

# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

print("-- Entrada de tamanho de área a ser pintada, processamento de quantidades de latas e galões de tinta e preço total e impressão de resultados para usuário --")

continuar = "s"

while "s" in continuar:
    area = float(input("\nDigite o tamanho da área a ser pintada (Ex: 15): ").replace(' ', '').replace(',', '.'))

# -- Cálculo litros necessários --
    litrosNecessarios = (area / COBERTURA_TINTA_LITRO_METRO) * MARGEM_FOLGA

# -- Cálculo de somente quantidade de latas de tinta e preço --
    quantLatasTinta = int(litrosNecessarios / QUANTIDADE_LITROS_LATA_TINTA)

    if litrosNecessarios % QUANTIDADE_LITROS_LATA_TINTA > 0:
        quantLatasTinta = quantLatasTinta + 1

    precoApenasLatas = quantLatasTinta * PRECO_LATA_TINTA

# -- Cálculo de somente quantidade de galões de tinta e preço --
    quantGaloesTinta = int(litrosNecessarios / QUANTIDADE_LITROS_GALAO_TINTA)

    if litrosNecessarios % QUANTIDADE_LITROS_GALAO_TINTA > 0:
        quantGaloesTinta = quantGaloesTinta + 1
    
    precoApenasGaloes = quantGaloesTinta * PRECO_GALAO_TINTA

# -- Cálculo de quantidade de latas e galões de tinta misturados e preço --
    quantLatasMistura = int(litrosNecessarios / QUANTIDADE_LITROS_LATA_TINTA)
    litrosRestantes = litrosNecessarios % QUANTIDADE_LITROS_LATA_TINTA

    quantGaloesMistura = int(litrosRestantes / QUANTIDADE_LITROS_GALAO_TINTA)
    if litrosRestantes % QUANTIDADE_LITROS_GALAO_TINTA > 0:
        quantGaloesMistura = quantGaloesMistura + 1

    precoLatasGaloes = quantLatasMistura * PRECO_LATA_TINTA + quantGaloesMistura * PRECO_GALAO_TINTA

    print(f"""
Resumo de valores finais:
          
Quantidade de litros da lata de tinta: {QUANTIDADE_LITROS_LATA_TINTA:,g}L.
Preço da lata de tinta (unitário): R$ {PRECO_LATA_TINTA:,.2f}.
Quantidade de litros do galão de tinta : {QUANTIDADE_LITROS_GALAO_TINTA:,g}L.
Preço do galão de tinta (unitário): R$ {PRECO_GALAO_TINTA:,.2f}.

Tamanho da área: {area:,g} m².

1 - Comprando apenas latas de tinta:
    Quantidade de latas de tinta: {quantLatasTinta:,g}.
    Preço total a pagar: R$ {precoApenasLatas:,.2f}.

2 - Comprando apenas galões de tinta:
    Quantidade de galões de tinta: {quantGaloesTinta:,g}.
    Preço total a pagar: R$ {precoApenasGaloes:,.2f}.

3 - Comprando latas de tinta e galões misturados:
    Quantidade de latas de tinta: {quantLatasMistura:,g}.
    Quantidade de galões de tinta: {quantGaloesMistura:,g}.
    Preço total a pagar: {precoLatasGaloes:,.2f}.
""")
    
    continuar = input("Deseja continuar? (s/n): ").strip().lower()

print("\nFim do programa. Obrigado por visitar!")

