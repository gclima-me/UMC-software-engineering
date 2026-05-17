# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: 
#       F - Feminino 
#       M - Masculino 
#       Sexo Inválido. 

print("\n-- Entrada de letra, verificação se a letra é valida para os parâmetros estabelecidos ou não e impressão de resultado para usuário --")

continuar = "s"

while "s" in continuar:
    letra = input("\nDigite o seu sexo (M/F): ").strip().upper()

    if letra == "M":
        confirmar = input("\nVocê selecionou seu sexo como Masculino.\n\nConfirmar escolha? (s/n): ").strip().lower()
        if confirmar == "s":
            print("\nSeu sexo foi registrado como Masculino.")
        else:
            continue
        
    elif letra == "F":
        confirmar = input("\nVocê selecionou seu sexo como Feminino.\n\nConfirmar escolha? (s/n): ").strip().lower()
        if confirmar == "s":
            print("\nSeu sexo foi registrado como Feminino.")
        else:
            continue

    else:
        print('\nO sexo digitado é inválido. Digite apenas "M" para Masculino ou "F" para Feminino.')

    continuar = input("\nDeseja continuar? (s/n): ").strip().lower()

print("\nFim do programa. Obrigado por visitar!\n")