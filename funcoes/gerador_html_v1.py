def tag_bloco(texto, classe='success'):
    return f'<div class="{classe}">{texto}</div>'


if __name__ == '__main__':
    # Testes (assertions)
    assert tag_bloco('Incluído com sucesso!') == \
    '<div class="sucess">Inclu´do com sucesso!<div>'
    assert tag_bloco('Impossível excluir!', 'error') == '<div class="erro">Impossível excluir!<div>'