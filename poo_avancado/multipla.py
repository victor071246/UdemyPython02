class Animal:
    @property
    def capacidade(self):
        return ('dormir', 'comer', 'beber')
    
class Homem(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('amar', 'falar', 'estudar')
    
class Aranha(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('fazer teia', 'andar pelas paredes')
    
class HomemAranha(Homem, Aranha):
    @property
    def capacidades(self):
        return super().capacidades + ('bater em bandidos', 'atirar teias entre prédios')
    
if __name__ == '__main__':
    jhon = Homem()
    print(f'Jhon: {jhon.capacidades}')

    peter = HomemAranha()
    print(f'Peter Parker: {peter.capacidades}')