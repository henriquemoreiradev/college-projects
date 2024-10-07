#Locadora
#1) Listar
#2) Adicionar
#3) Sair
#Digite sua opção:

opcao = 0

while opcao != 3:
    print("Opção: 1) Listar, 2) Adicionar, 3) Sair")

    opcao = int(input("Digite a sua opção: "))
    print(f"A opção lida foi {opcao}")

    if opcao == 1:
        print("Listar")
    
    elif opcao == 2:
        print("Adicionar")

    elif opcao != 3:
        print("Opção inválida")

print("Bye")