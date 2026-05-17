vogais = ['A', 'E', 'I', 'O', 'U']
consoantes = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z', 'Ç']
acentos = ['.', ',', ':', ';', '?', '!', '@', '#', '$', '%', '¨', '&', '*', '(', ')', '-', '_', '+', '=', '/', '°', '|', '"', "'"]

# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que verifique se uma letra digitada é vogal ou consoante.

print("\n-- Entrada de letra, verificação de se é consoante ou vogal e impressão de resultado para usuário --")

continuar = "s"

while "s" in continuar:
    letra = input("\nDigite a letra a ser verificada: ").strip().upper()

    if letra in vogais:
        print(f'\nA letra "{letra}" é uma vogal!')
    elif letra in consoantes:
        print(f'\nA letra "{letra}" é uma consoante!')
    elif letra in acentos:
        print("\nIsso é um caractere, não uma letra!")
    elif letra.isdigit:
        print("\nIsso é um número, não uma letra!")
    else:
        print("\nParece que você dormiu no teclado! Tente novamente.")

    continuar = input("\nDeseja continuar? (s/n): ").strip().lower()

print("\nFim do programa. Obrigado por visitar!\n")