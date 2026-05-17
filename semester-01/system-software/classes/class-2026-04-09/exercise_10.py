# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

# DETALHE: O exercício anterior é muito parecido com esse, então o código acaba sendo o mesmo...

print("-- Entrada de graus fahrenheit, graus celsius ou graus Kelvin, processamento de conversão de Fahrenheit para Celsius ou Celsius para Fahrenheit e impressão de conversão para usuário --")

continuar = "s"
while "s" in continuar:
    opcao = input("""
Digite uma das opções a seguir:
1 - Fahrenheit para Celsius
2 - Fahrenheit para Kelvin
3 - Celsius para Fahrenheit
4 - Celsius para Kelvin
5 - Kelvin para Celsius
6 - Kelvin para Fahrenheit
Opção: """).strip()
    
    if opcao == "1":
        fahrenheit = float(input("\nDigite a temperatura em graus Fahrenheit: ").replace(' ', '').replace(',', '.'))
        print(f"\nO resultado da conversão é: {fahrenheit:g}° Fahrenheit --> {(fahrenheit - 32) / 1.8:g}° Celsius.")

    elif opcao == "2":
        fahrenheit = float(input("\nDigite a temperatura em graus Fahrenheit: ").replace(' ', '').replace(',', '.'))
        print(f"\nO resultado da conversão é: {fahrenheit:g}° Fahrenheit --> {(fahrenheit - 32) / 1.8 + 273.15:g} Kelvin.")

    elif opcao == "3":
        celsius = float(input("\nDigite a temperatura em graus Celsius: ").replace(' ', '').replace(',', '.'))
        print(f"\nO resultado da conversão é: {celsius:g}° Celsius --> {celsius * 1.8 + 32:g}° Fahrenheit.") 
        
    elif opcao == "4":
        celsius = float(input("\nDigite a temperatura em graus Celsius: ").replace(' ', '').replace(',', '.'))
        print(f"\nO resultado da conversão é: {celsius:g}° Celsius --> {celsius + 273.15:g} Kelvin.")

    elif opcao == "5":
        kelvin = float(input("\nDigite a temperatura em Kelvin: ").replace(' ', '').replace(',', '.'))
        print(f"\nO resultado da conversão é: {kelvin:g} Kelvin --> {kelvin - 273.15:g}° Celsius.")

    elif opcao == "6":
        kelvin = float(input("\nDigite a temperatura em Kelvin: ").replace(' ', '').replace(',', '.'))
        print(f"\nO resultado da conversão é: {kelvin:g} Kelvin --> {(kelvin - 273.15) * 1.8 + 32:g}° Fahrenheit.")

    else:
        print("\nERRO: Digite uma opção válida (apenas 1, 2, 3, 4, 5 ou 6).")
        continue

    continuar = input("\nDeseja continua? (s/n): ").strip().lower()

print("\nFim do programa. Obrigado por visitar!")