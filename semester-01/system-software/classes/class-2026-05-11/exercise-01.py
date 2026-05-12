IDADE_MINIMA = 16
IDADE_MAXIMA = 60
ALTURA_MINIMA = 1.0
ALTURA_MAXIMA = 2.5

# Autor: Guilherme Caetano Lima
# Exercício: Crie um programa para validar o cadastro de um aluno.

print("\n-- Entrada de nome, idade e altura de aluno(a), verificação de se os dados estão corretos e impressão de resultado para usuário --")

while True:
    nome = input("\nDigite o nome do(a) aluno(a): ").strip()

    if not nome or any(c.isdigit() for c in nome):
        print("\nERRO: O nome não pode estar vazio ou conter números.")
        continue

    try:
        idade = int(input("Digite a idade do(a) aluno(a): "))
        altura = float(input("Digite a altura do(a) aluno(a): ").replace(',', '.'))

    except ValueError:
        print("\nERRO: Digite apenas números.")
        continue

    if IDADE_MINIMA <= idade <= IDADE_MAXIMA and ALTURA_MINIMA <= altura <= ALTURA_MAXIMA:
        matriculado = "Sim"
    else:
        matriculado = "Não"

    print(f"""
-- Resumo de Cadastro --
          
Nome: {nome}
Idade: {idade}
Altura {altura:.,2f}

Matriculado: {matriculado}
""")
    
    if input("Deseja matricular mais alunos? [s/n]: ").strip().lower() != 's':
        break

print("\nFim do programa. Obrigado por visitar!\n")