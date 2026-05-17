# Autor: Guilherme Caetano Lima
# Exercício 4: Receba N números do usuário e calcule a média aritmética.

print("\n-- Entrada de quantidade e valores, processamento de média aritmética e Saída de resultado --")

while True:
    try:
        num = int(input("\nQuantos números você deseja inserir para a média? "))
        
        if num <= 0:
            print("\nERRO: A quantidade deve ser maior que zero.")
            continue

        soma = 0
        i = 1
        
        print()
        while i <= num:
            try:
                valor = float(input(f"Digite o {i}º número: "))
                soma += valor
                i += 1
            except ValueError:
                print("\nERRO: Digite um número real válido\n.")

        media = soma / num

        print(f"\nResultado: A média dos {num} números inseridos é {media:.2f}!")

    except ValueError:
        print("\nERRO: Digite apenas números inteiros para a quantidade.")
        continue

    if input("\nDeseja calcular outra média? [s/n]: ").strip().lower() != 's':
        break

print("\nFim do programa. Obrigado por visitar!\n")