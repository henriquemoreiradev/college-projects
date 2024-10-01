import mysql.connector
#from mysql.connector import errorcode


def criar_conexao():
    try:
        endereco = "localhost"
        usuario = "root"
        senha = "12345"
        bancodedados = "ouvidoria"

        return mysql.connector.connect(
            host = endereco,
            user = usuario,
            password = senha,
            database = bancodedados
        )
    except mysql.connector.Error as err:
        print("-" * 110)
        print(f"Erro ao conectar ao banco de dados: {err}")
        print("-" * 110)
        return None


def checar_banco_dados():
    try:
        endereco = "localhost"
        usuario = "root"
        senha = "12345"
        bancodedados = "ouvidoria"

        #   criar_banco_dados   ------------------------------------------------------------
        conexao = mysql.connector.connect(
            host = endereco,
            user = usuario,
            password = senha
        )
            
        cursor = conexao.cursor()
            
        cursor.execute(f"SHOW DATABASES LIKE '{bancodedados}'")
        resultado = cursor.fetchone()
            
        if not resultado:
            cursor.execute(f"CREATE DATABASE {bancodedados}")
            # print(f"Banco de dados '{bancodedados}' criado com sucesso!")
            pass
        else:
            # print(f"Banco de dados '{bancodedados}' já existe.")
            pass
        
        cursor.close()
        conexao.close()

        #   criar_tabela    ----------------------------------------------------------------
        conexao = mysql.connector.connect(
            host = endereco,
            user = usuario,
            password = senha,
            database = bancodedados
        )
        cursor = conexao.cursor()

        tabelas = {
            "reclamacoes": "CREATE TABLE reclamacoes (id_reclamacao BIGINT PRIMARY KEY, reclamacao VARCHAR(255) NOT NULL)",
            "elogios": "CREATE TABLE elogios (id_elogio BIGINT PRIMARY KEY, elogio VARCHAR(255) NOT NULL)",
            "sugestoes": "CREATE TABLE sugestoes (id_sugestao BIGINT PRIMARY KEY, sugestao VARCHAR(255) NOT NULL)"
        }

        for nome_tabela, sql_criacao in tabelas.items():
            cursor.execute(f"SHOW TABLES LIKE '{nome_tabela}'")
            resultado = cursor.fetchone()
            if not resultado:
                cursor.execute(sql_criacao)
                # print(f"Tabela '{nome_tabela}' criada com sucesso!")
                pass
            else:
                # print(f"Tabela '{nome_tabela}' já existe.")
                pass
        cursor.close()
        conexao.close()
        return True
    except mysql.connector.Error as err:
        print("-" * 110)
        print(f"Erro ao checar o banco de dados: {err}")
        print("-" * 110)
        return None


def limpar_console():
    import os
    os.system("cls" if os.name == "nt" else "clear")


def exibirManifestacao(manifestacao):
        #print(f"\n{tabela.capitalize()}:")
        print("-" * 40)
        print(" | ".join([str(item) for item in manifestacao]))
        print("-" * 40)


def menu():
    print("""\n----------- MENU DO SISTEMA ------------\n
[1] Listagem das manifestações
[2] Listagem de manifestações por tipo
[3] Criar uma nova manifestação
[4] Exibir quantidade de manifestações
[5] Pesquisar uma manifestação por código
[6] Excluir uma manifestação pelo código
[7] Sair do sistema""")

    opcao = input("\n    Escolha uma opção: ")

    limpar_console()

    if opcao == "1":
        listar_manifestacoes()

    elif opcao == "2":
        listar_manifestacoes_tipo()

    elif opcao == "3":
        nova_manifestacao()
        
    elif opcao == "4":
        quantidade_manifestacoes()
        
    elif opcao == "5":
        pesquisar_manifestacao()
        
    elif opcao == "6":
        excluir_manifestacao()
        
    elif opcao == "7":
        exit()

    else:
        print("\nOpção inválida! Tente novamente...\n")
        menu()


