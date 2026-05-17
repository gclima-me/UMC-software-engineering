# Autor: Guilherme Caetano Lima
# Exercício 01: Faça um programa para gerar os n primeiros termos da sequência:
#       1 1 2 3 5 8 13 21 ...

print("\n-- Processamento de sequência de Fibonacci e impressão de resultado para usuário --")

anterior = 1
atual = 1

while anterior <= 21:
    print(anterior, end=" ")
    
    proximo = anterior + atual
    anterior = atual
    atual = proximo