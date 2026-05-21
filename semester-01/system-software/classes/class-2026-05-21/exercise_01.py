# Autor: Guilherme Caetano Lima
# Exercício 01: Operação com dicionários, listas e bibliotecas

# ==========================================
# IMPORTS
# ==========================================
import locale
import os

# Formatação de moeda
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Limpar console
os.system("cls")


# ==========================================
# FUNÇÕES
# ==========================================
def soma(a, b):
    return a + b

def subt(a, b):
    print(a - b)

#def mult():
#    a = float(input("Digite o 1° número: ").replace(' ', '').replace(',', '.'))
#    b = float(input("Digite o 2° número: ")replace(',', '.'))
#    print(a + b)


# ==========================================
# ESTRUTURAS DE DADOS (DADOS INICIAIS)
# ==========================================
# definindo dicionário
salaries = {
    "Luiz": 14500,
    "Fulano": 9500,
    "Sicrano": 11000,
    "Beltrano": 13000
}

# Lista
my_list = ["Tomate", 15, "Abacaxi", 16]

# Dicionários
dictionary = {
    "Name": "Guilherme",
    "Age": 19,
    "Height": 1.75,
    "City": "Poá"
}

fruits = {
    "Apple": 2.75,
    "Tomato": 7.65,
    "Potato": 1.25,
    "Pineaple": 7,
    "Banana": 5.50
}

# Dicionário com chaves como "ID" e valores como listas
info = {
    111: ["Tomato", 15],
    112: ["Pineaple", 16],
    113: ["Orange", 17]
}

# Dicionario com ID e listas
students = {
    115: ["NOME", "CURSO", "IDADE"],
    116: ["Victor", "ENG SOFT", 25],
    117: ["Henrique", "ADS", 77],
    118: ["Hellen", "Medicina", 19],
    119: ["David", "SIS INFO", 23]
}


# ==========================================
# EXECUÇÃO E TESTES
# ==========================================

# Teste de Funções
print(soma(25, 25))

subt(25, 25)

#mult()

print()

# Imprimindo dictionary
print(dictionary)

print()

# Acessando chave
print(dictionary["Name"])

print()

# Imprimindo fruits
print(fruits)

print()

# Acessando chave
print(fruits["Pineaple"])

print()

# Verificando se uma chave existe na tabela
print("Age" in dictionary)

print()

# Acessando valores
print(dictionary.values())

print()

# Ordenando pela chave (sorted ordena por tamanho ou em ordem alfabética, reverse inverte a ordem)
for i in sorted(fruits, reverse = True):
    print(i, fruits[i])

print()

for i in sorted(fruits, reverse = False):
    print(i, fruits[i])

print()

# Manipulando dicionário
del fruits["Tomato"]
fruits["Pineaple"] = 175
print(fruits)

print()

# Manipulando dicionário
for i in salaries:
    salary = locale.currency(salaries[i], grouping = True, symbol = True)
    print(f"{i:15} {salary:<10}")

print()

# Deletando chaves no dicionário
del students[119]
students[118][2] = 21
print(students)

print()

# Método para desempacotamento de dados, organização de items em tabela
for key, data in students.items():
    print(f'{key:^10} {data[0]:^15} {data[1]:^10} {data[2]:^5}')

print()

# Adicionando chave e valor no dicionário
students[120] = ["Fernando", "Odontologia", 27]

print()

# Verificando existência de chave dentro do dicionário
while True:
    val = int(input("\nDigite uma matrícula para ser pesquisada (ID): "))
    if val in students:
        print()
        print(val, students[val])
        break
    else:
        print("\nERRO: Matrícula não encontrada! Digite uma matrícula válida.\n")
        break

print()

# Limpando os dados de um dicionário com clear
students.clear()
print(students)

print()

# Incluindo e atualizando dicionário com update
students.update({0: ["Antonio", "ADS", 19]})
print(students)

print()

# Buscar valor, e caso não encontre, retorne "não encontrado"
print(students.get("Eduarda", "Não encontrado."))
print(students.get("Cláudio", "Não encontrado."))

print()


# ==========================================
# ESTUDO DE TUPLAS
# ==========================================
# Criando uma tupla (ao contrário de listas, tuplas não podem ser modificadas assim como constantes)
my_tuple = ("Tomato", 15)

#Tentando mudar valor da tupla
my_tuple[0] = "Arroz"

print(my_tuple)

print()