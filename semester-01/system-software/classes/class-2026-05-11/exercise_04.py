# Autor: Guilherme Caetano Lima
# Exercício: Uma turma de ADS precisa calcular as médias das notas de seus alunos. O programa deve armazenar as notas em uma lista e realizar cálculos sobre elas.

print("\n-- Entrada de 5 notas de alunos, processamento de média da turma, aprovados e reprovados, verificação de maior e menor nota e impressão de resultado para usuário --")

while True:
    lista_notas = []
    aprovados = 0
    
    print()
    try:
        for i in range(1, 6):
            nota = float(input(f"Digite a {i}° nota: ").replace(',', '.'))
            lista_notas.append(nota)
            if nota >= 6:
                aprovados += 1

    except ValueError:
        print("\nERRO: Digite apenas números.")
        continue

    maior_nota = max(lista_notas)
    menor_nota = min(lista_notas)
    media = sum(lista_notas) / 5

    print(f"""
-- Resumo de notas --
          
Lista de notas: {lista_notas}
Maior nota: {maior_nota}
Menor nota: {menor_nota}
Média da sala: {media}

Alunos aprovados: {aprovados}
Alunos reprovados: {5 - aprovados}
""")
    
    if input("Deseja verificar mais notas: [s/n]: ").strip().lower() != 's':
        break

print("\nFim do programa. Obrigado por visitar!\n")