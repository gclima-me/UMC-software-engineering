# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que calcule as raízes de uma equação do segundo grau, na formula ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

#       Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve pedir os demais valores, mas sim ser encerrado;
#       Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao usuário e encerre o programa;
#       Se o delta calculado for igual a zero, a equação possui apenas uma raiz real. Informe ao usuário;
#       Se o delta fo

print("\n-- Entrada de a, b e c, verificação de delta e processamento de raízes e impressão de resultado para usuário --")

continuar = "s"

while "s" in continuar:
    a = float(input("\nDigite o valor de a: ").replace(' ', '').replace(',', '.'))

    if a == 0:
        mensagem_valores = f"a = {a:,g}."
        mensagem_resultado = "Essa não é uma equação do segundo grau."
    else:
        b = float(input("Digite o valor de b: ").replace(' ', '').replace(',', '.'))
        c = float(input("Digite o valor de c: ").replace(' ', '').replace(',', '.'))

        mensagem_valores = f"a = {a:,g}.\nb = {b:,g}.\nc = {c:,g}."

        delta = (b**2) - (4 * a * c)

        if delta < 0:
            mensagem_resultado  = f"Delta: {delta:,g}. A equação não possui raízes reais."
        elif delta == 0:
            raiz = -b / (2 * a)
            mensagem_resultado = f"Raiz única: {raiz:,g}"
        else:
            raiz1 = (-b + (delta**0.5)) / (2 * a)
            raiz2 = (-b - (delta**0.5)) / (2 * a)
            mensagem_resultado = f"Raiz 1: {raiz1:,g}.\nRaiz 2: {raiz2:,g}."

    print(f"""
Resumo de resultados
          
{mensagem_valores}

{mensagem_resultado}
""")
    
    continuar = input("Deseja continuar? (s/n): ").strip().lower()

print("\nFim do programa. Obrigado por visitar!\n")