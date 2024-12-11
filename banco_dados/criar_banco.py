from mysql.connector import connect

conexao = connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='root'
)

cursor = conexao.cursor()
# if not exists
cursor.execute('create database if not exists agenda')