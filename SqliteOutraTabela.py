import sqlite3

conn = sqlite3.connect('mydatabase.db')

#criar a tabela companies
conn.execute('''CREATE TABLE companies ( symbol text, name text, sector text)''')

#inserir dados na tabela companies
conn.execute("INSERT INTO companies VALUES ('GOOG', 'Google Inc.', 'Technology')")
conn.execute("INSERT INTO companies VALUES ('MSFT', 'Microsoft Corporation', 'Technology')")
conn.execute("INSERT INTO companies VALUES ('AAPL', 'Apple Inc.', 'Technology')")
conn.execute("INSERT INTO companies VALUES ('AMZN', 'Amazon.com Inc.', 'Retail')")
conn.execute("INSERT INTO companies VALUES ('FB', 'Facebook Inc.', 'Technology')")
conn.execute("INSERT INTO companies VALUES ('RHAT', 'Red Hat Inc', 'Software')")
conn.execute("INSERT INTO companies VALUES ('IBM', 'IBM Corporation', 'Technology')")

conn.commit()
conn.close()
