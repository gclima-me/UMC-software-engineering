# Calcular e apresentar o valor do volume de uma lata de óleo, utilizando a fórmula VOLUME <- 3.14159 *Ri 2 * ALTURA.

# Autor: Guilherme Caetano Lima

import math

raio = float(input('-- Calculadora de volume de lata de óleo --\n\nDigite o valor do raio da lata (centímetros): '))

altura = float(input('Digite o valor da altura da lata de óleo (centímetros): '))

volume = math.pi * raio ** 2 * altura

print(f'\nO volume da lata de óleo de raio {raio}cm e altura {altura}cm é de: {volume:,.2f}.')