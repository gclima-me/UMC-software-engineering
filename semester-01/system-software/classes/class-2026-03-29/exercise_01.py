# Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. A fórmula de conversão é F <- (9 * C + 160) / 5, sendo F a temperatura em Fahrenheit e C a temperatura  em Celsius.

#Autor: Guilherme Caetano Lima

tempCelsius = float(input(f'-- Conversor de graus Celsius para Fahrenheit --\n\nDigite a temperatura em graus Celsius: '))

tempFahrenheit = (9 * tempCelsius + 160) / 5

print(f'\nA temperatura de {tempCelsius}° Celsius em Fahrenheit é de: {tempFahrenheit:.2f}° Farenheit.')