# Autor: Guilherme Caetano Lima
# Exercício 14: Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. 

def verificar_magico(q):

    soma_l1 = q[0] + q[1] + q[2]
    soma_l2 = q[3] + q[4] + q[5]
    soma_l3 = q[6] + q[7] + q[8]
    
    soma_c1 = q[0] + q[3] + q[6]
    soma_c2 = q[1] + q[4] + q[7]
    soma_c3 = q[2] + q[5] + q[8]
    
    soma_d1 = q[0] + q[4] + q[8]
    soma_d2 = q[2] + q[4] + q[6]
    
    if soma_l1 == 15 and soma_l2 == 15 and soma_l3 == 15 and \
       soma_c1 == 15 and soma_c2 == 15 and soma_c3 == 15 and \
       soma_d1 == 15 and soma_d2 == 15:
        return True
    else:
        return False

print("\n-- Entrada de nove números inteiros, processamento de verificação mágica e impressão de resultado para usuário --")

while True:
    print("\nDigite os 9 números (de 1 a 9) para o quadrado:")
    lista_numeros = []
    
    for i in range(9):
        valor = int(input(f"Posição {i+1}: "))
        lista_numeros.append(valor)

    if verificar_magico(lista_numeros):
        print("\nResultado: É um quadrado mágico!")
    else:
        print("\nResultado: Não é um quadrado mágico.")

    if input("\nDeseja continuar? (s/n): ").strip().lower() != 's':
        break

print("\nFim do programa. Obrigado por visitar!\n")