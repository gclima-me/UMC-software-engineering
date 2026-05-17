# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa para imprimir:
#       1
#       2 2
#       3 3 3
#       .....
#       n n n n n n ... n

def imprimir_padrao(a):
    for i in range(1, a + 1):
        print(f'{i} ' * i)

print("\n-- Entrada de número de repetições, processamento de números e vezes a repeti-los e impressão de resultado para usuário --")

while True:
    num = int(float(input("\nDigite o número de repetições: ").replace(' ', '').replace(',', '.')))
    print()

    imprimir_padrao(num)

    if input("\nDeseja continuar? (s/n): ").strip().lower() != 's':
        break

print("\nFim do programa. Obrigado por visitar!\n")