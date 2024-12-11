from collections import defaultdict
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
        try:
            cursor.execute(sql)
            contatos = cursor.fetchall()
        finally:
            cursor.close()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        agrupados = defaultdict(list)
        for contato in contatos:
            agrupados[contato['grupo']]
            
        print(agrupados)