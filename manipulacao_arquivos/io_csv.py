import csv

pessoas_csv = 'C://Users//victo//OneDrive//Área de Trabalho//programação//PythonUdemy02//manipulacao_arquivos//pessoas.csv'

pessoas_txt = 'C://Users//victo//OneDrive//Área de Trabalho//programação//PythonUdemy02//manipulacao_arquivos//pessoas.txt'

with open(pessoas_csv) as entrada:
    for pessoa in csv.reader(entrada):
        print('Nome: {} | Idade: {}'.format(*pessoa))