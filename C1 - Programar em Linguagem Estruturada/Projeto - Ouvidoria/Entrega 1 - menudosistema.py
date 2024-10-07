"""
Esse código inicializa listas de manifestações, combina essas listas em uma única lista e define uma função menu() que exibe um menu de opções para o usuário. Dependendo da escolha do usuário, diferentes funções são chamadas para listar, criar, contar, pesquisar ou excluir manifestações, ou para sair do sistema.
"""

manifestacoes = [] # Inicializa uma lista vazia para armazenar todas as manifestações.

manifestacao_reclamacao = [] # Inicializa uma lista vazia para armazenar todas as reclamações.
manifestacao_elogio  = [] # Inicializa uma lista vazia para armazenar todas os elogios.
manifestacao_sugestao = [] # Inicializa uma lista vazia para armazenar todas as sugestões.

manifestacoes = manifestacao_reclamacao + manifestacao_elogio + manifestacao_sugestao # Combina todas as listas de manifestações em uma única lista.

# Menu --------------------------------------------------------------
def menu():
    """
    Define uma função chamada menu() que exibe um menu de opções para o usuário e executa diferentes funções com base na escolha do usuário.
        1º Exibição do Menu: A função menu() começa imprimindo um menu com várias opções numeradas de 1 a 7. Cada opção corresponde a uma ação diferente que o sistema pode realizar.
        2º Entrada do Usuário: O código então solicita ao usuário que escolha uma opção digitando um número.
        3º Limpeza do Console: Antes de executar a ação correspondente à opção escolhida, a função limpar_console() é chamada para limpar a tela.
        4º Execução da Opção Escolhida: Dependendo da opção escolhida pelo usuário, uma das seguintes funções é chamada:
            - listar_manifestacoes(): Lista todas as manifestações.
            - listar_manifestacoes_tipo(): Lista manifestações por tipo.
            - nova_manifestacao(): Cria uma nova manifestação.
            - quantidade_manifestacoes(): Exibe a quantidade de manifestações.
            - pesquisar_manifestacao(): Pesquisa uma manifestação por código.
            - excluir_manifestacao(): Exclui uma manifestação pelo código.
            - exit(): Sai do sistema.
        5º Opção Inválida: Se o usuário digitar uma opção inválida, uma mensagem de erro é exibida e o menu é mostrado novamente.
    """

    # Exibe o menu de opções para o usuário
    print("""\n     --- MENU DO SISTEMA ---\n
[1] Listagem das manifestações
[2] Listagem de manifestações por tipo
[3] Criar uma nova manifestação
[4] Exibir quantidade de manifestações
[5] Pesquisar uma manifestação por código
[6] Excluir uma manifestação pelo código
[7] Sair do sistema""")

    # Solicita ao usuário que escolha uma opção
    opcao = input("\n   Escolha uma opção: ")
    """
    A variável 'opção' receberá a opção escolhida pelo usuário como uma string,
    pois qualquer que seja o input do usuário, não ocorrerá erro por 'invalid literal'.
    """

    # Limpa o console
    limpar_console()

    # Verifica a opção escolhida pelo usuário e chama a função correspondente
    if opcao == "1":
        listar_manifestacoes() # Lista todas as manifestações

    elif opcao == "2":
        listar_manifestacoes_tipo() # Lista manifestações por tipo

    elif opcao == "3":
        nova_manifestacao() # Cria uma nova manifestação
        
    elif opcao == "4":
        quantidade_manifestacoes() # Exibe a quantidade de manifestações
        
    elif opcao == "5":
        pesquisar_manifestacao() # Pesquisa uma manifestação por código
        
    elif opcao == "6":
        excluir_manifestacao() # Exclui uma manifestação pelo código
        
    elif opcao == "7":
        exit() # Sai do sistema

    else:
        # Informa ao usuário que a opção é inválida e exibe o menu novamente
        print("\nOpção inválida! Tente novamente...\n")
        menu() # Chama a função menu() para exibir ao menu principal novamente

