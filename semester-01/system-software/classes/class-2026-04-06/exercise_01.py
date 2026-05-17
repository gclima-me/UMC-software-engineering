# Calculadora de idade
nome = input("Digite o seu nome: ")
sobrenome = input("Digite o seu sobrenome: ")
ano = int(input("Digite o ano do seu nascimento: "))
anoAtual = int(input("Digite o ano atual: "))
idade = anoAtual - ano
print(f"\nOlá {nome} {sobrenome}, a sua idade é: {idade}.")