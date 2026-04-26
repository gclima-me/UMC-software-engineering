# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que leia 4 notas, mostre as notas e a média na tela.

print("\n-- Entrada de 4 notas, processamento de média e impressão de resultado para usuário --")

while True:
    notas = []

    print("")

    for i in range(1, 5):
        nota = float(input(f"Digite a {i}° nota: ").replace(' ', '').replace(',', '.'))
        notas.append(nota)

    soma = sum(notas)
    quantidade = len(notas)
    media = soma / quantidade

    print(f"""
-- Resumo de notas --
          
Notas: {notas}
Soma das notas: {soma:,g}
Quantidade de notas: {quantidade}
Média: {media:,g}
""")
    
    continuar = input("Deseja analisar outra média? (s/n): ").strip().lower()
    if not 's' in continuar:
        break

print("\nFim do programa. Obrigado por visitar!\n")