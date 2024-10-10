import sqlite3

#criar conexao com banco de dados
conn = sqlite3.connect('mydatabase.db')

#Inserir dados na tabela
conn.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
conn.execute("INSERT INTO stocks VALUES ('2006-03-28','BUY','IBM',1000,45.00)")
conn.execute("INSERT INTO stocks VALUES ('2006-04-06','SELL','IBM',500,53.00)")
conn.execute("INSERT INTO stocks VALUES ('2006-03-06','SELL','FB',700,63.00)")

#salvar alterações
conn.commit()

#fechar conexão com o banco de dados
conn.close()