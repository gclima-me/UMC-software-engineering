# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois vetores anteriores.

print("\n-- Entrada de dois vetores de 10 elementos, geração de um terceiro vetor intercalado e impressão de resultado para usuário --")

while True:
    vetor_a = []
    vetor_b = []
    vetor_intercalado = []

    print("\n-- Preenchimento do Vetor A --")
    for i in range(1, 11):
        num = float(input(f"Vetor A - Digite o {i}° número: ").replace(' ', '').replace(',', '.'))
        vetor_a.append(num)

    print("\n-- Preenchimento do Vetor B --")
    for i in range(1, 11):
        num = float(input(f"Vetor B - Digite o {i}° número: ").replace(' ', '').replace(',', '.'))
        vetor_b.append(num)

    for i in range(10):
        vetor_intercalado.append(vetor_a[i])
        vetor_intercalado.append(vetor_b[i])

    print(f"""
-- Resultados --
          
Vetor A: {vetor_a}
Vetor B: {vetor_b}
Vetor Intercalado: {vetor_intercalado}
""")

    continuar = input("Deseja criar novos vetores? (s/n): ").strip().lower()
    if continuar != 's':
        break

print("\nFim do programa. Obrigado por visitar!\n")