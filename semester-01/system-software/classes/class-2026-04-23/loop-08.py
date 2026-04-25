# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que leia 5 números e informe a soma e a média dos números.

print("-"*50)
print("Entrada de números, processamento de soma e média e impressão de resultado para usuário")
print("-"*50)
print("")

while True:
    numeros = []

    for i in range(1, 6):
        num = float(input(f"Digite o {i}° número: ").replace(' ', '').replace(',', '.'))
        numeros.append(num)
    
    soma = sum(numeros)
    quantidade = len(numeros)
    media = soma / quantidade

    print(f"""
Resumo de informações
          
Números digitados: {numeros}
Quantidade de números: {quantidade}
Soma de todos os números: {soma:,g}

Média: {media:,g}
""")
    
    continuar = input("Deseja continuar? (s/n): ").strip().lower()
    if continuar != 's':
        break

print("\nFim do programa. Obrigado por usar!\n")