# Autor: Guilherme Caetano Lima
# Exercício: Um professor quer um programa para gerar a tabuada de qualquer número, exibindo o resultado formatado em uma tabela simples no terminal.

print("\n-- Entrada de número de tabuada, processamento de tabuada do número com laço for e impressão de resultado para usuário --")

while True:
    tabuada = ""
    soma_total = 0

    try:
        num = int(input("\nDigite o número da tabuada: "))
    except ValueError:
        print("\nERRO: Digite apenas números inteiros.")
        continue

    for i in range(11):
        tabuada += f"{i} x {num} = {i * num}\n"
        soma_total += i * num

    print(f"""
-- Tabuada do {num} --

{tabuada}
Soma total: {soma_total}
""")
    
    if input("Deseja verificar mais alguma tabuada? [s/n]: ").strip().lower() != 's':
        break

print("\nFim do programa. Obrigado por visitar!\n")