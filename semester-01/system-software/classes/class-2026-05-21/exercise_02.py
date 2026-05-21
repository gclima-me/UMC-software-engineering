# Autor: Guilherme Caetano Lima
# Exercise: Implemente em Python o que se pede nos exercícios abaixo.

agenda = {
    "Ana": "9999-0001",
    "Carlos": "9999-0002",
    "Beatriz": "9999-0003",
    "Eduardo": "9999-0004",
    "Sérgio": "9999-0005"
}

# Exercício 1: Acesso por chave
#   Mostre o telefone de "Beatriz".

print(f"\nExibindo o Número da Beatriz: {agenda['Beatriz']}")

# Exercício 2: Alteração de valor
#   Troque o telefone de "Carlos" para "9999-1111".

print(f"\nExibindo o Número do Carlos Antes: {agenda['Carlos']}")

agenda["Carlos"] = "9999-1111"

print(f"\nExibindo o Número do Carlos Depois: {agenda['Carlos']}")

# Exercício 3: Inclusão de novo item
#   Adicione o contato "Voslano" com telefone "9999-2222".

agenda["Voslano"] = "9999-2222"

print(f'\nAdicionando o Contato "Voslano": {agenda["Voslano"]}')

# Exercício 4: Verificação de chave
#   Verifique se "Sérgio" está na agenda.

if "Sérgio" in agenda:
    print('\nO Contato "Sérgio" Está na Agenda!')
else:
    print('\nO Contato "Sérgio" Não Está na Agenda!')

# Exercício 5: Remoção de item
#   Remova o contato "Ana".

del agenda["Ana"]
print('\nA "Ana" foi Removida da Agenda!')
print(agenda)

# Exercício 6: Percorrer com for e items()
#   Mostre todos os contatos e seus telefones.

print("\nPercorrendo Todos os Contatos e seus Telefones...\n")
for chave, valor in agenda.items():
    print(f"{chave:^5} {valor:^5}")

# Exercício 7: Verificar se chave começa com letra específica
#   Mostre todos os contatos que começam com a letra "E".

print("\nExibindo Contatos que Começam com a Letra 'E':")
for nome in agenda:
    if nome.startswith("E"):
        print(f"{nome}: {agenda[nome]}")

# Exercício 8: Quantidade de contatos
#   Mostre quantos contatos existem na agenda.

print(f"\nQuantidade de Contatos na Agenda: {len(agenda)}")

# Exercício 9: Inclusão condicional
#   Peça ao usuário um nome. Se ele não estiver na agenda, peça o telefone e adicione.

print("\n-- Consulta de Contatos --")

while True:
    nome = input('\nDigite o Nome do Contato que Deseja Verificar (Digite "sair" para Encerrar): ').strip()

    if nome.lower() == "sair":
        print("\nConsulta de Contatos Encerrada.")
        break
        
    if not nome or any(c.isdigit() for c in nome):
        print("\nERRO: O Nome não pode Conter Números. Tente novamente.")
        continue
    
    if nome in agenda:
        print(f"\n{agenda[nome]}")
    else:
        while True:
            tel = input(f"\nDigite o Número de Telefone do(a) {nome}: ").replace(' ', '')

            if not tel or any(c.isalpha() for c in tel):
                print("\nERRO: O Número Deve ter Apenas Números. Tente Novamente")
                continue

            agenda[nome] = tel
            print(f"\nNúmero {tel} Adicionado à Agenda com Sucesso!")
            break


# Exercício 10: Atualização de vários valores
#   Atualize os telefones de "Beatriz" e "Eduardo" simultaneamente.

agenda["Beatriz"] = "9999-3333"
agenda["Eduardo"] = "9999-4444"
print(f"\nTelefones de Beatriz e Eduardo Atualizados com Sucesso!")

# Exercício 11: Acesso seguro (get)
#   Use o método get() para acessar o telefone de "João", retornando uma mensagem personalizada se ele não existir.

print(f"\nBuscando Contato: {agenda.get('João', 'O Contato João não Existe na Agenda.')}")

# Exercício 12: Verificar se a agenda está vazia
#   Mostre "Vazia" ou "Contatos existentes".

if not agenda:
    print("\nVazia.")
else:
    print("\nContatos existentes.")

# Exercício 13: Obter lista de chaves e valores separadamente
#   Mostre todas as chaves e depois todos os valores.

print(f"\nExibindo Todas as Chaves da Agenda: {list(agenda.keys())}")
print(f"\nExibindo Todos os Valores da Agenda: {list(agenda.values())}")

# Exercício 14: Atualização usando update()
#   Utilize o método update() para inserir ou alterar o contato "Lucas".

agenda.update({"Lucas": "9999-5555"})
print(f'\nContato "Lucas" Atualizado via update(): {agenda["Lucas"]}')

# Exercício 15: Criar um dicionário a partir de duas listas
#   Dada uma lista de nomes e outra de telefones, crie um dicionário.

nomes = ["Marcos", "Patrícia"]
telefones = ["9999-6666", "9999-7777"]
nova_agenda = dict(zip(nomes, telefones))
print(f"\nNovo Dicionário Criado a Partir de Duas Listas: {nova_agenda}")

# Exercício 16: Contar quantos nomes possuem mais de 6 letras
#   Mostre o total de nomes (chaves) com mais de 6 caracteres.

contagem = sum(1 for nome in agenda if len(nome) > 6)
print(f"\nQuantidade de Nomes com Mais de 6 Letras: {contagem}")

# Exercício 17: Filtrar dicionário
#   Crie um novo dicionário contendo apenas os contatos cujo número termina com "0001", "0003" ou "0005".

agenda_filtrada = {k: v for k, v in agenda.items() if v.endswith(("0001", "0003", "0005"))}
print(f"\nExibindo Nova Agenda Filtrada por Finais: {agenda_filtrada}")

# Exercício 18: Apagar todos os contatos
#   Use clear() para esvaziar o dicionário.

agenda.clear()
print(f"\nLimpando Toda a Agenda com clear(). Status Atual: {agenda}")

print("\nFim do programa. Obrigado por visitar!\n")