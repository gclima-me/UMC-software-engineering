# Ler uma temperatura em graus Fahrenheit e apresentá-la convertida em graus Celsius. A fórmula de conversão é C <- ((F - 32) * 5) / 9, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

# Autor: Guilherme Caetano Lima

tempFahrenheit = float(input(f'-- Conversor de graus Fahrenheit para Celsius --\n\nDigite a temperatura em graus Fahrenheit: '))

tempCelsius = ((tempFahrenheit - 32) * 5) / 9

print(f'\nA temperatura de {tempFahrenheit}° Fahrenheit em Celsius é de: {tempCelsius:.2f}° Celsius.')