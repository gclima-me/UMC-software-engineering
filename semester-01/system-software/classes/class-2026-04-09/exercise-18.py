# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

print("-- Entrada de tamanho de arquivo e velocidade da internet, processamento de tempo de donwload e impressão de resultado --")

continuar = "s"

while "s" in continuar:
    tamArquivo = float(input(f"\nDigite o tamanho do arquivo (MB): ").replace(' ', '').replace(',', '.'))
    velInternet = float(input("Digite a velocidade da internet (Mbps): ").replace(' ', '').replace(',', '.'))

    segundos = tamArquivo / velInternet
    minutos = int(segundos / 60)
    convMinutosSegundos = minutos * 60
    restSegundos = segundos - convMinutosSegundos

    print(f"""
Resumo de Download:

Tamanho do arquivo (MB): {tamArquivo:,g} MB.
Velocidade da Internet: {velInternet:,g} Mbps.
Tempo de Download: {minutos} Minutos e {restSegundos:,g} Segundos.
""")
    
    continuar = input("Deseja continuar? (s/n): ").strip().lower()

print("\nFim do programa. Obrigado por visitar!")