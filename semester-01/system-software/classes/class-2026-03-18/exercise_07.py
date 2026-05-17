#7. Conversor de Moeda: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira (em R$) e mostre quantos dólares ela pode comprar (Considere US$ 1,00 R$ 5,00).

print('Conversor de reais para dólares')

valReal = float(input('Insira o valor de reais que você deseja converter: '))

valDolar = valReal * 5

print('O valor de R$', valReal, 'em dólares é: US$', valDolar)