# Autor: Guilherme Caetano Lima
# Exercício 7: Crie uma calculadora que resolva as quatro operações (soma, subtração, multiplicação e divisão). O programa deve perguntar qual operação o usuário quer resolver, receber dois números, e efetuar a operação. Em seguida, o programa pergunta novamente qual operação deve ser resolvida. O programa só será finalizado quando o usuário pressionar uma tecla de finalização.

print("\n-- Entrada de operação e números, processamento de cálculo e impressão de resultado para usuário --")

while True:
    try:
        opcao = int(input("""
-- Operações Disponíveis --   
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Encerrar programa

Escolha a operação: """))

        if opcao == 5:
            break
        
        if opcao < 1 or opcao > 5:
            print("\nERRO: Opção inválida. Tente novamente.")
            continue

        while True:
            try:
                print()
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                break
            except ValueError:
                print("\nERRO: Digite apenas números.")
                continue

        if opcao == 1:
            print(f"\nResultado: {num1:,g} + {num2:,g} = {num1 + num2:,g}")
        elif opcao == 2:
            print(f"\nResultado: {num1:,g} - {num2:,g} = {num1 - num2:,g}")
        elif opcao == 3:
            print(f"\nResultado: {num1:,g} * {num2:,g} = {num1 * num2:,g}")
        elif opcao == 4:
            if num2 == 0:
                print("\nERRO: Divisão por zero não é permitida.")
            else:
                print(f"\nResultado: {num1:,g} / {num2:,g} = {num1 / num2:,g}")

    except ValueError:
        print("\nERRO: Digite apenas números.")
        continue

print("\nFim do programa. Obrigado por visitar!\n")