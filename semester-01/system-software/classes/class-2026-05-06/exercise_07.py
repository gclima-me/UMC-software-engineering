# Autor: Guilherme Caetano Lima
# Exercício: Função valor_pagamento para determinar o valor a ser pago por uma prestação.
# Multa de 3% para atraso, mais 0,1% de juros por dia.

def valor_pagamento(valor, dias):
    if dias <= 0:
        return valor
    else:
        multa = valor * 0.03
        juros = valor * (dias * 0.001)
        return valor + multa + juros

print("\n-- Entrada de prestações, cálculo de juros/multas e relatório de pagamentos --")

total_pago = 0
quantidade = 0

while True:
    valor_prestacao = float(input("\nValor da prestação (0 para sair): ").replace(',', '.'))
    
    if valor_prestacao == 0:
        break
        
    dias_atraso = int(input("Dias em atraso: "))

    valor_final = valor_pagamento(valor_prestacao, dias_atraso)
    
    total_pago += valor_final
    quantidade += 1

    print(f"Valor a pagar: R$ {valor_final:,.2f}")

print(f"""
Resumo da prestação
---------------------------
Quantidade de prestações: {quantidade}
Valor total recebido: R$ {total_pago:,.2f}
---------------------------
""")

print("Fim do programa. Obrigado por visitar!\n")