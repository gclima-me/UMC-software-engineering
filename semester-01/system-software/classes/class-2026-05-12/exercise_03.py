# Autor: Guilherme Caetano Lima
# Exercício 3: Ler um número e escreva se ele "é primo" ou "não é primo".

print("\n-- Entrada de número, verificação de se é primo ou não e impressão de resultado para usuário --")

while True:
    try:
        num = int(input("\nDigite um número inteiro: "))

        if num < 2:
            resultado = " não"
        else:
            e_primo = True
            divisor = 2

            while divisor * divisor <= num:
                if num % divisor == 0:
                    e_primo = False
                    break
                divisor += 1
            
            if e_primo:
                resultado = ""
            else:
                resultado = " não"

        print(f"\nO número {num}{resultado} é primo!")

    except ValueError:
        print("\nERRO: Digite apenas números inteiros.")
        continue

    if input("\nDeseja verificar mais algum número? [s/n]: ").strip().lower() != 's':
        break

print("\nFim do programa. Obrigado por visitar!\n")