# Limpar console ----------------------------------------------------
def limpar_console():
    """
    Verifica o sistema operacional e executa o comando apropriado para limpar a tela do terminal, seja no Windows (cls) ou em sistemas Unix-like (clear).
        1º Importação do módulo "os":
            O módulo "os" fornece uma maneira de interagir com o sistema operacional.
        2º Execução do comando de limpeza de tela:
            - "os.name" retorna uma string que identifica o sistema operacional. Se for "nt", significa que o sistema operacional é Windows.
            - O comando 'os.system()' executa um comando no terminal do sistema operacional.
            - "cls" é o comando usado para limpar a tela no Windows.
            - "clear" é o comando usado para limpar a tela em sistemas Unix-like (como Linux e macOS).
    """
    
    # Importa o módulo os, que permite interagir com o sistema operacional
    import os

    # Executa um comando do sistema operacional para limpar a tela do console
    os.system("cls" if os.name == "nt" else "clear")

#1) Listagem das Manifestações --------------------------------------
def listar_manifestacoes():
    """
    Lista todas as manifestações registradas, verificando se há manifestações disponíveis e exibindo-as de forma organizada.
        1º Definição da Função listar_manifestacoes():
        2º Combinação de Listas:
            - Combina três listas (manifestacao_reclamacao, manifestacao_elogio e manifestacao_sugestao) em uma única lista chamada manifestacoes.
        3º Verificação de Lista Vazia:
        4º Exibição das Manifestações:
        5º Chamada da Função retornar_ou_sair():
    """

    # Combina todas as manifestações em uma única lista
    manifestacoes = manifestacao_reclamacao + manifestacao_elogio + manifestacao_sugestao

    # Verifica se a lista de manifestações está vazia
    if len(manifestacoes) == 0:
        print("\nNão há manifestações cadastradas.") # Informa que não há manifestações cadastradas
    else:
        print("\n--- LISTAGEM DE MANIFESTAÇÕES ---\n")
        print( 'código da manifestação: ------- manifestação:')
        posicao_codigo = range(len(manifestacoes))  # Usa enumerate para obter o índice e a manifestação
        for item in posicao_codigo:
            print (item + 1,'--------',manifestacoes[item])# Exibe a posição (índice) e o conteúdo da manifestação





    menu() # Volta ao menu após listar as manifestações

    # Chama a função retornar_ou_sair() para permitir que o usuário escolha a próxima ação
    
    menu() # Chama a função menu() para voltar ao menu principal

#2) Listagem de Manifestações por Tipo ------------------------------
def listar_manifestacoes_tipo():
    """
    Permite ao usuário listar manifestações por tipo, retornar ao menu principal ou sair do sistema, garantindo uma navegação intuitiva e organizada.
        1º Exibe um Menu: Mostra opções para listar manifestações por tipo (reclamação, elogio, sugestão), retornar ao menu principal ou sair do sistema.
        2º Recebe a Escolha do Usuário: Solicita ao usuário que escolha uma opção.
        3º Executa Ação Baseada na Escolha:
            - Lista as manifestações do tipo escolhido.
            - Retorna ao menu principal.
            - Sai do sistema.
            - Informa se a opção é inválida e permite tentar novamente.
    """

    # Exibe um menu para o usuário escolher o tipo de manifestação a ser listado
    print("""\n--- LISTAGEM DE MANIFESTAÇÕES POR TIPO ---\n
Informe o tipo de Manifestação\n
[1] Reclamção
[2] Elogio
[3] Sugestão
[4] Retornar
[5] Sair""")

    # Solicita ao usuário que escolha uma opção
    opcao = input("\nDigite uma opção: ")

    # Limpa o console
    limpar_console()

    # Verifica a opção escolhida pelo usuário e executa a ação correspondente
    if opcao == "1":
        # Se o usuário escolher a opção 1, exibe a lista de reclamações
        
        if len(manifestacao_reclamacao) == 0:
            print("\nNão há reclamações cadastradas.") # Informa que não há manifestações cadastradas
        else:
            print("\n--- LISTA DE RECLAMAÇÕES ---\n")
            for item in manifestacao_reclamacao:
                print("-", item)
            
    elif opcao == "2":
        # Se o usuário escolher a opção 2, exibe a lista de elogio

        if len(manifestacao_elogio) == 0:
            print("\nNão há elogios cadastrados.") # Informa que não há manifestações cadastradas
        else:
            print("\n--- LISTA DE ELOGIOS ---\n")
            for item in manifestacao_elogio:
                print("-", item)
            
    elif opcao == "3":
        # Se o usuário escolher a opção 3, exibe a lista de sugestões

        if len(manifestacao_sugestao) == 0:
            print("\nNão há sugestões cadastradas.") # Informa que não há manifestações cadastradas
        else:
            print("\n--- LISTA DE SUGESTÕES ---\n")
            for item in manifestacao_sugestao:
                print("-", item)
    
    elif opcao == "4":
        menu() # Chama a função menu() para voltar ao menu principal

    elif opcao == "5":
        # Se o usuário escolher a opção 5, limpa o console e sai do sistema com a função exit()
        limpar_console()
        exit()
    
    else:
        # Se o usuário digitar uma opção inválida, limpa o console, exibe uma mensagem de erro e chama a função listar_manifestacoes_tipo() novamente para que o usuário possa tentar outra vez
        limpar_console()
        print("\nOpção inválida! Tente novamente...\n")
        listar_manifestacoes_tipo()
    
    # Exibe um menu com duas opções: listar manifestações por tipo novamente ou voltar ao menu principal
    print("""\n[1] Listar novamente
[2] Menu""")
    
    # Solicita ao usuário que escolha uma das opções
    opcao = input("\n   Escolha uma opção: ")
    
    # Verifica a opção escolhida pelo usuário
    if opcao == "1":
        limpar_console() # Limpa a tela do console
        listar_manifestacoes_tipo() # Chama a função listar_manifestacoes_tipo() para listar manifestações por tipo novamente

    elif opcao == "2":
        limpar_console() # Limpa a tela do console
        menu() # Chama a função menu() para voltar ao menu principal

    else:
        # Limpa o console, exibe mensagem de erro e chama a função retornar_ou_sair() novamente para tentar outra vez
        limpar_console()
        print("Opção inválida! Tente novamente...\n")
        listar_manifestacoes_tipo() # Chama a função listar_manifestacoes_tipo()

