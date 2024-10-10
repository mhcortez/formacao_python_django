import sqlite3

def AlteraBanco (conn, table_name, column_name, new_value, condition_column, condition_value):
    try:
        cursor = conn.cursor()
        cursor.execute(f"UPDATE {table_name} SET {column_name} = ? WHERE {condition_column} = ?", (new_value, condition_value))
        conn.commit()
        print(f"Registro atualizado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao atualizar registro: {e}")


def DeletaBanco (conn, table_name, condition_column, condition_value):
    try:
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {table_name} WHERE {condition_column} = ?", (condition_value,))
        conn.commit()
        print(f"Registro deletado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao deletar registro: {e}")