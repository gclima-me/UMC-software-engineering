# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que leia um vetor de 5 números inteiros e mostre-os.

print("\n-- Entrada de 5 números inteiros, agrupamento em vetor e impressão de resultado para usuário --")

while True:
    vetor = []

    print("")

    for i in range(1,6):
        num = int(float(input(f"Digite o {i}° número: ").replace(' ', '').replace(',', '.')))
        vetor.append(num)

    print(f"\nExibindo vetor com os números:\n\n{vetor}")

    continuar = input("\nDeseja criar outro vetor? (s/n): ").strip().lower()
    if not 's' in continuar:
        break

print("\nFim do programa. Obrigado por visitar!\n")