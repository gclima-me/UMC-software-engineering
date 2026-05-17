import math

# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que peça o raio de um círculo, calcule e mostre sua área.

print("-- Entrada de raio de circulo, processamento de área e impressão de área para usuário --")

continuar = "s"

while "s" in continuar:
    raio = float(input("\nDigite o raio do círculo: ").replace(' ', '').replace(',', '.'))
    
    print(f"\nA área do círculo com raio {raio:g} é: {math.pi * (raio ** 2):,g}.")

    continuar = input("\nDeseja continuar? (s/n): ").strip().lower()

print("\nFim do programa. Obrigado pela visita!")