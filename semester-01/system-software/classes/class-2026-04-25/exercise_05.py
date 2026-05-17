# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números ÍMPARES no vetor impar. Imprima os três vetores.

print("\n-- Processamento de 20 números inteiros, armazenamento em vetores e impressão de resultado para usuário --\n")

vetor_numeros = []
vetor_impar = []
vetor_par = []

for i in range(1,21):
    numero = int(float(input(f"Digite o {i}° número: ").replace(' ', '').replace(',', '.')))

    vetor_numeros.append(numero)

    if numero % 2 == 0:
        vetor_par.append(numero)
    else:
        vetor_impar.append(numero)

print(f"""
-- Resultados --
          
Números: {vetor_numeros}
Ímpares: {vetor_impar}
Pares: {vetor_par}
""")

print("Fim do programa. Obrigado por visitar!\n")