# Autor: Guilherme Caetano Lima
# Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes e Kilobytes, usando as seguintes fórmulas:
#       Para Megabytes: Gigabytes * 1024
#       Para Kilobytes: Gigabytes * 1024 * 1024

print("-- Entrada de tamanho de arquivo em Gigabytes, processamento de conversão para Megabytes e Kilobytes e impressão de resultados para usuário --")

continuar = "s"

while "s" in continuar:
    exibir = True

    opcao = input(f"""
Escolha uma das opções a seguir:
1 - GB para MB
2 - GB para KB
3 - MB para GB
4 - MB para KB
5 - KB para GB
6 - KB para MB
Opção: """).strip()
    
    if opcao == "1":
        tamArquivo = float(input("\nDigite o tamanho do arquivo (GB): ").replace(' ', '').replace(',', '.'))
        conversao = tamArquivo * 1024
        medArquivo = "GB"
        medConversao = "MB"

    elif opcao == "2":
        tamArquivo = float(input("\nDigite o tamanho do arquivo (GB): ").replace(' ', '').replace(',', '.'))
        conversao = tamArquivo * 1024 * 1024
        medArquivo = "GB"
        medConversao = "KB"

    elif opcao == "3":
        tamArquivo = float(input("\nDigite o tamanho do arquivo (MB): ").replace(' ', '').replace(',', '.'))
        conversao = tamArquivo / 1024
        medArquivo = "MB"
        medConversao = "GB"

    elif opcao == "4":
        tamArquivo = float(input("\nDigite o tamanho do arquivo (MB): ").replace(' ', '').replace(',', '.'))
        conversao = tamArquivo * 1024
        medArquivo = "MB"
        medConversao = "KB"

    elif opcao == "5":
        tamArquivo = float(input("\nDigite o tamanho do arquivo (KB): ").replace(' ', '').replace(',', '.'))
        conversao = tamArquivo / 1024 / 1024
        medArquivo = "KB"
        medConversao = "GB"

    elif opcao == "6":
        tamArquivo = float(input("\nDigite o tamanho do arquivo (KB): ").replace(' ', '').replace(',', '.'))
        conversao = tamArquivo / 1024
        medArquivo = "KB"
        medConversao = "MB"

    else:
        print("\nERRO: Digite uma opção válida (apenas de 1 a 6).")
        exibir = False

    if exibir == True:
        print(f"""
Resultado da conversão de {tamArquivo:,g} {medArquivo} para {medConversao}:

Tamanho do arquivo: {tamArquivo:,g} {medArquivo}.
Resultado da conversão para {medConversao}: {conversao:,g} {medConversao}.
""")
        
    continuar = input("\nDeseja continuar? (s/n): ").strip().lower()

print("\nFim do programa. Obrigado por visitar!")