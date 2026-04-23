# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo. Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:

#       326 = 3 centenas, 2 dezenas e 6 unidades
#       12 = 1 dezena e 2 unidades

print("\n-- Entrada de número inteiro menor que 1000, identificação de quantidade de centenas, dezenas e unidades e impressão de resultado para usuário --")

continuar = "s"

while "s" in continuar:
    num = int(float(input("\nDigite um número maior que 0 e menor que 1000: ").replace(' ', '').replace(',', '.')))

    if num >= 1000 or num < 0:
        saida = "\nERRO: Valor inválido. Insira apenas números maiores que 0 ou menores que 1000."
    else:
        centenas = num // 100
        dezenas = (num % 100) // 10
        unidades = num % 10

        if centenas > 0:
            texto_centenas = f"\n{centenas} Centena, " if centenas == 1 else f"\n{centenas} Centenas, "
        else:
            texto_centenas = "\n"

        if dezenas > 0:
            texto_dezenas = f"{dezenas} Dezena e " if dezenas == 1 else f"{dezenas} Dezenas e "
        else:
            texto_dezenas = ""

        if unidades > 0:
            texto_unidades = f"{unidades} Unidade" if unidades == 1 else f"{unidades} Unidades."
        else:
            texto_unidades = ""

        saida = texto_centenas + texto_dezenas + texto_unidades

    print(saida)
    
    continuar = input("\nDeseja continuar: (s/n): ").strip().lower()

print("\nFim do programa. Obrigado por visitar!\n")