def listar_manifestacoes():
    try:
        print(f"\n------ LISTAGEM DAS MANIFESTAÇÕES ------")
        conexao = criar_conexao()
        tabelas = ["reclamacoes", "elogios", "sugestoes"]
        verificador = 0

        for nome_tabela in tabelas:
            cursor = conexao.cursor()
            cursor.execute(f"SELECT * FROM {nome_tabela}")
            resultado = cursor.fetchall()

            if resultado:
                verificador += 1
                print(f"\n{nome_tabela.capitalize()}:")
                for linha in resultado:
                    exibirManifestacao(linha)
        if verificador == 0:
            limpar_console()
            print(f"\nNenhuma manifestação foi registrada.\n")
            
        cursor.close()
        conexao.close()
        print()
    except mysql.connector.Error as err:
        print("-" * 110)
        print(f"Erro ao listar manifestações: {err}")
        print("-" * 110)
        return None    
    finally:
        menu()


def listar_manifestacoes_tipo():
    print("""\n-- LISTAGEM DE MANIFESTAÇÕES POR TIPO --\n
[1] Reclamações
[2] Elogios
[3] Sugestões""")

    opcao = input("\n    Escolha uma opção: ")

    limpar_console()
    try:
        print(f"\n-- LISTAGEM DE MANIFESTAÇÕES POR TIPO --")
        conexao = criar_conexao()
        cursor = conexao.cursor()

        if opcao == "1":
            nome_tabela = "reclamacoes"
            cursor.execute(f"SELECT * FROM reclamacoes")

        elif opcao == "2":
            nome_tabela = "elogios"
            cursor.execute(f"SELECT * FROM elogios")

        elif opcao == "3":
            nome_tabela = "sugestoes"
            cursor.execute(f"SELECT * FROM sugestoes")
            
        resultado = cursor.fetchall()
        if resultado:
            print(f"\n{nome_tabela.capitalize()}:")
            for linha in resultado:
                exibirManifestacao(linha)
        else:
            limpar_console()
            print(f"\nNenhuma manifestação foi registrada.\n")
        cursor.close()
        conexao.close()
    except mysql.connector.Error as err:
        print("-" * 110)
        print(f"Erro ao listar manifestações: {err}")
        print("-" * 110)
        return None    
    finally:
        menu()


def nova_manifestacao():
    try:
        print("""\n----- CRIAR UMA NOVA MANIFESTAÇÃO ------\n
[1] Reclamações
[2] Elogios
[3] Sugestões""")

        opcao = input("\n    Escolha uma opção: ")

        limpar_console()
        conexao = criar_conexao()
        cursor = conexao.cursor()

        from datetime import datetime
        data_e_hora_atuais = datetime.now()
        codigo_id = data_e_hora_atuais.strftime("%d%m%Y%H%M%S")

        if opcao == "1":
            nome_tabela = "reclamacoes"
            reclamacao = input("Digite sua reclamação: ")
            cursor.execute("INSERT INTO reclamacoes (id_reclamacao, reclamacao) VALUES (%s, %s)", (codigo_id, reclamacao))
            cursor.execute("SELECT * FROM reclamacoes WHERE id_reclamacao = %s", (codigo_id,))

        elif opcao == "2":
            nome_tabela = "elogios"
            elogio = input("Digite seu elogio: ")
            cursor.execute("INSERT INTO elogios (id_elogio, elogio) VALUES (%s, %s)", (codigo_id, elogio))
            cursor.execute("SELECT * FROM elogios WHERE id_elogio = %s", (codigo_id,))

        elif opcao == "3":
            nome_tabela = "sugestoes"
            sugestao = input("Digite sua sugestão: ")
            cursor.execute("INSERT INTO sugestoes (id_sugestao, sugestao) VALUES (%s, %s)", (codigo_id, sugestao))
            cursor.execute("SELECT * FROM sugestoes WHERE id_sugestao = %s", (codigo_id,))
        
        resultados = cursor.fetchall()
        conexao.commit()
        for linha in resultados:
            exibirManifestacao(nome_tabela, linha)
        cursor.close()
        conexao.close()
    except mysql.connector.Error as err:
        print("-" * 110)
        print(f"Erro ao criar manifestação: {err}")
        print("-" * 110)
        return None
    finally:
        menu()


