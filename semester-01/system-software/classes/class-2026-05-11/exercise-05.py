# Autor: Guilherme Caetano Lima
# Exercício: Um sistema matemático precisa verificar se os números fornecidos pelo usuário são primos, repetindo a operação até que o usuário decida parar.

def verificar_primo(n):
    if n < 2:
        return " não"
    for i in range(2, n):
        if n % i == 0:
            return " não"
    return ""

print("\n-- Entrada de número, verificação de se é primo ou não e impressão de resultado para usuário --")

while True:
    try:
        num = int(input("\nDigite um número inteiro: "))
    except ValueError:
        print("\nERRO: Digite apenas números inteiros.")
        continue

    resultado = verificar_primo(num)

    print(f"\nO número {num}{resultado} é primo!")

    if input("\nDeseja verificar mais algum número? [s/n]: ").strip().lower() != 's':
        break

print("\nFim do programa. Obrigado por visitar!\n")