# Autor: Guilherme Caetano Lima
# Exercise 01: Criação e manipulação de arquivos txt

from datetime import datetime

# Diretório base para geração dos arquivos corrigido
diretorio = "semester-01/system-software/classes/class-2026-06-08/"

# 1. ESCRITA E ATUALIZAÇÃO DE ARQUIVOS

# Criando e adicionando nomes (writelines aceita listas/geradores)
with open(f"{diretorio}alunos.txt", "w", encoding="utf-8") as arquivo:
    arquivo.writelines(["Guilherme Caetano\n", "Felipe Camargo\n", "João Ricardo\n"])
print("Arquivo 'alunos.txt' criado com sucesso!")

with open(f"{diretorio}alunos.txt", "a", encoding="utf-8") as arquivo:
    arquivo.writelines(["Daniela Rocha\n", "Carlos Rodrigues\n"])
print("Nomes adicionados com sucesso!")


# 2. LEITURA, BUSCA E ESTATÍSTICAS

# Lendo, exibindo linhas enumeradas e buscando termo de uma só vez
busca = "Carlos"
print("\n--- Conteúdo do Arquivo ---")

with open(f"{diretorio}alunos.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    
    # Exibe o conteúdo bruto
    print(conteudo.strip()) 
    print("\n--- Lista Customizada ---")
    
    # Reseta o ponteiro para ler linha por linha e buscar
    arquivo.seek(0)
    for i, linha in enumerate(arquivo, 1):
        linha_limpa = linha.strip()
        print(f"Aluno {i}: {linha_limpa}")
        
        if busca.lower() in linha_limpa.lower():
            print(f"  └─> [Busca] Encontrado na Linha {i}: {linha_limpa}")

# Estatísticas do arquivo
linhas = conteudo.splitlines()
print(f"\nEstatísticas:\n- Linhas: {len(linhas)}\n- Palavras: {len(conteudo.split())}\n- Caracteres: {len(conteudo)}")


# 3. MANIPULAÇÃO DE CONTEÚDO (SUBSTITUIR E REMOVER)

# Atualizar nome
conteudo_novo = conteudo.replace("Guilherme Caetano", "Guilherme Caetano Lima")
with open(f"{diretorio}alunos.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(conteudo_novo)
print("\nNome atualizado com sucesso!")

# Salvar lista de notas
notas = ["Ana Silva", "9.5", "Bruno Oliveira", "7.0", "Carlos Mendes", "8.2", "Daniela Rocha", "9.8"]
with open(f"{diretorio}notas.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("\n".join(notas) + "\n")
print("notas.txt salvo com sucesso!")

# Remover uma linha específica de notas.txt
remover = "Carlos Mendes"
with open(f"{diretorio}notas.txt", "r", encoding="utf-8") as arquivo:
    linhas_notas = arquivo.readlines()

with open(f"{diretorio}notas.txt", "w", encoding="utf-8") as arquivo:
    arquivo.writelines(l for l in linhas_notas if remover not in l)
print(f'"{remover}" removido de notas.txt com sucesso!')


# 4. SISTEMA DE LOGS

def registrar_log(mensagem, arquivo="sistema.log"):
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    entrada = f"[{agora}] {mensagem}\n"
    with open(f"{diretorio}{arquivo}", "a", encoding="utf-8") as f:
        f.write(entrada)
    print(f"LOG: {entrada.strip()}")

print("\n--- Simulando Eventos de Log ---")
registrar_log("Sistema iniciado")
registrar_log("Usuário 'admin' fez login")
registrar_log("Arquivo alunos.txt modificado")
registrar_log("Sistema encerrado")


# 5. OUTROS ARQUIVOS E MODOS COMPLEMENTARES

# Criando frutas
with open(f"{diretorio}frutas.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Maça\nBanana\nUva\nLaranja\nMelância\n")

# Uso do modo 'x' (Gera erro se o arquivo já existir)
try:
    with open(f"{diretorio}frutas_premium.txt", "x", encoding="utf-8") as arquivo:
        arquivo.write("Morango\nAbacaxi\n")
    print("\nArquivo exclusivo 'frutas_premium.txt' criado com sucesso!")
except FileExistsError:
    print("\n[Aviso] O arquivo 'frutas_premium.txt' já existe, nada foi feito.")