class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_carvenas(self):
        self.especie = 'Homo Neanderthalensis'
        return self

if __name__ == '__main__':
    jose = Humano('José')
    grokn = Humano('Grokn').das_carvenas()

    print(f'Humano.especie: {Humano.especie}')
    print(f'jose.especie: {jose.especie}')
    print(f'grokn.especie: {grokn.especie}')