#3) Criar uma nova Manifestação -------------------------------------
def nova_manifestacao():
    """
    Permite ao usuário criar uma nova manifestação (reclamação, elogio ou sugestão), retornar ao menu principal ou sair do sistema, garantindo uma navegação intuitiva e organizada.
        1º Exibe um Menu: Mostra opções para criar uma nova manifestação (reclamação, elogio, sugestão), retornar ao menu principal ou sair do sistema.
        2º Recebe a Escolha do Usuário: Solicita ao usuário que escolha uma opção.
        3º Executa Ação Baseada na Escolha:
            - Solicita ao usuário que digite a manifestação e a adiciona à lista correspondente.
            - Retorna ao menu principal.
            - Sai do sistema.
            - Informa se a opção é inválida e permite tentar novamente.
    """

    global manifestacoes

    # Exibe um menu para o usuário escolher o tipo de manifestação a ser criada
    print("""\nInforme o tipo de Manifestação que você pretende criar\n
[1] Reclamção
[2] Elogio
[3] Sugestão
[4] Retornar
[5] Sair""")
    
    # Solicita ao usuário que escolha uma opção
    opcao = input("\nDigite uma opção: ")

    # Verifica a opção escolhida pelo usuário e executa a ação correspondente
    if opcao == "1":
        # Se o usuário escolher a opção 1, solicita que ele digite sua reclamação
        print("\nDigite sua reclamação")
        manifestacao_reclamacao.append(input(": ")) # Adiciona a reclamação à lista de reclamações
        manifestacoes.append(manifestacao_reclamacao[-1]) # Adiciona a reclamação à lista geral de manifestações
        
        limpar_console() # Limpa a tela do console

        print(f"\nO código da sua reclamação é {len(manifestacao_reclamacao)}\n") # Exibe o código da reclamação
            
    elif opcao == "2":
        # Se o usuário escolher a opção 2, solicita que ele digite seu elogio
        print("\nDigite seu elogio")
        manifestacao_elogio.append(input(": ")) # Adiciona o elogio à lista de elogios
        manifestacoes.append(manifestacao_elogio[-1]) # Adiciona o elogio à lista geral de manifestações
        
        limpar_console() # Limpa a tela do console

        print(f"\nO código do seu elogio é {len(manifestacao_elogio)}\n") # Exibe o código do elogio
            
    elif opcao == "3":
        # Se o usuário escolher a opção 3, solicita que ele digite sua sugestão
        print("\nDigite sua sugestão")
        manifestacao_sugestao.append(input(": ")) # Adiciona a sugestão à lista de sugestões
        manifestacoes.append(manifestacao_sugestao[-1]) # Adiciona a sugestão à lista geral de manifestações
        
        limpar_console() # Limpa a tela do console

        print(f"\nO código da sua sugestão é {len(manifestacao_sugestao)}\n") # Exibe o código da sugestão
    
    elif opcao == "4":
        # Se o usuário escolher a opção 4, limpa o console e retorna ao menu principal
        limpar_console()
        menu()

    elif opcao == "5":
        # Se o usuário escolher a opção 5, limpa o console e sai do sistema
        limpar_console()
        exit()
    
    else:
        # Se o usuário digitar uma opção inválida, limpa o console, exibe uma mensagem de erro e chama a função novamente
        limpar_console()
        print("\nOpção inválida! Tente novamente...\n")
        nova_manifestacao()
    
    # Exibe um menu com duas opções: criar outra manifestação ou voltar ao menu principal
    print("""\n[1] Criar outra manifestação
[2] Menu""")
    
    # Solicita ao usuário que escolha uma das opções
    opcao = input("\n   Escolha uma opção: ")
    
    # Verifica a opção escolhida pelo usuário
    if opcao == "1":
        limpar_console() # Limpa a tela do console
        nova_manifestacao() # Chama a função nova_manifestacao() para criar outra manifestação

    elif opcao == "2":
        limpar_console() # Limpa a tela do console
        menu() # Chama a função menu() para voltar ao menu principal

    else:
        # Limpa o console, exibe mensagem de erro e chama a função retornar_ou_sair() novamente para tentar outra vez
        limpar_console()
        print("Opção inválida! Tente novamente...\n")
        nova_manifestacao() # Chama a função nova_manifestacao()

