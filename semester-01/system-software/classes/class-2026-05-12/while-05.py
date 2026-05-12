# Autor: Guilherme Caetano Lima
# Exercício 5: Crie um algoritmo que, dado um número informado pelo usuário, imprima a tabuada dele de 1 a 10.

print("\n-- Entrada de número, processamento da tabuada com while e impressão de resultado para usuário --")

while True:
    try:
        num = int(input("\nDeseja ver a tabuada de qual número? "))
        
        print(f"\nTabuada do {num}:")
        print("-" * 15)
        
        i = 1
        while i <= 10:
            print(f"{num} x {i} = {num * i}")
            i += 1
            
        print("-" * 15)

    except ValueError:
        print("\nERRO: Digite apenas números inteiros.")
        continue

    if input("\nDeseja ver outra tabuada? [s/n]: ").strip().lower() != 's':
        break

print("\nFim do programa. Obrigado por visitar!\n")