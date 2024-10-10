import SqliteFuncoes
import Conexao

conn = Conexao.connect_to_database()

#SqliteFuncoes.AlteraBanco(conn,'stocks', 'qty', '25.5', 'symbol', 'IBM')
SqliteFuncoes.DeletaBanco(conn,'stocks', 'symbol','FB')
