# Autor: Guilherme Caetano Lima
# Exercício 2: Somatório de r elevado a i

print("\n-- Entrada de R e N, processamento de somatório de potências e impressão de resultado para usuário --")

while True:
    try:
        r = float(input("\nDigite o valor de r: "))
        n = int(input("Digite o valor de N: "))

        if n < 0:
            print("\nERRO: N deve ser maior ou igual a zero.")
            continue

        soma = 0
        i = 0
        termos = []

        while i <= n:
            termo = r ** i
            soma += termo
            termos.append(str(termo))
            i += 1

        print(f"\nS_{n} = {' + '.join(termos)} = {soma:.3f}")

    except ValueError:
        print("\nERRO: Entrada inválida.")

    if input("\nDeseja continuar? [s/n]: ").strip().lower() != 's':
        break

print("\nFim do programa.\n")