#4) Exibir quantidade de manifestações ------------------------------
def quantidade_manifestacoes():
    """
    Conta o número total de manifestações registradas e exibe essa quantidade para o usuário. Em seguida, permite que o usuário escolha a próxima ação, como retornar ao menu principal ou sair do sistema.
        1º Definição da Função quantidade_manifestacoes():
        2º Impressão do Título
        3ª Contagem e Impressão das Manifestações:
            - print(f"Há {len(manifestacoes)} manifestações registradas."): Calcula o número total de manifestações na lista manifestacoes usando len(manifestacoes) e imprime essa quantidade.
        4º Chamada da Função retornar_ou_sair():
    """

    # Imprime um título para a contagem de manifestações
    print(f"\n--- CONTADOR DE MANIFESTAÇÕES ---\n")

    # Imprime a quantidade total de manifestações registradas
    print(f"\nHá {len(manifestacoes)} manifestações registradas.")

    menu() # Chama a função menu() para voltar ao menu principal

#5) Pesquisar uma manifestação por código ---------------------------
def pesquisar_manifestacao():
    """
     Permite ao usuário pesquisar uma manifestação específica por tipo (reclamação, elogio, sugestão) e código. Dependendo da escolha do usuário, a função exibe a manifestação correspondente, retorna ao menu principal ou sai do sistema.
        1º Exibe um Menu: Mostra opções para pesquisar uma manifestação por tipo (reclamação, elogio, sugestão), retornar ao menu principal ou sair do sistema.
        2º Recebe a Escolha do Usuário: Solicita ao usuário que escolha uma opção.
        3º Executa Ação Baseada na Escolha:
            - Solicita o código da manifestação e exibe a manifestação correspondente.
            - Retorna ao menu principal.
            - Sai do sistema.
            - Informa se a opção é inválida e permite tentar novamente.
    """
    
    # Exibe um título e um menu para o usuário escolher o tipo de manifestação a ser pesquisada
    print(f"\n--- BUSCAR MANIFESTAÇÁO ---\n")
    print("""Informe o tipo de Manifestação que você pretende pesquisar\n
[1] Reclamção
[2] Elogio
[3] Sugestão
[4] Retornar
[5] Sair""")
    
    # Solicita ao usuário que escolha uma opção
    opcao = input("\nDigite uma opção: ")

    # Verifica a opção escolhida pelo usuário e executa a ação correspondente
    if opcao == "1":
        # Se o usuário escolher a opção 1, solicita o código da reclamação e exibe a reclamação correspondente
        posicao = int(input("\nInforme o código da manifestação que você procura: "))

        # Verifica se o código informado é válido
        while posicao > len(manifestacao_reclamacao):
            print("\nCódigo não encontrado. Tente novamente!")
            posicao = int(input("\nInforme o código da manifestação que você procura: "))

        print(f"\nA reclamação pesquisada foi:\n. {manifestacao_reclamacao[posicao-1]}") # Exibe a reclamação correspondente ao código fornecido.
            
    elif opcao == "2":
        # Se o usuário escolher a opção 2, solicita o código do elogio e exibe o elogio correspondente
        posicao = int(input("\nInforme o código da manifestação que você procura: "))

        # Verifica se o código informado é válido
        while posicao > len(manifestacao_elogio):
            print("\nCódigo não encontrado. Tente novamente!")
            posicao = int(input("\nInforme o código da manifestação que você procura: "))

        print(f"\nO elogio pesquisado foi:\n. {manifestacao_elogio[posicao-1]}") # Exibe o elogio correspondente ao código fornecido.
            
    elif opcao == "3":
        # Se o usuário escolher a opção 3, solicita o código da sugestão e exibe a sugestão correspondente
        posicao = int(input("\nInforme o código da manifestação que você procura: "))

        # Verifica se o código informado é válido
        while posicao > len(manifestacao_sugestao):
            print("\nCódigo não encontrado. Tente novamente!")
            posicao = int(input("\nInforme o código da manifestação que você procura: "))

        print(f"\nA seugestão pesquisada foi:\n. {manifestacao_sugestao[posicao-1]}") # Exibe a sugestão correspondente ao código fornecido.
    
    elif opcao == "4":
        # Se o usuário escolher a opção 4, limpa o console e retorna ao menu principal
        limpar_console()
        menu() # Chama a função menu() para voltar ao menu principal

    elif opcao == "5":
        # Se o usuário escolher a opção 5, limpa o console e sai do sistema
        limpar_console()
        exit()
    
    else:
        # Se o usuário digitar uma opção inválida, limpa o console, exibe uma mensagem de erro e chama a função novamente
        limpar_console()
        print("\nOpção inválida! Tente novamente...\n")
        nova_manifestacao()
    
    # Exibe um menu com duas opções: Nova pesquisa ou voltar ao menu principal
    print("""\n[1] Nova pesquisa
[2] Menu""")
    
    # Solicita ao usuário que escolha uma das opções
    opcao = input("\n   Escolha uma opção: ")
    
    # Verifica a opção escolhida pelo usuário
    if opcao == "1":
        limpar_console() # Limpa a tela do console
        pesquisar_manifestacao() # Chama a função pesquisar_manifestacao() para pesquisar novamente

    elif opcao == "2":
        limpar_console() # Limpa a tela do console
        menu() # Chama a função menu() para voltar ao menu principal

    else:
        # Limpa o console, exibe mensagem de erro e chama a função retornar_ou_sair() novamente para tentar outra vez
        limpar_console()
        print("Opção inválida! Tente novamente...\n")
        pesquisar_manifestacao() # Chama a função pesquisar_manifestacao()

