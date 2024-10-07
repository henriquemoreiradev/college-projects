manifestacoes = []

# Menu --------------------------------------------------------------
def menu():
    opcao = ""
    while opcao != "7":
        print("""--- MENU DO SISTEMA ---\n
1) Listagem das Manifestações
2) Listagem de Manifestações por Tipo
3) Criar uma nova Manifestação
4) Exibir quantidade de manifestações
5) Pesquisar uma manifestação por código
6) Excluir uma Manifestação pelo Código
7) Sair do Sistema""")
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":  # 1) Listagem das Manifestações
            limpar_console()
            listar_manifestacoes()

        elif opcao == "2":  # 2) Listagem de Manifestações por Tipo
            limpar_console()
            listar_manifestacoes_tipo()

        elif opcao == "3":  # 3) Criar uma nova Manifestação
            limpar_console()
            criar_manifestacao()

        elif opcao == "4":  # 4) Exibir quantidade de manifestações
            limpar_console()
            quantidade_manifestacoes()

        elif opcao == "5":  # 5) Pesquisar uma manifestação por código
            limpar_console()
            pesquisar_manifestacao()

        elif opcao == "6":  # 6) Excluir uma Manifestação pelo Código
            limpar_console()
            excluir_manifestacao()

        elif opcao == "7":  # 7) Sair do Sistema
            limpar_console()
            exit()

        else:
            limpar_console()
            print("Opção inválida! Tente novamente...\n")

# Limpar console ----------------------------------------------------
def limpar_console():
    import os
    os.system("cls" if os.name == "nt" else "clear")

# Retornar ou Sair --------------------------------------------------
def retornar_ou_sair():
    opcao = ""
    while opcao != "2":
        print("""\n1) Menu
2) Sair""")
        opcao = input("\n  Escolha uma opção: ")

        if opcao == "1":
            limpar_console()
            menu()
            return  # Retorna após o menu ser chamado para evitar duplicação

        elif opcao == "2":
            limpar_console()
            exit()

        else:
            limpar_console()
            print("Opção inválida! Tente novamente...\n")

# 1) Listagem das Manifestações --------------------------------------
def listar_manifestacoes():
    if len(manifestacoes) == 0:
        print("Não há manifestações cadastradas.")
    else:
        print("--- LISTAGEM DE MANIFESTAÇÕES ---\n")
        for item in manifestacoes:
            print(f"Código: {item["codigo"]}, Tipo: {item["tipo"]}, Descrição: {item["descricao"]}, Autor: {item["autor"]}")

    retornar_ou_sair()

# 2) Listagem de Manifestações por Tipo ------------------------------
def listar_manifestacoes_tipo():
    print("""--- LISTAGEM DE MANIFESTAÇÕES POR TIPO ---\n
Informe o tipo de Manifestação\n
1) Reclamação
2) Elogio
3) Sugestão
4) Retornar
5) Sair""")

    opcao = input("\nDigite uma opção: ")

    limpar_console()

    if opcao == "1":  # Reclamção
        print("--- LISTA DE RECLAMAÇÕES ---\n")
        for item in manifestacoes:
            if item["tipo"] == "Reclamção":
                print(f"Código: {item["codigo"]}, Descrição: {item["descricao"]}, Autor: {item["autor"]}")

    elif opcao == "2":  # Elogio
        print("--- LISTA DE ELOGIOS ---\n")
        for item in manifestacoes:
            if item["tipo"] == "Elogio":
                print(f"Código: {item["codigo"]}, Descrição: {item["descricao"]}, Autor: {item["autor"]}")

    elif opcao == "3":  # Sugestão
        print("--- LISTA DE SUGESTÕES ---\n")
        for item in manifestacoes:
            if item["tipo"] == "Sugestão":
                print(f"Código: {item["codigo"]}, Descrição: {item["descricao"]}, Autor: {item["autor"]}")

    elif opcao == "4":  # Retornar ao menu
        menu()

    elif opcao == "5":  # Sair
        limpar_console()
        exit()

    else:
        limpar_console()
        print("Opção inválida! Tente novamente...\n")
        listar_manifestacoes_tipo()

    retornar_ou_sair()

# 3) Criar uma nova Manifestação -------------------------------------
def criar_manifestacao():
    tipo = input("""\n1) Reclamação 
2) Elogio 
3) Sugestão 
Informe o tipo de manifestação: """).strip()

    tipos_validos = ["1", "2", "3"]
    if tipo not in tipos_validos:
        print("Tipo inválido. A manifestação não foi criada.")
        retornar_ou_sair()
        return

    tipo_dict = {"1": "Reclamção", "2": "Elogio", "3": "Sugestão"}
    tipo_manifestacao = tipo_dict[tipo]

    descricao = input("Descreva a manifestação: ").strip()
    autor = input("Informe o autor da manifestação: ").strip()
    codigo = len(manifestacoes) + 1

    nova_manifestacao = {
        "codigo": codigo,
        "tipo": tipo_manifestacao,
        "descricao": descricao,
        "autor": autor
    }
    manifestacoes.append(nova_manifestacao)
    print("Manifestação criada com sucesso!")

    retornar_ou_sair()

# 4) Exibir quantidade de manifestações ------------------------------
def quantidade_manifestacoes():
    print(f"--- CONTADOR DE MANIFESTAÇÕES ---\n")
    print(f"Há {len(manifestacoes)} manifestações registradas")
    retornar_ou_sair()

# 5) Pesquisar uma manifestação por código ---------------------------
def pesquisar_manifestacao():
    codigo = int(input("Informe o código da manifestação que você procura: ").strip())
    encontrado = False
    for item in manifestacoes:
        if item['codigo'] == codigo:
            print(f"Código: {item["codigo"]}, Tipo: {item["tipo"]}, Descrição: {item["descricao"]}, Autor: {item["autor"]}")
            encontrado = True
            break
    if not encontrado:
        print("Manifestação não encontrada")

    retornar_ou_sair()

# 6) Excluir uma Manifestação pelo Código ---------------------------
def excluir_manifestacao():
    global manifestacoes
    try:
        codigo = int(input("Informe o código da manifestação que você pretende excluir: ").strip())

        print(f"Manifestacoes antes da exclusão: {manifestacoes}")

        if any(item["codigo"] == codigo for item in manifestacoes):
            manifestacoes = [item for item in manifestacoes if item["codigo"] != codigo]
            print("Manifestação excluída com sucesso.")
        else:
            print("Manifestação não encontrada")

        print(f"Manifestacoes após a exclusão: {manifestacoes}")

    except ValueError:
        print("Código inválido. Informe um número inteiro")

    retornar_ou_sair()
menu()