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

#   Executar a instrução UPDATE para atualizar a carga horária das disciplinas
cursor.execute("UPDATE Disciplinas SET carga_hor = 80 WHERE carga_hor = 60")

#   Confirmar a transação
db.commit()

#   Fechar o cursor e a conexão
cursor.close()
db.close()