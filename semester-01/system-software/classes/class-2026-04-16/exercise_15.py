# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é equilatero, isósceles ou escaleno. Dicas:

#       Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#       Triângulo Equilátero: três lados iguais;
#       Triângulo Isósceles: quaisquer dois lados iguais;
#       Triângulo Escaleno: Três lados diferentes.

print("\n-- Entrada de três lados de um triângulo, verificação de tipo de triângulo e impressão de resultado para usuário --")

continuar = "s"

while "s" in continuar:
    unidade_medida = input("\nDigite a sigla da unidade de medida do triângulo (m, cm, mm): ").strip().lower()
    lado1 = float(input(f"Digite o primeiro lado do triângulo ({unidade_medida}): ").replace(' ', '').replace(',', '.'))
    lado2 = float(input(f"Digite o segundo lado do triângulo ({unidade_medida}): ").replace(' ', '').replace(',', '.'))
    lado3 = float(input(f"Digite o terceiro lado do triângulo ({unidade_medida}): ").replace(' ', '').replace(',', '.'))

    # Verificando se é um triângulo ou não e se é um Equilátero
    if lado1 == lado2 == lado3:
        mensagem_tipo = "Triângulo Equilátero."

    elif lado1 > lado2 and lado1 > lado3:
        if (lado2 + lado3) >= lado1:
            mensagem_tipo = "Verificar"
        else:
            mensagem_tipo = "Não é um triângulo."
    
    elif lado2 > lado1 and lado2 > lado3:
        if (lado1 + lado3) >= lado2:
            mensagem_tipo = "Verificar"
        else:
            mensagem_tipo = "Não é um triângulo."

    elif lado3 > lado1 and lado3 > lado2:
        if (lado1 + lado2) >= lado3:
            mensagem_tipo = "Verificar"
        else:
            mensagem_tipo = "Não é um triângulo."

    # Verificação do tipo do triângulo caso não identificado
    if mensagem_tipo == "Verificar":
        if lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            mensagem_tipo= "Triângulo Isósceles."
        else:
            mensagem_tipo = "Triângulo Escaleno."

    print(f"""
Resumo do Triângulo
          
Lado 1: {lado1:,g}{unidade_medida}.
Lado 2: {lado2:,g}{unidade_medida}.
Lado 3: {lado3:,g}{unidade_medida}.

Tipo do Triângulo: {mensagem_tipo}
""")
    
    continuar = input("Deseja continuar? (s/n): ").strip().lower()

print("\nFim do programa. Obrigado por visitar!\n")