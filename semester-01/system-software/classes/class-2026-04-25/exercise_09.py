# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que leia um vetor de 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

print("\n-- Entrada de 10 números inteiros, cálculo da soma dos quadrados e impressão de resultado para usuário --")

while True:
    vetor_numeros = []
    soma_quadrados = 0

    for i in range(1, 11):
        num = int(float(input(f"Digite o {i}° número inteiro: ").replace(' ', '').replace(',', '.')))
        vetor_numeros.append(num)

        soma_quadrados += (num ** 2)

    print(f"""
-- Resultados --
          
Números: {vetor_numeros}
Soma dos quadrados: {soma_quadrados}
""")

    continuar = input("Deseja calcular novas somas? (s/n): ").strip().lower()
    if continuar != 's':
        break

print("\nFim do programa. Obrigado por visitar!\n")