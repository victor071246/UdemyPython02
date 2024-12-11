from db import nova_conexao

sql = 'select tel, nome from contatos limit 10 offset 3'

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)
    
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())