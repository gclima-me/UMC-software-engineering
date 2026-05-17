# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa, utilizando while, que permita o usuário fazer contas de adição enquanto quiser.

def adicao(n1, n2):
    r = f"{n1:,g} + {n2:,g} = {n1+n2:,g}"
    return r

def subtracao(n1, n2):
    r = f"{n1:,g} - {n2:,g} = {n1-n2:,g}"
    return r

def multiplicacao(n1, n2):
    r = f"{n1:,g} * {n2:,g} = {n1*n2:,g}"
    return r

def divisao(n1, n2):
    r = f"{n1:,g} / {n2:,g} = {n1/n2:,g}"
    return r

def potenciacao(n1, n2):
    r = f"{n1:,g}^{n2:,g} = {n1**n2:,g}"
    return r


print("\n-- Entrada de opção de cálculo matemático e dois números, processamento de cálculo matemático e impressão de resultado para usuário --")

while True:
    try:
        opcao = int(input("""
Digite a operação desejada:
1 - Adição
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Potenciação
Resposta: """))
        
        while True:
            try:
                if opcao == 1:
                    num1 = float(input("\nDigite o 1° número: ").replace(' ', '').replace(',', '.'))
                    num2 = float(input("Digite o 2° número: ").replace(' ', '').replace(',', '.'))
                    resultado = adicao(num1, num2)
                elif opcao == 2:
                    num1 = float(input("\nDigite o 1° número: ").replace(' ', '').replace(',', '.'))
                    num2 = float(input("Digite o 2° número: ").replace(' ', '').replace(',', '.'))
                    resultado = subtracao(num1, num2)
                elif opcao == 3:
                    num1 = float(input("\nDigite o 1° número: ").replace(' ', '').replace(',', '.'))
                    num2 = float(input("Digite o 2° número: ").replace(' ', '').replace(',', '.'))
                    resultado = multiplicacao(num1, num2)
                elif opcao== 4:
                    num1 = float(input("\nDigite o 1° número: ").replace(' ', '').replace(',', '.'))
                    num2 = float(input("Digite o 2° número: ").replace(' ', '').replace(',', '.'))
                    if num2 != 0:
                        resultado = divisao(num1, num2)
                    else:
                        print("\nERRO: Não existe divisão por 0. Tente novamente.\n")
                elif opcao == 5:
                    num1 = float(input("\nDigite o 1° número: ").replace(' ', '').replace(',', '.'))
                    num2 = float(input("Digite o 2° número: ").replace(' ', '').replace(',', '.'))
                    resultado = potenciacao(num1, num2)
                else:
                    print("\nERRO: Digite apenas uma das opções disponíveis acima (número inteiro).")
                    break

            except ValueError:
                print("\nERRO: Digite apenas números.")
                continue

            print(f"""
-- Resultado do cálculo --

{resultado}""")

            break

    except ValueError:
        print("\nERRO: Digite apenas uma das opções disponíveis acima (número inteiro).")

    if input("\nDeseja continuar? [s/n]\nResposta: ").strip().lower() != 's':
        break

print("\nFim do programa. Obrigado por visitar!\n")