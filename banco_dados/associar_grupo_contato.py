from mysql.connector.errors import ProgrammingError
from db import nova_conexao

selecionar_grupo = 'select id from grupos where descricao = %s'
atualizar_contato = 'update contatos set grupo_id = %s where nome = %s'

contato_grupo = {
    '...': 'Casa',
    '...': 'Trabalho',
    'Ana': 'Casa',
    'Bia': 'Trabalho',
    'Lucas Yuri': 'Casa',
    'Lu': 'Casa',
    'Gui': 'Trabalho',
    'Beca': 'Trabalho',
    'Pedro': 'Trabalho',
    'Luca': 'Trabalho',
    'Luca': 'Casa',
}

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        for contato, grupo in contato_grupo.items():
            cursor.execute(selecionar_grupo, (grupo,))
            grupo_id = cursor.fetchone()[0]
            cursor.execute(atualizar_contato, (grupo_id, contato))
            conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print('contatos associados')