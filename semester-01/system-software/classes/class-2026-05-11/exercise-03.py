# Autor: Guilherme Caetano Lima
# Exercício: Uma loja precisa de um sistema simples para registrar entradas e saídas de produtos no estoque enquanto o usuário desejar continuar.

print("\n-- Entrada de ação, verificação do que executar e impressão de resultado para usuário --")

un_estoque = 100

while True:

    acao = input(f"""
------------------------------------------
Atualmente, temos {un_estoque} unidades no estoque.
O que deseja fazer?

A - Adicionar unidade
R - Remover unidade
PA - Adicionar valor personalizado
PR - Remover valor personalizado
Sair - Encerrar programa

Resposta: """).strip().lower()
    
    if acao == 'a':
        un_estoque += 1
        print("\n1 Unidade adicionada ao estoque!")
        
    elif acao == 'r':
        un_estoque -= 1
        print("\n1 Unidade removida do estoque!")

    elif acao == 'pa':
        try:
            num = int(input("\nDigite o número de unidades para adicionar: "))
            un_estoque += num
            print(f"\n{num} Unidades adicionadas do estoque!")
        except ValueError:
            print("\nERRO: Digite apenas números inteiros.")
            continue

    elif acao == 'pr':
        try:
            num = int(input("\nDigite o número de unidades para remover: "))
            un_estoque -= num
            print(f"\n{num} Unidades removidas do estoque!")
        except ValueError:
            print("\nERRO: Digite apenas números inteiros.")
            continue

    elif acao == 'sair':
        break
    
    else:
        print("\nERRO: Digite uma opção válida.")

    if un_estoque < 0:
        un_estoque = 0

print("\nFim do programa. Obrigado por visitar!\n")