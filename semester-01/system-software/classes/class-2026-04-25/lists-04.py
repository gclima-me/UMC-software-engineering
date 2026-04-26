# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

VOGAIS = "aeiouáéíóúàèìòùâêîôûãẽĩõũäëïöü"
LIMITE_PALAVRA = 10

print("\n-- Entrada de vetor de até 10 caracteres, verificação de consoantes e impressão de resultado para usuário --")

while True:
    entrada = input(f"\nDigite uma palavra de até {LIMITE_PALAVRA} caracteres: ").strip()

    if len(entrada) <= 0 or len(entrada) > LIMITE_PALAVRA or ' ' in entrada:
        print(f"\nERRO: Digite apenas uma palavra de até {LIMITE_PALAVRA} caracteres. Tente novamente\n")
        continue

    vetor_palavra = list(entrada)

    vetor_consoantes = []
    for char in vetor_palavra:
        if char.isalpha() and char.lower() not in VOGAIS:
            vetor_consoantes.append(char)

    print(f"""
-- Resultados --
          
Palavra: {entrada}
Letras da palavra: {vetor_palavra}
Consoantes: {vetor_consoantes}
""")
    
    continuar = input("Deseja continuar? (s/n): ").strip().lower()
    if continuar != 's':
        break

print("\nFim do programa. Obrigado por visitar!\n")