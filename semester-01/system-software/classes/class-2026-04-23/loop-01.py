# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

continuar = "s"

print("-"*50)
print("Entrada de número, verificação se número é correto com loop e if e impressão de resultado para usuário")
print("-"*50)

while True:
    num = float(input("\nTente adivinhar o número certo entre 0 e 10: ").replace(' ', '').replace(',', '.'))

    if num > 10 or num < 0:
        print("\nTente somente números entre 0 e 10.")
        continue

    while num != 5:
        print("\nErrou! Tente novamente.")
        break
    else:
        print("\nParabéns, você acertou!")

    continuar = input("\nDeseja continuar? (s/n): ").strip().lower()
    if continuar != 's':
        break

print("\nFim do programa. Obrigado por usar!\n")