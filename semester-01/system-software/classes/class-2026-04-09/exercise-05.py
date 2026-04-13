# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que converta metros para centímetros.

print("-- Entrada de metros ou centímetros, processamento de conversão de medida e impressão de resultado para usuário --")

continuar = "s"

while "s" in continuar:
    opcao = input("""
Digite uma das opções a seguir:
1 - Metros para centímetros
2 - Centímetros para metros
Opção: """).strip()

    if opcao == "1":
        metros = float(input("\nDigite a quantidade de metros que será convertida: ").replace(' ', '').replace(',', '.'))
        centimetros = metros * 100
        print (f"\nO resultado da conversão de {metros:,g} metros para centímetros é: {metros:,g} metro(s) = {centimetros:,g} centímetro(s).")

    elif opcao == "2":
        centimetros = float(input("\nDigite a quantidade de centímetros que será convertida: ").replace(' ', '').replace(',', '.'))
        metros = centimetros / 100
        print(f"\nO resultado da conversão de {centimetros:,g} centímetros para metros é: {centimetros:,g} centímetro(s) = {metros:,g} metro(s).")
        
    else:
        print("\nERRO: Digite uma opção válida (apenas 1 ou 2).")

    continuar = input("\nDeseja continuar? (s/n): ").strip().lower()

print("\nFim do programa. Obrigado pela visita!")