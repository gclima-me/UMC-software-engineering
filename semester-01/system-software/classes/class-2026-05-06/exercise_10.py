import random

# Autor: Guilherme Caetano Lima
# Exercício 10: Jogo de Craps. Faça um programa que implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. 
# Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. 
# Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10, este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. 
# Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

def lancar_dados():
    return random.randint(1, 6) + random.randint(1, 6)

print("\n-- Entrada de comando para lançar dados, processamento de regras de craps e impressão de resultado para usuário --")

while True:
    input("\nPressione Enter para lançar os dados...")
    soma = lancar_dados()
    print(f"Você tirou: {soma}")

    if soma == 7 or soma == 11:
        print("Resultado: Você é um 'Natural' e GANHOU!")
    elif soma in [2, 3, 12]:
        print("Resultado: Isso é um 'Craps' e você PERDEU!")
    else:
        ponto = soma
        print(f"Resultado: Seu PONTO é {ponto}. Tente tirá-lo novamente antes de tirar um 7.")
        while True:
            input("Lançar dados novamente (Enter)...")
            novo = lancar_dados()
            print(f"Tirou: {novo}")
            if novo == ponto:
                print("Resultado: Você tirou seu Ponto novamente! GANHOU!")
                break
            elif novo == 7:
                print("Resultado: Você tirou 7 antes do Ponto! PERDEU!")
                break

    if input("\nDeseja jogar uma nova partida? (s/n): ").strip().lower() != 's':
        break

print("\nFim do programa. Obrigado por visitar!\n")