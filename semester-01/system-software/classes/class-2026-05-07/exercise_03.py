# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa, utilizando while e listas, que permita o usuário escrever o nome de cinco pessoas e os mostre na tela.

print("\n-- Entrada de nomes de cinco pessoas, inserção dos nomes dentro de uma lista e impressão de resultado para usuário --")

while True:
    lista_nomes = []
    contador = 1

    print()
    while contador < 6:
        nome = input(f"Digite o {contador}° nome: ").strip()

        if not nome or any(caractere.isdigit() for caractere in nome):
            print("\nERRO: O nome não pode conter números ou estar vazio.\n")
        else:
            lista_nomes.append(nome)
            contador += 1

    if input(f"""
Nomes: {lista_nomes}

Os nomes estão corretos? (s/n): """).strip().lower() == 's':
        print("\nNomes cadastrados com sucesso!\n")
    else:
        continue

    if input("Deseja cadastrar mais nomes? [s/n]: ").strip().lower() != 's':
        break

print("\nFim do programa. Obrigado por visitar!\n")