#6) 6) Excluir uma Manifestação pelo Código -------------------------
def excluir_manifestacao():
    """
    Organiza a exclusão de manifestações de forma clara e interativa.
        1º Exibe um Menu: Mostra opções para excluir uma manifestação por tipo (reclamação, elogio, sugestão), retornar ao menu principal ou sair do sistema.
        2º Recebe a Escolha do Usuário: Solicita ao usuário que escolha uma opção.
        3º Executa Ação Baseada na Escolha:
            - Solicita o código da manifestação a ser excluída e confirma a exclusão.
            - Retorna ao menu principal.
            - Sai do sistema.
            - Informa se a opção é inválida e permite tentar novamente.
    """

    # Exibe um título para a seção de exclusão de manifestações
    print(f"\n--- EXCLUIR MANIFESTAÇÁO ---\n")

    # Exibe um menu para o usuário escolher o tipo de manifestação a ser excluída
    print("""\nInforme o tipo de Manifestação que você pretende excluir\n
[1] Reclamção
[2] Elogio
[3] Sugestão
[4] Retornar
[5] Sair""")
    
    # Solicita ao usuário que escolha uma opção
    opcao = input("\nDigite uma opção: ")

    # Verifica a opção escolhida pelo usuário e executa a ação correspondente
    if opcao == "1":
        # Se o usuário escolher a opção 1, solicita o código da reclamação a ser excluída
        posicao = int(input("\nInforme o código da reclamação que você pretende excluir: "))

        # Verifica se o código informado é válido
        while posicao > len(manifestacao_reclamacao):
            print("\nCódigo não encontrado. Tente novamente!")
            posicao = int(input("\nInforme o código da reclamação que você pretende excluir: "))
        
        # Solicita confirmação do usuário para excluir a reclamação
        confirmar = input(f"\nO código informado foi {posicao}. Digite 's' para confirmar e 'n' para corrigir: ")
                
        if confirmar == "s":
            del manifestacao_reclamacao[posicao-1] # Exclui a reclamação da lista
        elif confirmar == "n":
            excluir_manifestacao() # Chama a função novamente para corrigir o código
        else:
            limpar_console()
            print("\nOpção inválida! Tente novamente...\n")
            excluir_manifestacao()

    elif opcao == "2":
        # Se o usuário escolher a opção 2, solicita o código do elogio a ser excluído
        posicao = int(input("Informe o código do elogio que você pretende excluir: "))
        
        # Verifica se o código informado é válido
        while posicao > len(manifestacao_elogio):
            print("Código não encontrado. Tente novamente!")
            posicao = int(input("Informe o código da reclamação que você pretende excluir: "))

        # Solicita confirmação do usuário para excluir o elogio
        confirmar = input(f"O código informado foi {posicao}. Digite 's' para confirmar e 'n' para corrigir: ")
        
        if confirmar == "s":
            del manifestacao_elogio[posicao-1] # Exclui o elogio da lista
        elif confirmar == "n":
            excluir_manifestacao() # Chama a função novamente para corrigir o código
        else:
            limpar_console()
            print("Opção inválida! Tente novamente...\n")
            excluir_manifestacao()

    elif opcao == "3":
        # Se o usuário escolher a opção 3, solicita o código da sugestão a ser excluída
        posicao = int(input("Informe o código da sugestão que você pretende excluir: "))
        
        # Verifica se o código informado é válido
        while posicao > len(manifestacao_sugestao):
            print("Código não encontrado. Tente novamente!")
            posicao = int(input("Informe o código da reclamação que você pretende excluir: "))

        # Solicita confirmação do usuário para excluir a sugestão
        confirmar = input(f"O código informado foi {posicao}. Digite 's' para confirmar e 'n' para corrigir: ")
        
        if confirmar == "s":
            del manifestacao_sugestao[posicao-1] # Exclui a sugestão da lista
        elif confirmar == "n":
            excluir_manifestacao() # Chama a função novamente para corrigir o código
        else:
            limpar_console()
            print("Opção inválida! Tente novamente...\n")
            excluir_manifestacao()

    elif opcao == "4":
        # Se o usuário escolher a opção 4, limpa o console e retorna ao menu principal
        limpar_console()
        menu()

    elif opcao == "5":
        # Se o usuário escolher a opção 5, limpa o console e sai do sistema
        limpar_console()
        exit()
    
    else:
        # Se o usuário digitar uma opção inválida, limpa o console, exibe uma mensagem de erro e chama a função novamente
        limpar_console()
        print("Opção inválida! Tente novamente...\n")
        excluir_manifestacao()
    
    # Informa que a manifestação foi excluída com sucesso e chama a função retornar_ou_sair()
    print(f"\nA manifestação foi excluída com sucesso!\n")
    
    # Exibe um menu com duas opções: excluir outra manifestação ou voltar ao menu principal
    print("""\n[1] Excluir outra manifestação
[2] Menu""")
    
    # Solicita ao usuário que escolha uma das opções
    opcao = input("\n   Escolha uma opção: ")
    
    # Verifica a opção escolhida pelo usuário
    if opcao == "1":
        limpar_console() # Limpa a tela do console
        excluir_manifestacao() # Chama a função excluir_manifestacao() para excluir outra manifestação

    elif opcao == "2":
        limpar_console() # Limpa a tela do console
        menu() # Chama a função menu() para voltar ao menu principal

    else:
        # Limpa o console, exibe mensagem de erro e chama a função retornar_ou_sair() novamente para tentar outra vez
        limpar_console()
        print("Opção inválida! Tente novamente...\n")
        excluir_manifestacao() # Chama a função excluir_manifestacao()

limpar_console() # Limpa a tela do console
menu() # Chama a função menu() para exibir o menu principal