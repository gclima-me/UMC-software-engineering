# Autor: Guilherme Caetano Lima
# Exercício 01: Crie uma lista com 5 números e mostre o maior valor.

print("\n-- Entrada de 5 números, inserção em lista e impressão do maior número para usuário --\n")

numeros = []

while True:
    try:
        for i in range(1, 6):
            entrada = input(f"Digite o {i}° número: ")
            num = float(entrada.replace(' ', '').replace(',', '.'))

            numeros.append(num)
    except ValueError:
        print("\nERRO: Insira apenas números.\n")
        continue

    maior_num = max(numeros)

    print(f"\nO maior número é o {maior_num:,g}.")

    if input("\nDeseja verificar mais números? [s/n]: ").strip().lower() != 's':
        break

print("\nFim do programa. Obrigado por visitar!\n")