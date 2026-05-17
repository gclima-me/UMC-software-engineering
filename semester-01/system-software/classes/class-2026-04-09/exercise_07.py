# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

print ("-- Entrada de lado de quadrado em metros, centímetros ou milímetros, processamento de área e dobro desta área e impressão de dobro da área para usuário --")

continuar = "s"

while "s" in continuar:
    exibir = True
    opcao = input("""
Digite uma das opções a seguir:
1 - Lado do quadrado em metros
2 - Lado do quadrado em centímetros
3 - Lado do quadrado em milímetros
Opção: """).strip()
    
    if opcao == "1":
        lado = float(input("\nDigite o lado do quadrado (metros): ").replace(' ', '').replace(',', '.'))
        medida = "metro(s)"

    elif opcao == "2":
        lado = float(input("\nDigite o lado do quadrado (centímetros): ").replace(' ', '').replace(',', '.'))
        medida = "centímetro(s)"

    elif opcao == "3":
        lado = float(input("\nDigite o lado do quadrado (milímetros): ").replace(' ', '').replace(',', '.'))
        medida = "milímetro(s)"

    else:
        print("\nERRO: Digite uma opção válida (apenas 1, 2 ou 3).")
        exibir = False
        continue
    
    if exibir == True:
        area = lado ** 2
        print(f"""
Resumo do quadrado:
Lado do quadrado: {lado:,g} {medida}.
Área do quadrado: {area:,g} {medida} quadrado(s).
Dobro da área do quadrado: {area * 2:,g} {medida} quadrados.
""")

    continuar = input("Deseja continuar? (s/n): ").strip().lower()

print("\nFim do programa. Obrigado por visitar!")