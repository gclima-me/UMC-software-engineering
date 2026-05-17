# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

print("-"*50)
print("Entrada de dois números, processamento de intervalo e impressão de resultado para usuário")
print("-"*50)
print("")

while True:
    n1 = int(float(input("Digite o primeiro número inteiro: ").replace(' ', '').replace(',', '.')))
    n2 = int(float(input("Digite o segundo número inteiro: ").replace(' ', '').replace(',', '.')))

    print(f"\nExibindo o intervalo entre {n1} e {n2}:")

    if n1 < n2:
        inicio = n1
        fim = n2
    else:
        inicio = n2
        fim = n1

    for i in range(inicio + 1, fim):
        print(i, end=" ")

    continuar = input("\n\nDeseja continuar? (s/n): ").strip().lower()
    if continuar != 's':
        break

print("\nFim do programa. Obrigado por visitar!\n")