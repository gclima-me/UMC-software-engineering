# Autor: Guilherme Caetano Lima
# Exercício: Simule um caixa eletrônico básico que permita saques e depósitos, mantendo o saldo atualizado e registrando o histórico de operações em uma lista.

print("\n-- Entrada de ação, verificação do que fazer e impressão de resultado para usuário --")

saldo = 1000.00
extrato = []
logado = False
senha = "1234"

while True:
    tentativa = input("\nDigite sua senha para acessar o sistema: ").strip()
    
    if tentativa == senha:
        logado = True
        break
    else:
        print("\nSenha incorreta. Tente novamente.")

while logado:
    try:
        acao = int(input("""
-- Caixa Eletrônico --
                 
O que você deseja fazer?
                 
1 - Saque
2 - Depósito
3 - Extrato
4 - Sair

Resposta: """))
        
        if acao == 1:
            valor = float(input("\nDigite o valor do saque: ").replace(',', '.'))
            if valor > saldo:
                print(f"\nERRO: Saldo insuficiente.\nSaldo atual: R$ {saldo:,.2f}")
            elif valor <= 0:
                print("\nERRO: Valor de saque inválido.")
            else:
                saldo -= valor
                extrato.append(f"SAQUE: - R$ {valor:,.2f}")
                print(f"Saque de R$ {valor:,.2f} realizado.")

        elif acao == 2:
            valor = float(input("\nDigite o valor do depósito: ").replace(',', '.'))
            if valor > 0:
                saldo += valor
                extrato.append(f"DEPÓSITO: + R$ {valor:,.2f}")
                print(f"Depósito de R$ {valor:,.2f} realizado.")
            else:
                print("\nERRO: Valor de depósito inválido.")

        elif acao == 3:
            print("\nListando todas as movimentações:\n")
            if not extrato:
                print("Nenhuma transação encontrada.")
            else:
                for i, item in enumerate(extrato):
                    print(f"{i + 1}. {item}")
            print(f"\nSALDO ATUAL: R$ {saldo:,.2f}")
            
        elif acao == 4:
            break
        else:
            print("\nERRO: Digite uma opção válida.")

    except ValueError:
        print("\nERRO: Entrada inválida. Por favor, utilize apenas números.")

print("\nFim do programa. Obrigado por visitar!\n")