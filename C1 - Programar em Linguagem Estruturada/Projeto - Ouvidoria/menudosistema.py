manifestacoes = []

manifestacao_reclamacao = {"reclamacao":""}
manifestacao_elogio  = {"elogio"}
manifestacao_sugestao = {"sugestao"}

print(manifestacao_reclamacao)
manifestacoes = manifestacao_reclamacao + manifestacao_elogio + manifestacao_sugestao

def listar_manifestacoes(): #1) Listagem das Manifestações
    if len(manifestacoes) == 0:
        print("Não há manifestações cadastradas.")
    else:
        print("Lista de manifestacoes")
        for item in manifestacoes:
            print("-", item)

def listar_manifestacoes_tipo(): #2) Listagem de Manifestações por Tipo
    opcao = 0

    print("""\nInforme o tipo de Manifestação
1) Reclamção
2) Elogio
3) Sugestão
4) Sair""")

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        print("Lista de reclamações")
        for item in manifestacao_reclamacao:
            print("-", item)
            
    elif opcao == 2:
        print("Lista de elogios")
        for item in manifestacao_elogio:
            print("-", item)
            
    elif opcao == 3:
        print("Lista de sugestao")
        for item in manifestacao_sugestao:
            print("-", item)
    elif opcao != 4:
        print("Opção Inválida")

def nova_manifestacao(): #3) Criar uma nova Manifestação
    opcao = 0

    print("""\nInforme o tipo de Manifestação que você pretende criar
1) Reclamção
2) Elogio
3) Sugestão
4) Sair""")
    
    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        pass
            
    elif opcao == 2:
        pass
            
    elif opcao == 3:
        pass
    
    elif opcao != 4:
        print("Opção Inválida")

def menu():
    opcao = 0
    while opcao != 7:
        print("""\n1) Listagem das Manifestações
2) Listagem de Manifestações por Tipo
3) Criar uma nova Manifestação
4) Exibir quantidade de manifestações
5) Pesquisar uma manifestação por código
6) Excluir uma Manifestação pelo Código
7) Sair do Sistema""")
        opcao = int(input("Escolha uma opção: "))
    
        if opcao == 1: #1) Listagem das Manifestações
            listar_manifestacoes()

        elif opcao == 2: #2) Listagem de Manifestações por Tipo
            listar_manifestacoes_tipo()

        elif opcao == 3: #3) Criar uma nova Manifestação
            nova_manifestacao()
        
        elif opcao == 4: #4) Exibir quantidade de manifestações
            # pesquisar_manifestacao
            print('opção 4')
        
        elif opcao == 5: #5) Pesquisar uma manifestação por código
            # excluir_manifestacao
            print('opção 5')
        
        elif opcao == 6: #6) Excluir uma Manifestação pelo Código
            print("Saindo do Sistema...")
        
        else:
            print('Opção inválida')
            
menu()