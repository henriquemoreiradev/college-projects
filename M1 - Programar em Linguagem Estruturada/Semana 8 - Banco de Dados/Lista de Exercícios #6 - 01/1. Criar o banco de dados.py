import mysql.connector

#   Conectar ao servidor MySQL
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "12345",
)

#   Criar um cursor
cursor = db.cursor()

#   Criar um banco de dados
cursor.execute("CREATE DATABASE Lista_de_Exercícios_6_1")

#   Fechar o cursor e a conexão
cursor.close()
db.close()