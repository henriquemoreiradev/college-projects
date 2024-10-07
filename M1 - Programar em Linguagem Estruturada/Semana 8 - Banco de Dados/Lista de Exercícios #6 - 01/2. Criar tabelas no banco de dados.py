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

#   Criar a tabela Alunos
cursor.execute("""
    CREATE TABLE Alunos (
        MAT int,
	    nome varchar(100),
	    endereço varchar(100),
  	    cidade varchar(100),
	    primary key(MAT)
    );
""")

#   Criar a tabela Disciplinas
cursor.execute("""
    CREATE TABLE Disciplinas (
	    COD_DISC int,
	    nome_disc varchar(100),
	    carga_hor int,
	    primary key(COD_DISC)
    );
""")

#   Criar a tabela Professores
cursor.execute("""
    CREATE TABLE Professores (
	    COD_PROF int,
	    nome varchar(100),
	    endereco varchar(100),
	    cidade varchar(100),
	    primary key(COD_PROF)
    );
""")

#   Fechar o cursor e a conexão
cursor.close()
db.close()