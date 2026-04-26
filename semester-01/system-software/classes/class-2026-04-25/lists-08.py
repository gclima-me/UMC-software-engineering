# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

print("\n-- Entrada de idade e altura de 5 pessoas, armazenamento em vetores, inversão de valores e impressão de resultado para usuário --")

while True:
    vetor_idades = []
    vetor_alturas = []

    for i in range(1, 6):
        print(f"\nDados da {i}° pessoa:")
        idade = int(float(input("Digite a idade: ").replace(' ', '').replace(',', '.')))
        altura = float(input("Digite a altura: ").replace(' ', '').replace(',', '.'))

        vetor_idades.append(idade)
        vetor_alturas.append(altura)

    print(f"""
-- Resultado --
          
Idades: {vetor_idades[::-1]}
Alturas: {vetor_alturas[::-1]}
""")

    continuar = input("Deseja continuar? (s/n): ").strip().lower()
    if continuar != 's':
        break

print("\nFim do programa. Obrigado por visitar!\n")