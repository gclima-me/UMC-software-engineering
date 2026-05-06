# Autor: Guilherme Caetano Lima
# Exercício 13: Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. 
# Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. 

def desenhar_moldura(l, c):
    if l < 1: l = 1
    if l > 20: l = 20
    if c < 1: c = 1
    if c > 20: c = 20

    print('+' + '-' * c + '+')
    
    for i in range(l):
        print('|' + ' ' * c + '|')
        
    print('+' + '-' * c + '+')

print("\n-- Entrada de números de linhas e colunas, processamento de desenho de moldura e impressão de resultado para usuário --")

while True:
    lin = int(input("\nDigite a quantidade de linhas (1-20): "))
    col = int(input("Digite a quantidade de colunas (1-20): "))

    print()
    desenhar_moldura(lin, col)

    if input("\nDeseja continuar? (s/n): ").strip().lower() != 's':
        break

print("\nFim do programa. Obrigado por visitar!\n")