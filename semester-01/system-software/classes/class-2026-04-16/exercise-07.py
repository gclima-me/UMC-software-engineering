# Autor: Guilherme
# Exercício: Faça um programa que leia 3 números e mostre o maior e o menor deles.

print("\n-- Entrada de 3 números, verificação do maior e menor número e impressão de resultado para usuaŕio --")

continuar = "s"

while "s" in continuar:
    num1 = float(input("\nDigite o primeiro número: ").replace(' ', '').replace(',', '.'))
    num2 = float(input("Digite o segundo número: ").replace(' ', '').replace(',', '.'))
    num3 = float(input("Digite o terceiro número: ").replace(' ', '').replace(',', '.'))

    # Verificação dos maiores números (se houver)
    if num1 == num2 == num3:
        mensagem_maior_num = f"Todos os números são iguais a {num1:,g}. Não há um maior número."

    elif num1 == num2:
        if num3 > num1:
            mensagem_maior_num = f"O maior número é: Número 3 ({num3:,g})."
        else:
            mensagem_maior_num = f"Os maiores números são: Número 1 ({num1:,g}) e Número 2 ({num2:,g})."
        
    elif num2 == num3:
        if num1 > num2:
            mensagem_maior_num = f"O maior número é: Número 1 ({num1:,g})."
        else:
            mensagem_maior_num = f"Os maiores números são: Número 2 ({num2:,g}) e Número 3 ({num3:,g})."

    elif num1 == num3:
        if num2 > num1:
            mensagem_maior_num = f"O maior número é: Número 2 ({num2:,g})."
        else:
            mensagem_maior_num = f"Os maiores números são: Número 1 ({num1:,g}) e Número 3 ({num3:,g})."

    elif num1 > num2 and num1 > num3:
        mensagem_maior_num = f"O maior número é: Número 1 ({num1:,g})."

    elif num2 > num1 and num2 > num3:
        mensagem_maior_num = f"O maior número é: Número 2 ({num2:,g})."

    elif num3 > num1 and num3 > num2:
        mensagem_maior_num = f"O maior número é: Número 3 ({num3:,g})."

# Verificação dos menores números (se houver)
    if num1 == num2 == num3:
        mensagem_menor_num = f"Todos os números são iguais a {num1:,g}. Não há um menor número."

    elif num1 == num2:
        if num3 < num1:
            mensagem_menor_num = f"O menor número é: Número 3 ({num3:,g})."
        else:
            mensagem_menor_num = f"Os menores números são: Número 1 ({num1:,g}) e Número 2 ({num2:,g})."
        
    elif num2 == num3:
        if num1 < num2:
            mensagem_menor_num = f"O menor número é: Número 1 ({num1:,g})."
        else:
            mensagem_menor_num = f"Os menores números são: Número 2 ({num2:,g}) e Número 3 ({num3:,g})."

    elif num1 == num3:
        if num2 < num1:
            mensagem_menor_num = f"O menor número é: Número 2 ({num2:,g})."
        else:
            mensagem_menor_num = f"Os menores números são: Número 1 ({num1:,g}) e Número 3 ({num3:,g})."

    elif num1 < num2 and num1 < num3:
        mensagem_menor_num = f"O menor número é: Número 1 ({num1:,g})."

    elif num2 < num1 and num2 < num3:
        mensagem_menor_num = f"O menor número é: Número 2 ({num2:,g})."

    elif num3 < num1 and num3 < num2:
        mensagem_menor_num = f"O menor número é: Número 3 ({num3:,g})."

    print(f"""
Resumo dos números
          
Número 1: {num1:,g}.
Número 2: {num2:,g}.
Número 3: {num3:,g}.

{mensagem_maior_num}
{mensagem_menor_num}
""")
    
    continuar = input("Deseja continuar? (s/n): ").strip().lower()

print("\nFim do programa. Obrigado por visitar!\n")