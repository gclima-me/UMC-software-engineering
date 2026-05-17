# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar: 
#       A mensagem "Aprovado", se a média alcançada for maior ou igual a sete; 
#       A mensagem "Reprovado", se a média for menor do que sete; 
#       A mensagem "Aprovado com Distinção", se a média for igual a dez.

print("\n-- Entrada de duas notas de aluno, processamento de média de notas e impressão de resultado para usuário --")

continuar = "s"

while "s" in continuar:
    nome_aluno = input("\nDigite o nome do(a) aluno(a): ").strip()
    nota1 = float(input(f"Digite a primeira nota do(a) {nome_aluno}: ").replace(' ', '').replace('.', '.'))
    nota2 = float(input(f"Digite a segunda nota do(a) {nome_aluno}: ").replace(' ', '').replace(',', '.'))

    media = (nota1 + nota2) / 2
    if media >= 10:
        situacao = "Aprovado(a) com distinção!!"
    elif media >= 7:
        situacao = "Aprovado(a)!"
    else:
        situacao = "Reprovado(a)..."

    print(f"""
Resumo do(a) {nome_aluno}

Nota 1: {nota1:,g}.
Nota 2: {nota2:,g}.
Média: {media:,g}.

Situação: {situacao}
""")
    
    continuar = input("Deseja continuar? (s/n): ").strip().lower()

print("Fim do programa. Obrigado por visitar!\n")