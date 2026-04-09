#2. Conversor de Medidas: Crie um programa que receba un valor em metros e o exiba convertido em centimetros e milimetros.

print('Conversor de metros para centímetros e milímetros')

metros = float(input('Insira a quantidade de metros para converter: '))

centimetros = metros * 100

milimetros = metros * 1000

print(metros, ' em centímetros é:', centimetros)
print(metros, ' em milímetros é:', milimetros)