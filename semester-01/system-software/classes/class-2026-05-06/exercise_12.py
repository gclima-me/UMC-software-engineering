import random

# Autor: Guilherme Caetano Lima
# Exercício 12: Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os caracteres embaralhados. 
# Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.

def embaralhar(palavra):
    palavra = palavra.upper()

    letras = []
    for caractere in palavra:
        letras.append(caractere)
    
    random.shuffle(letras)
    
    resultado = ""
    for letra in letras:
        resultado = resultado + letra
        
    return resultado

print("\n-- Entrada de palavra de texto, processamento de embaralhamento de caracteres e impressão de resultado para usuário --")

while True:
    p = input("\nDigite a palavra que deseja embaralhar: ").strip()

    resultado = embaralhar(p)
    print(f"Resultado embaralhado: {resultado}")

    if input("\nDeseja continuar? (s/n): ").strip().lower() != 's':
        break

print("\nFim do programa. Obrigado por visitar!\n")