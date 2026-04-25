# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que leia 5 números e informe o maior número.

print("-"*50)
print("Entrada de quantidade de números, verificação do maior e menor número e impressão de resultado para usuário")
print("-"*50)
print("")

while True:
    lista_numeros = []

    for i in range(1, 6):
        num = float(input(f"Digite o {i}° número: ").replace(' ', '').replace(',', '.'))
        lista_numeros.append(num)

    maior_num = max(lista_numeros)
    menor_num = min(lista_numeros)
    quantidade_num = len(lista_numeros)

    print(f"""
Resumo de informações
          
Números digitados: {lista_numeros}
Quantidade de números: {quantidade_num:,g}

Maior número: {maior_num:,g}
Menor número: {menor_num:,g}
""")
    
    continuar = input("Deseja continuar? (s/n): ").strip().lower()
    if continuar != 's':
        break

print("\nFim do programa. Obrigado por visitar!\n")