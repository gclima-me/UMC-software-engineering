import random

# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere P, se seu argumento for positivo, e N, se seu argumento for zero ou negativo.

def verificar_sinal(n):
    if n > 0:
        return 'P'
    else:
        return 'N'
    
numero_sorteado = random.randint(1, 10)

tentativas = 0

print("\n-- Entrada de número, verificação de se o número está correto ou não e impressão de resultado para usuário --")

while True:
    chute = int(float(input("\nChute um número de 1 a 10 (apenas inteiros): ").replace(' ', '').replace(',', '.')))

    tentativas += 1

    sinal = verificar_sinal(chute)
    print(f"\nO sinal do seu chute é: {sinal}")

    if chute == numero_sorteado:
        print(f"Parabéns, você acertou após {tentativas} tentativas!")
        numero_sorteado = random.randint(1, 10)
        tentativas = 0
    else:
        print("Você errou! Tente novamente.")
    
    if input("\nDeseja adivinhar novamente? (s/n): ").strip().lower() != 's':
        break

print("\nFim do programa. Obrigado por visitar!\n")