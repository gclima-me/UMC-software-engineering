# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa, utilizando while e listas, que permita o usuário realizar o cadastro de um número inderteminado de pessoas enquanto quiser e mostre na tela ao finalizar.

print("-- Entrada de nomes de funcionário, inserção de nomes de funcionários en lista e impressão  --")

while True:
    lista_funcionarios = []
    contador = 1

    print("\nDigite 0 para encerrar o cadastro!\n")

    while True:
        nome = input(f"Funcionário {contador}: ").strip()

        if nome == '0':
            break
        elif not nome or any(caractere.isdigit() for caractere in nome):
            print("\nERRO: O nome não pode conter números ou estar vazio.\n")
        else:
            lista_funcionarios.append(nome)
            contador += 1

    if input(f"""
Funcionários: {lista_funcionarios}

Os nomes estão corretos? (s/n): """).strip().lower() == 's':
        print("\nFuncionários cadastrados com sucesso!\n")
    else:
        continue

    if input("Deseja cadastrar mais funcionários? [s/n]: ").strip().lower() != 's':
        break

print("\nFim do programa. Obrigado por visitar!\n")