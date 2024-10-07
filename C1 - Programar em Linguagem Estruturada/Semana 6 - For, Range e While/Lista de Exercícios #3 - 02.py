#2 Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nomeDeUsuario = input("Digite o nome de usuário: ")

while True:
    senha = input("Digite a senha: ")

    if senha != nomeDeUsuario:
        break
    else:
        print("A senha não pode ser igual ao nome de usuário.")