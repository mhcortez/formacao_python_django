import sqlite3

#criar conexao com banco de dados
conn = sqlite3.connect('mydatabase.db')

#selecionar dados da tabela
cursor = conn.execute("Select * from stocks")

#iterar sobre os dados retornados
for row in cursor:
    print(row)
    
#fechar conexão com o banco de dados
conn.close()