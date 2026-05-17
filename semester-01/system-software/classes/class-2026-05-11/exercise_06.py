# Autor: Guilherme Caetano Lima
# Exercício: Um aplicativo simples de lista de compras deve permitir ao usuário adicionar, remover e visualizar itens usando um menu de opções em loop.

print("\n-- Entrada de ação, veirifcação do que fazer e impressão de resultado para usuário --")

lista_compras = []

while True:
    try:
        acao = int(input("""
-- Lista de Compras --
                 
O que você deseja fazer?
                 
1 - Adicionar item
2 - Remover item pelo nome
3 - Listar todos os itens com numeração
4 - Sair

Resposta: """))
        
        if acao == 1:
            item = input("\nDigite o nome do item a ser adicionado: ").strip()
            lista_compras.append(item)

        elif acao == 2:
            while True:
                item = input("\nDigite o nome do item a ser removido: ").strip()
                if not item in lista_compras:
                    if input("\nERRO: O item não existe na lista.\nDeseja tentar novamente? [s/n]: ").strip().lower() != 's':
                        break
                else:
                    lista_compras.remove(item)
                    break

        elif acao == 3:
            print("\nListando todos os itens:\n")
            for i, item in enumerate(lista_compras):
                print(f"{i + 1}. {item}")
            
        elif acao == 4:
            break
        else:
            print("\nERRO: Digite uma opção válida.")
            
    except ValueError:
        print("\nERRO: Entrada inválida. Por favor, digite apenas números para as opções do menu.")

print("\nFim do programa. Obrigado por visitar!\n")