# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

print("\n-- Entrada de 4 notas de 10 alunos, processamento de média de cada aluno e impressão de resultado para usuário --")

vetor_medias = []
count_aprovados = 0

while True:
    for i in range(1, 11):
        soma_notas = 0
        print(f"\nDados do aluno {i}:")
    
        for j in range(1, 5):
            nota = float(input(f"Digite a {j}° nota: ").replace(' ', '').replace(',', '.'))
            soma_notas += nota
    
        media = soma_notas / 4
        vetor_medias.append(media) # Armazena no vetor conforme pedido
    
        if media >= 7.0:
            count_aprovados += 1
    
    print(f"  Média do aluno {i}: {media:.1f}\n")

    print(f"""
-- Resumo de notas dos alunos --
          
Médias dos alunos: {vetor_medias}
Número de alunos com média igual ou maior que 7: {count_aprovados}
""")
    
    continuar = input("Deseja calcular mais médias? (s/n): ").strip().lower()
    if continuar != 's':
        break

print("\nFim do programa. Obrigado por usar!\n")