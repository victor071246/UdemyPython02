from db import nova_conexao

sql = 'select nome, id from contatos order by nome desc'

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)
    
    print('\n'.join(str(registro) for registro in cursor))