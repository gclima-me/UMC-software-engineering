# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

print("\n-- Entrada de 10 números reais, agrupamento em vetor, inversão da ordem dos elementos e impressão de resultado para usuário --")

while True:
    vetor = []

    print("")

    for i in range(1, 11):
        num = float(input(f"Digite o {i}° número: ").replace(' ', '').replace(',', '.'))
        vetor.append(num)

    print(f"\nExibindo vetor com os números ao contrário:\n\n{vetor[::-1]}")

    continuar = input("\nDeseja criar outro vetor? (s/n): ").strip().lower()
    if not 's' in continuar:
        break

print("\nFim do programa. Obrigado por visitar!\n")