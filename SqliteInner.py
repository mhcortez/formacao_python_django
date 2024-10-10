import sqlite3  

conn = sqlite3.connect('mydatabase.db')

cursor = conn.execute("SELECT stocks.date , stocks.trans , stocks.qty, stocks.price, companies.name \
                      FROM stocks \
                      INNER JOIN companies \
                      ON stocks.symbol = companies.symbol")
for row in cursor:
    print(row)

conn.close()
