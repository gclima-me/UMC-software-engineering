# Autor: Guilherme Caetano Lima
# Exercício 03: Crie um dicionário de um aluno e exiba suas informações.

print("\n-- Entrada de informações de aluno, inserção em dicionário e impressão de resultado para usuário --\n")

dicionario_aluno = {}

while True:
    # Validação do nome
    while True:
        entrada = input("Digite o Nome do(a) Aluno(a): ").strip()
        if not entrada or any(c.isdigit() for c in entrada):
            print("\nERRO: O nome não pode conter números ou estar vazio. Tente novamente.\n")
            continue
        dicionario_aluno["nome"] = entrada
        break

    # Validação do gênero
    while True:
        genero = input('Digite o Gênero ("M" para Masculino, "F" para Feminino ou "O" para Outro): ').strip().lower()
        if genero not in ['m', 'f', 'o']:
            print("\nERRO: Apenas os Gêneros Informados Acima Serão Aceitos. Tente novamente.\n")
            continue
        dicionario_aluno["genero"] = genero
        break

    # Validação da Idade
    while True:
        try:
            dicionario_aluno["idade"] = int(input("Digite a Idade: "))
            break
        except ValueError:
            print("\nERRO: Idade inválida. Digite apenas números inteiros.\n")

    # Validação da Série
    while True:
        try:
            serie = int(input("\nDigite a Série (Apenas entre 1 e 9): "))
            if serie < 1 or serie > 9:
                print("\nERRO: Apenas Valores entre 1 e 9 Serão Aceitos. Tente novamente.\n")
                continue
            dicionario_aluno["serie"] = serie
            break
        except ValueError:
            print("\nERRO: Série inválida. Digite apenas números inteiros.\n")

    # Validação do Ano de Ingresso
    while True:
        try:
            ano = int(input("Digite o Ano de Ingresso na Escola: "))
            if ano < 2000 or ano > 2026:
                print("\nERRO: Ano de Ingresso Inválido (Permitido Entre 2000 e 2026). Tente novamente.\n")
                continue
            dicionario_aluno["ano_ingresso"] = ano
            break
        except ValueError:
            print("\nERRO: Ano inválido. Digite apenas números inteiros.\n")

    # Exibição e confirmação dos dados
    print("\n-- Informações do(a) Aluno(a) --")
    for chave, valor in dicionario_aluno.items():
        print(f"{chave.title()}: {valor}")
        
    if input("\nAs Informações Acima Estão Corretas? [s/n]: ").strip().lower() == 's':
        if input("Deseja Cadastrar Mais Algum Aluno? [s/n]: ").strip().lower() != 's':
            break
        else:
            dicionario_aluno = {}

print("\nFim do programa. Obrigado por visitar!\n")