def quantidade_manifestacoes():
    print(f"\n----- QUANTIDADE DE MANIFESTAÇÕES ------")

    conexao = criar_conexao()
    cursor = conexao.cursor()

    tabelas = ["reclamacoes", "elogios", "sugestoes"]
    tamanho = 0

    for nome_tabela in tabelas:
        cursor.execute(f"SELECT COUNT(*) FROM {nome_tabela}")
        resultado = cursor.fetchall()
        tamanho += resultado[0][0]
    
    cursor.close()
    conexao.close()

    if tamanho > 0:
        print("-" * 40)
        print(f"\nHá {tamanho} manifestações registradas\n")
        print("-" * 40)
    else:
        print(f"\nNão há manifestações registradas\n")
    
    menu()


def pesquisar_manifestacao():
    try:
        print("\n------------ PESQUISAR UMA MANIFESTAÇÃO POR CÓDIGO -------------")

        pesquisa_id = int(input("Digite o código da manifestação que você procura: "))

        tabelas = {
                "reclamacoes": "id_reclamacao",
                "elogios": "id_elogio",
                "sugestoes": "id_sugestao"
            }
        conexao = criar_conexao()
        cursor = conexao.cursor()
        verificador = 0
        for nome_tabela, id_coluna in tabelas.items():
            cursor.execute(F"SELECT * FROM {nome_tabela} WHERE {id_coluna} = '{pesquisa_id}'")
            resultados = cursor.fetchall()
            if resultados:
                verificador += 1
                limpar_console()
                print(f"\n{nome_tabela.capitalize()}:")
                for linha in resultados:
                    exibirManifestacao(linha)
        if verificador == 0:
            limpar_console()
            print(f"Nenhuma manifestação de código {pesquisa_id} foi encontrada.")
        cursor.close()
        conexao.close()
    except mysql.connector.Error as err:
        print("-" * 110)
        print(f"Erro ao pesquisar manifestação: {err}")
        print("-" * 110)
        return None
    finally:
        menu()


def excluir_manifestacao():
    try:
        print("\n------------- EXCLUIR UMA MANIFESTAÇÃO PELO CÓDIGO -------------")

        pesquisa_id = int(input("\nDigite o código da manifestação que você procura: "))

        tabelas = {
                "reclamacoes": "id_reclamacao",
                "elogios": "id_elogio",
                "sugestoes": "id_sugestao"
            }
        conexao = criar_conexao()
        cursor = conexao.cursor()
        for nome_tabela, id_coluna in tabelas.items():
            cursor.execute(F"SELECT * FROM {nome_tabela} WHERE {id_coluna} = '{pesquisa_id}'")
            resultados = cursor.fetchall()
            if resultados:
                cursor.execute(F"DELETE FROM {nome_tabela} WHERE {id_coluna} = '{pesquisa_id}'")
                conexao.commit()

                linhas_afetadas = cursor.rowcount
                if linhas_afetadas > 0:
                    limpar_console()
                    print("------------------------------------------------------------")
                    print(f"Manifestação com código {pesquisa_id} excluída com sucesso.")
                    print("------------------------------------------------------------")
                else:
                    print(f"Nenhuma manifestação encontrada com o código {pesquisa_id}.")
        cursor.close()
        conexao.close()
    except mysql.connector.Error as err:
        print("-" * 110)
        print(f"Erro ao excluir manifestação: {err}")
        print("-" * 110)
        return None
    finally:
        menu()


if checar_banco_dados():
    menu()