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

#   Executar a instrução DELETE para excluir alunos com sobrenome 'Abella'
cursor.execute("DELETE FROM Alunos WHERE nome LIKE '%Abella%'")

#   Confirmar a transação
db.commit()

#   Fechar o cursor e a conexão
cursor.close()
db.close()