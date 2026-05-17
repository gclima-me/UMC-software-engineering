# Autor: Guilherme Caetano Lima
# Exercício: Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def contar_digitos(n):
    texto = str(n)
    return len(texto)

print("\n-- Entrada de número, contagem de dígitos e impressão de resultado para usuário --")

while True:
    num = int(input("\nDigite um número inteiro: "))

    resultado = contar_digitos(num)
    print(f"\nO número tem {resultado} dígitos.")

    if input("\nDeseja continuar? (s/n): ").strip().lower() != 's':
        break

print("\nFim do programa. Obrigado por visitar!\n")