# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que leia e valide as seguintes informações:

#       Nome: maior que 3 caracteres;
#       Idade: entre 0 e 150;
#       Salário: maior que zero;
#       Estado Civil: 's', 'c', 'v', 'd';

print("-"*50)
print("Entrada de informações, verificação se são válidas ou inválidas e impressão de resultado para usuário")
print("-"*50)

while True:
    nome = ""
    while len(nome) <= 3:
        nome = input("\nDigite o seu nome (pelo menos 4 caracteres): ").strip()
        if len(nome) <= 3:
            print("\nERRO: Nome menor que 4 caracteres. Tente novamente).")

    idade = -1
    while idade < 0 or idade > 150:
        idade = int(float(input("\nDigite a sua idade (entre 0 e 150): ").replace(',', '.')))
        if idade < 0 or idade > 150:
            print("\nERRO: Sua idade deve estar entre 0 e 150. Tente novamente")

    salario = 0
    while salario <= 0:
        salario = float(input("\nDigite o seu salário (maior que 0): ").replace(' ', '').replace(',', '.'))
        if salario <= 0:
            print("\nERRO: Seu salário deve ser maior que 0. Tente novamente")

    estado_civil = ""
    while True:
        estado_civil = input("\nEstado Civil [s, c, v, d]: ").lower().strip()
        if estado_civil in ['s', 'c', 'v', 'd']:
            break
        else:
            print("\nERRO: Estado civil inválido. Tente novamente.")

    confirmar_cadastro = input(f"""
Resumo de dados preenchidos

Nome: {nome}
Idade {idade}
Salário: R$ {salario:,.2f}
Estado civil: {estado_civil}

Confirmar cadastro? (s/n): """).strip().lower()
    if confirmar_cadastro != 's':
        continue
    else:
        print("\nCadastro realizado com sucesso!")

    continuar = input("\nDeseja cadastrar novo usuário? (s/n): ").strip().lower()
    if continuar != 's':
        break

print("\nFim do programa. Obrigado por usar!\n")