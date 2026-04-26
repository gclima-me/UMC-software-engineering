# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

print("\n-- Entrada de 5 números inteiros, cálculo de soma e multiplicação e impressão de resultados para usuário --")

while True:
    vetor_numeros = []
    soma = 0
    multiplicacao = 1

    for i in range(1, 6):
        num = int(float(input(f"Digite o {i}° número inteiro: ").replace(' ', '').replace(',', '.')))
        vetor_numeros.append(num)

        soma += num
        multiplicacao *= num

    print(f"""
-- Resultados --
          
Números: {vetor_numeros}
Soma: {soma}
Multiplicação: {multiplicacao}
""")

    continuar = input("Deseja continuar? (s/n): ").strip().lower()
    if continuar != 's':
        break

print("\nFim do programa. Obrigado por visitar!\n")