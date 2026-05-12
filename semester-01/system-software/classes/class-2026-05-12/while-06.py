# Autor: Guilherme Caetano Lima
# Exercício 6: Faça um programa que receba as duas notas e calcule a média de um aluno. Depois pergunte se ele quer calcular outra média. O programa deve ser rodado ao menos uma vez.

print("\n-- Entrada de notas, processamento da média e impressão de resultado para usuário --")

while True:
    try:
        nota1 = float(input("\nDigite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))

        media = (nota1 + nota2) / 2

        print(f"\nA média do aluno é: {media:.2f}")

    except ValueError:
        print("\nERRO: Digite apenas números para as notas.")
        continue

    if input("\nDeseja calcular outra média? [s/n]: ").strip().lower() != 's':
        break

print("\nFim do programa. Obrigado por visitar!\n")