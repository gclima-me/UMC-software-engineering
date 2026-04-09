# Ler dois valores para as variáveis A e B e efetuar a troca dos valores de forma que a variável Apasse a possuir o valor da variável B e a variável B passe a possuir o valor da variável A. Apresentaros valores após a efetivação do processamento da troca.

# Autor: Guilherme Caetano Lima

a = input('-- Efetuar a troca de valores entre 2 variáveis --\n\nDigite o valor de A: ')

b = input('Digite o valor de B: ')

c = a

a = b

b = c

print(f'\nAgora os valores de A e B foram trocados, veja:\n\nValor de A: {a}.\nValor de B: {b}.')