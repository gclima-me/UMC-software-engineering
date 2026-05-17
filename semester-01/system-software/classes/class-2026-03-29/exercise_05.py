# Efetuar o cálculo e apresentar o valor de uma prestação de um bem em atraso, utilizando a fórmula PRESTAÇÃO= VALOR+ (VALOR* (TAXA/100) * TEMPO).

# Autor: Guilherme Caetano Lima

valor = float(input('-- Calcular valor da prestação de um ber em atraso --\n\nDigite o valor da prestação: '))

taxa = float(input('Digite o valor da taxa de juros (%): '))

tempo = float(input('Digite a quantidade de tempo (meses): '))

prestacao = valor + (valor * (taxa/100) * tempo)

print(f"""
      -- Resumo da prestação --
      Valor inicial: R$ {valor:.2f}.
      Taxa de juros: {taxa}%.
      Tempo: {tempo:.0f} meses.
      Valor da prestação: R$ {prestacao:.2f}.
      """)