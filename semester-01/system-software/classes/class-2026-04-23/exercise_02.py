# Autor: Guilherme Caetano Lima
# Exercício: Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

print("-"*50)
print("Entrada de nome de usuário e senha, verificação se senha é igual ao nome de usuário e impressão de resultado para usuário")
print("-"*50)

while True:
    entrada = False

    while entrada == False:
        nome_usuario = input("\nDigite seu nome de usuário para criar a conta: ").strip()
        senha = input("Digite sua senha para criar a conta (a senha e o nome de usuário devem ser diferentes): ").strip()

        while nome_usuario == senha:
            entrada = False
            print("\nERRO: A senha não pode ser igual ao nome do usuário. Tente novamente.")
            break
        else:
            print("\nSua conta foi criada com sucesso!")
            entrada = True

    continuar = input("\nDeseja criar outra conta? (s/n): ").strip().lower()
    if continuar != 's':
        break

print("\nFim do programa. Obrigado por visitar!\n")