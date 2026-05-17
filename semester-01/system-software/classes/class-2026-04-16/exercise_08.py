# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

print("\n-- Entrada de três preços de produtos, verificação do mais barato e impressão de resultado para usuário --")

continuar = "s"

while "s" in continuar:
    valor_produto1 = float(input("\nDigite o preço do produto 1 (apenas números): ").replace(' ', '').replace(',', '.'))
    valor_produto2 = float(input("Digite o preço do produto 2 (apenas números): ").replace(' ','').replace(',', '.'))
    valor_produto3 = float(input("Digite o preço do produto 3 (apenas números): ").replace(' ', '').replace(',', '.'))

    if valor_produto1 == valor_produto2 == valor_produto3:
        mensagem_escolha = f"Todos os produtos tem o mesmo preço e custam R$ {valor_produto1:,.2f}. Escolha o de sua preferência."

    elif valor_produto1 < valor_produto2:
        if valor_produto1 < valor_produto3:
            mensagem_escolha = f"Melhor escolha (menor preço): Produto 1 por R$ {valor_produto1:,.2f}."
        else:
            mensagem_escolha = f"Melhor escolha (menor preço): Produto 3 por R$ {valor_produto3:,.2f}."
    
    elif valor_produto2 < valor_produto3:
        mensagem_escolha = f"Melhor escolha (menor preço): Produto 2 por R$ {valor_produto2:,.2f}."

    else:
        mensagem_escolha = f"Melhor escolha (menor preço): Produto 3 por R$ {valor_produto3:,.2f}."

    print(f"""
Resumo dos produtos:
          
Preço do produto 1: R$ {valor_produto1:,.2f}.
Preço do produto 2: R$ {valor_produto2:,.2f}.
Preço do produto 3: R$ {valor_produto3:,.2f}.

{mensagem_escolha}
""")
    
    continuar = input("Deseja continuar? (s/n): ").strip().lower()

print("\nFim do programa. Obrigado por visitar!\n")