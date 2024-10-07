manifestacoes = []

manifestacao_reclamacao = []
manifestacao_elogio  = []
manifestacao_sugestao = []

manifestacoes = manifestacao_reclamacao + manifestacao_elogio + manifestacao_sugestao

# Menu --------------------------------------------------------------
def menu():
    while True:
        print("""--- MENU DO SISTEMA ---\n
1) Listagem das Manifestações
2) Listagem de Manifestações por Tipo
3) Criar uma nova Manifestação
4) Exibir quantidade de manifestações
5) Pesquisar uma manifestação por código
6) Excluir uma Manifestação pelo Código
7) Sair do Sistema""")
        opcao = input("\n   Escolha uma opção: ")

        limpar_console()

        if opcao == "1": #1) Listagem das Manifestações
            listar_manifestacoes()

        elif opcao == "2": #2) Listagem de Manifestações por Tipo
            listar_manifestacoes_tipo()

        elif opcao == "3": #3) Criar uma nova Manifestação
            nova_manifestacao()
        
        elif opcao == "4": #4) Exibir quantidade de manifestações
            quantidade_manifestacoes()
        
        elif opcao == "5": #5) Pesquisar uma manifestação por código
            pesquisar_manifestacao()
        
        elif opcao == "6": #6) Excluir uma Manifestação pelo Código
            excluir_manifestacao()
        
        elif opcao == "7": #7) Sair do Sistema
            exit()

        else:
            print("Opção inválida! Tente novamente...\n")
            menu()

# Limpar console ----------------------------------------------------
def limpar_console():
    import os
    os.system("cls" if os.name == "nt" else "clear")

# Retornar ou Sair --------------------------------------------------
def retornar_ou_sair():

    print("""\n1) Menu
2) Sair""")
    
    opcao = input("\n   Escolha uma opção: ")
    
    if opcao == "1":
        limpar_console()
        menu()

    elif opcao == "2":
        limpar_console()
        exit()

    else:
        limpar_console()
        print("Opção inválida! Tente novamente...\n")
        retornar_ou_sair()

#1) Listagem das Manifestações --------------------------------------
def listar_manifestacoes():

    if len(manifestacoes) == 0:
        print("Não há manifestações cadastradas.")
    else:
        print("--- LISTAGEM DE MANIFESTAÇÕES ---\n")
        for item in manifestacoes:
            print("-", item)

    retornar_ou_sair()

#2) Listagem de Manifestações por Tipo ------------------------------
def listar_manifestacoes_tipo():

    print("""--- LISTAGEM DE MANIFESTAÇÕES POR TIPO ---\n
Informe o tipo de Manifestação\n
1) Reclamção
2) Elogio
3) Sugestão
4) Retornar
5) Sair""")

    opcao = input("\nDigite uma opção: ")

    limpar_console()

    if opcao == "1": #Reclamção
        print("--- LISTA DE RECLAMAÇÕES ---\n")
        for item in manifestacao_reclamacao:
            print("-", item)

        retornar_ou_sair()
            
    elif opcao == "2": #Elogio
        print("--- LISTA DE ELOGIOS ---\n")
        for item in manifestacao_elogio:
            print("-", item)

        retornar_ou_sair()
            
    elif opcao == "3": #Sugestão
        print("--- LISTA DE SUGESTÕES ---\n")
        for item in manifestacao_sugestao:
            print("-", item)
        
        retornar_ou_sair()
    
    elif opcao == "4": #Retornar ao menu
        menu()

    elif opcao == "5": #Sair
        limpar_console()
        exit()
    
    else:
        limpar_console()
        print("Opção inválida! Tente novamente...\n")
        listar_manifestacoes_tipo()

