import sqlite3

#criar conexao com banco de dados
conn = sqlite3.connect('mydatabase.db')

#criar uma tabela
conn.execute('''CREATE TABLE IF NOT EXISTS stocks (date text, trans text, symbol text, qty real, price real)''')

#salvar alterações
conn.commit()

#fechar conexão com o banco de dados
conn.close()