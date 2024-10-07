import mysql.connector

#   Conectar ao servidor MySQL
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "12345",
    database="Lista_de_Exercícios_6_1"
)

#   Criar um cursor
cursor = db.cursor()

#   Inserir dados na tabela Alunos
cursor.execute("""
    INSERT INTO Alunos (MAT, nome, endereço, cidade)
    VALUES (1,"Romero Farias","Rua A", "Campina Grande")
""")

cursor.execute("""
    INSERT INTO Alunos (MAT, nome, endereço, cidade)
    VALUES (2,"Elaine Moreira","Rua B", "João Pessoa")
""")

cursor.execute("""
    INSERT INTO Alunos (MAT, nome, endereço, cidade)
    VALUES (3,"Daniel Abella","Rua C", "Patos")
""")

#   Inserir dados na tabela Disciplinas
cursor.execute("""
    INSERT INTO Disciplinas (COD_DISC, nome_disc, carga_hor)
    VALUES (4,"PYTHON",60);
""")
cursor.execute("""
    INSERT INTO Disciplinas (COD_DISC, nome_disc, carga_hor)
    VALUES (5,"JAVA",80);
""")
cursor.execute("""
    INSERT INTO Disciplinas (COD_DISC, nome_disc, carga_hor)
    VALUES (6,"SQL",100);
""")

#   Inserir dados na tabela Disciplinas
cursor.execute("""
    INSERT INTO Professores (COD_PROF, nome, endereco, cidade)
    VALUES (7,"Daniel","Rua D", "Campina Grande");
""")
cursor.execute("""
    INSERT INTO Professores (COD_PROF, nome, endereco, cidade)
    VALUES (8,"Abella","Rua E", "João Pessoa");
""")
cursor.execute("""
    INSERT INTO Professores (COD_PROF, nome, endereco, cidade)
    VALUES (9,"Zarac","Rua F", "Patos");
""")

#   Confirmar a transação
db.commit()

#   Fechar o cursor e a conexão
cursor.close()
db.close()