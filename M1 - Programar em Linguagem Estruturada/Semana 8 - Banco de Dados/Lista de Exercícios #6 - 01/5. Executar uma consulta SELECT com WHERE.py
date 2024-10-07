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

#   Executar uma consulta SELECT com condições específicas usando a cláusula WHERE
cursor.execute("SELECT * FROM Alunos WHERE cidade = 'Campina Grande'")

#   Recuperar todos os resultados
resultados = cursor.fetchall()

#   Iterar sobre os resultados e imprimir
for linha in resultados:
    print(linha)

#   Fechar o cursor e a conexão
cursor.close()
db.close()