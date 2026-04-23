# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplica ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

# Média de aproveitamento       Conceito
# Entre 9.0 e 10.0              A
# Entre 7.5 e 9.0               B
# Entre 6.0 e 7.5               C
# Entre 4.0 e 6.0               D
# Entre 4.0 e zero              E

# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem "Aprovado" se o conceito for A, B ou C ou "Reprovado" se o conceito for D ou E.

print("\n-- Entrada de nome e duas notas parciais de aluno, processamento de média e conceito equivalente e impressão de resultado para usuário --")

continuar = "s"

while "s" in continuar:
    nome_aluno = input("\nDigite o nome do aluno: ").strip()
    nota1 = float(input("Digite a primeira nota do aluno: ").replace(' ', '').replace(',', '.'))
    nota2 = float(input("Digite a segunda nota do aluno: ").replace(' ', '').replace(',', '.'))

    media = (nota1 + nota2)/2

    if media >= 9.0:
        conceito = "A"
    elif media >= 7.5 and media < 9.0:
        conceito = "B"
    elif media >= 6.0 and media < 7.5:
        conceito = "C"
    elif media >= 4.0 and media < 6.0:
        conceito = "D"
    else:
        conceito = "E"

    if media >= 6.0:
        situacao = "Aprovado!"
    else:
        situacao = "Reprovado..."

    print(f"""
Tabela de notas do {nome_aluno}

Nota 1: {nota1:,g}.
Nota 2: {nota2:,g}.

Média: {media:,g}
Conceito: {conceito}.

Situação: {situacao}.
""")
    
    continuar = input("Deseja continuar? (s/n): ").strip().lower()

print("\nFim do programa. Obrigado por visitar!\n")