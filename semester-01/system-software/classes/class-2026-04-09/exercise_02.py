# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que peça um número e então mostre a mensagem "O número informado foi [número]".

print("-- Entrada e impressão de dados para usuário --")

continuar = "s"

while "s" in continuar:
    num = float(input("\nDigite o número a ser exibido: ").replace(' ', '').replace(',', '.'))
    
    print(f"\nO número digitado é: {num:,g}.")
    
    continuar = input("\nDeseja continuar? (s/n): ").strip().lower()

print("\nFim do programa. Obrigado pela visita!")