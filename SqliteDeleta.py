import sqlite3

conn = sqlite3.connect('mydatabase.db')

conn.execute("DELETE from stocks where symbol = 'IBM'")

conn.commit()
conn.close()
