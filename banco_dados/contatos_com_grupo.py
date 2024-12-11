from db import nova_conexao
from mysql.connector.errors import ProgrammingError

sql = """
    select
    grupos.descricao as grupo,
    contatos.nome as nome
    from contatos
    inner join grupos on contatos.grupo_id = grupos.id
    order by grupo, nome
"""

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(sql)
        contatos = cursor.fetchall()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        for contato in contatos:
            print(f'{contato["grupo"]}? {contato["nome"]}')