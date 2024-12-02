pessoas_csv = 'C://Users//victo//OneDrive//Área de Trabalho//programação//PythonUdemy02//manipulacao_arquivos//pessoas.csv'

pessoas_txt = 'C://Users//victo//OneDrive//Área de Trabalho//programação//PythonUdemy02//manipulacao_arquivos//pessoas.txt'


with open(pessoas_csv) as arquivo:
    with open(pessoas_txt, 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {}, Idade: {}'.format(*pessoa), file=saida)


if arquivo.closed:
    print('Arquivo já foi fechado')

if saida.closed:
    print('Arquivo de saída já foi fechado')