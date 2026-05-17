# Autor: Guilherme Caetano Lima
# Exercício 02: Monte uma matriz 2x2 e calcule a soma dos elementos.

print("\n-- Entrada de 4 números, inserção em matriz, processamento de soma e impressão de resultado para usuário --\n")

n = 2

while True:
    matriz_numeros = []
    soma = 0.0
    sucesso = True

    try:
        for i in range(n):
            linha = []
            for j in range(n):
                entrada = input(f"Digite o número para a posição [{i}][{j}]: ")
                num = float(entrada.replace(' ', '').replace(',', '.'))
                
                linha.append(num)
                soma += num
            matriz_numeros.append(linha)

    except ValueError:
        print("\nERRO: Insira apenas números.\n")
        sucesso = False

    if sucesso:
        print("\nMatriz gerada:")
        for linha in matriz_numeros:
            print(linha)
            
        print(f"\nA soma de todos os elementos é: {soma}")

    if input("\nDeseja fazer mais somas? [s/n]: ").strip().lower() != 's':
        break

print("\nFim do programa. Obrigado por visitar!\n")
