# Elaborar um programa que calcule e apresente o valor do volume de uma caixa retangular, utilizando a fórmula VOLUME= COMPRIMENTO* LARGURA* ALTURA.

# Autor: Guilherme Caetano Lima

comprimento = float(input('-- Calcular o volume de uma caixa retangular --\n\nDigite o comprimento da caixa (centímetros): '))

largura = float(input('Digite a largura da caixa (centímetros): '))

altura = float(input('Digite a altura da caixa (centímetros): '))

volumeMls = comprimento * largura * altura

volumeLts = volumeMls / 1000

print(f"""
      -- Resumo e resultado --
      Comprimento da caixa: {comprimento}cm.
      Largura da caixa: {largura}cm.
      Altura da caixa: {altura}cm.
      Volume da caixa: {volumeLts:.2f} Litros ({volumeMls} Mililitros).
      """)