#3) Criar uma nova Manifestação -------------------------------------
def nova_manifestacao():
    global manifestacoes

    print("""Informe o tipo de Manifestação que você pretende criar\n
1) Reclamção
2) Elogio
3) Sugestão
4) Retornar
5) Sair""")
    
    opcao = input("\nDigite uma opção: ")

    if opcao == "1": #Reclamção
        print("\nDigite sua reclamação")
        manifestacao_reclamacao.append(input(": "))
        manifestacoes.append(manifestacao_reclamacao[-1])
        print(f"O código da sua reclamação é {len(manifestacao_reclamacao)}\n")
        nova_manifestacao()
            
    elif opcao == "2": #Elogio
        print("\nDigite seu elogio")
        manifestacao_elogio.append(input(": "))
        manifestacoes.append(manifestacao_elogio[-1])
        print(f"O código do seu elogio é {len(manifestacao_elogio)}\n")
        nova_manifestacao()
            
    elif opcao == "3": #Sugestão
        print("\nDigite sua sugestão")
        manifestacao_sugestao.append(input(": "))
        manifestacoes.append(manifestacao_sugestao[-1])
        print(f"O código da sua sugestão é {len(manifestacao_sugestao)}\n")
        nova_manifestacao()
    
    elif opcao == "4": #Retornar ao menu
        limpar_console()
        menu()

    elif opcao == "5": #Sair
        limpar_console()
        exit()
    
    else:
        limpar_console()
        print("Opção inválida! Tente novamente...\n")
        nova_manifestacao()

#4) Exibir quantidade de manifestações ------------------------------
def quantidade_manifestacoes():
    print(f"--- CONTADOR DE MANIFESTAÇÕES ---\n")
    print(f"Há {len(manifestacoes)} manifestações registradas.")
    retornar_ou_sair()

#5) Pesquisar uma manifestação por código ---------------------------
def pesquisar_manifestacao():
    global manifestacoes
    print(f"--- BUSCAR MANIFESTAÇÁO ---\n")
    posicao = int(input("Informe o código da manifestação que você procura: "))
    print(f"O elemento pesquisado foi {manifestacoes[posicao-1]}")
    retornar_ou_sair()

#6) 6) Excluir uma Manifestação pelo Código -------------------------
def excluir_manifestacao():
    print(f"--- EXCLUIR MANIFESTAÇÁO ---\n")

    print("""Informe o tipo de Manifestação que você pretende excluir\n
1) Reclamção
2) Elogio
3) Sugestão
4) Retornar
5) Sair""")
    
    opcao = input("\nDigite uma opção: ")

    if opcao == "1": #Reclamção
        posicao = int(input("Informe o código da reclamação que você pretende excluir: "))
        
        confirmar = input(f"O código informado foi {posicao}. Digite 's' para confirmar e 'n' para corrigir: ")
        
        if confirmar == "s":
            del manifestacao_reclamacao[posicao-1]
        elif confirmar == "n":
            excluir_manifestacao()
        else:
            limpar_console()
            print("Opção inválida! Tente novamente...\n")
            excluir_manifestacao()

    elif opcao == "2": #Elogio
        posicao = int(input("Informe o código do elogio que você pretende excluir: "))
        
        confirmar = input(f"O código informado foi {posicao}. Digite 's' para confirmar e 'n' para corrigir: ")
        
        if confirmar == "s":
            del manifestacao_elogio[posicao-1]
        elif confirmar == "n":
            excluir_manifestacao()
        else:
            limpar_console()
            print("Opção inválida! Tente novamente...\n")
            excluir_manifestacao()

    elif opcao == "3": #Sugestão
        posicao = int(input("Informe o código da sugestão que você pretende excluir: "))
        
        confirmar = input(f"O código informado foi {posicao}. Digite 's' para confirmar e 'n' para corrigir: ")
        
        if confirmar == "s":
            del manifestacao_sugestao[posicao-1]
        elif confirmar == "n":
            excluir_manifestacao()
        else:
            limpar_console()
            print("Opção inválida! Tente novamente...\n")
            excluir_manifestacao()

    elif opcao == "4": #Retornar ao menu
        limpar_console()
        menu()

    elif opcao == "5": #Sair
        limpar_console()
        exit()
    
    else:
        limpar_console()
        print("Opção inválida! Tente novamente...\n")
        excluir_manifestacao()
    
    print(f"\nA manifestação foi excluída com sucesso!\n")
    retornar_ou_sair()

menu()