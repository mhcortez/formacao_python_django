import sqlite3

conn = sqlite3.connect('mydatabase.db')

novo = input("Digite o novo valor: ")
#atualizar dados na tabela
conn.execute(f"UPDATE stocks SET price = {novo}  WHERE symbol = 'RHAT'")

conn.commit()

conn.close()    
