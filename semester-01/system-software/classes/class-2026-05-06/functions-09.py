# Autor: Guilherme Caetano Lima
# Exercício: Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def inverter_numero(n):
    texto = str(n)
    reverso = texto[::-1]
    return reverso

print("\n-- Entrada de número, processamento de inversão e impressão de resultado para usuário --")

while True:
    num = int(input("\nDigite um número para inverter: "))

    resultado = inverter_numero(num)
    print(f"\nO número invertido é: {resultado}")

    if input("\nDeseja continuar? (s/n): ").strip().lower() != 's':
        break

print("\nFim do programa. Obrigado por visitar!\n")