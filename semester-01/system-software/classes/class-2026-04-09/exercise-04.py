# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que peça as 4 notas bimestrais e mostre a média.

print("-- Entrada de nome e notas bimestrais, processamento de média e impressão de média para usuário --")

continuar = "s"

while "s" in continuar:
    aluno = input("\nDigite o nome do aluno: ").strip()
    nota1 = float(input("Digite a 1° nota do(a) aluno: ").replace(' ', '').replace(',', '.'))
    nota2 = float(input("Digite a 2° nota do(a) aluno: ").replace(' ', '').replace(',', '.'))
    nota3 = float(input("Digite a 3° nota do(a) aluno: ").replace(' ', '').replace(',', '.'))
    nota4 = float(input("Digite a 4° nota do(a) aluno: ").replace(' ', '').replace(',', '.'))
     
    media = (nota1 + nota2 + nota3 + nota4) / 4
     
    if media >= 7:
        situacao = "Aprovado(a) :)"

    elif media >= 5:
        situacao = "Recuperação :|"
        
    else:
        situacao = "Reprovado(a) :("

    print(f"""
Resumo do(a) {aluno}:

1° Nota: {nota1:g}.
2° Nota: {nota2:g}.
3° Nota: {nota3:g}.
4° Nota: {nota4:g}.

Média final: {media:g}.
Situação: {situacao}
""")
    
    continuar = input("Deseja continuar? (s/n): ").strip().lower()

print("\nFim do programa. Obrigado pela visita!")