PRECO_KILO = 4.00
LIMITE_PESO_SP = 50

# Autor: Guilherme Caetano Lima
# Exercício: João, um pescador, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

print("-- Entrada de peso de peixes, processamento de peso excedente e multa e impressão de excesso e multa --")

continuar = "s"

while "s" in continuar:
    pesoPeixes = float(input("\nDigite a quantidade de quilos de peixe (KG): ").replace(' ', '').replace(',', '.'))

    if pesoPeixes > LIMITE_PESO_SP:
        excesso = pesoPeixes - LIMITE_PESO_SP
        multa = excesso * PRECO_KILO

        print(f"""
Resumo de custos:
              
Quantidade de KG de peixe: {pesoPeixes:,g} KG.
Limite KG do estado de SP: {LIMITE_PESO_SP:,g} KG.
KG excedentes: {excesso:,g} KG.

Preço por KG excedente: R$ {PRECO_KILO:,.2f}.
Valor da multa: R$ {multa:,.2f}. """)
        
    else:
        print(f"\nSem multas a pagar. a quantidade de {pesoPeixes:,g} KG de peixe está dentro do limite estabelecido pelo estado de São Paulo ({LIMITE_PESO_SP} KG).")
    
    continuar = input("\nDeseja continuar? (s/n): ").strip().lower()

print("\nFim do programa. Obrigado por visitar!")