import mysql.connector #pip install mysql-connector-python

def pesquisa_banco_de_dados(database, tabela):
    banco_de_dados = mysql.connector.connect(host= 'localhost', user= 'root', password= '', database= f'{database}')
    cursor = banco_de_dados.cursor() 
    comando = f'SELECT * FROM {tabela}'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    return resultado

def filtrar_modalidades(databese, tabela):
    banco_de_dados = mysql.connector.connect(host= 'localhost', user= 'root', password= '', database= f'{databese}')
    cursor = banco_de_dados.cursor() 
    comando = f'SHOW COLUMNS FROM {databese}.{tabela}'
    cursor.execute(comando)
    modalidades_no_banco_de_dados = cursor.fetchall()
    esportes_do_banco_de_dados = []
    for i in modalidades_no_banco_de_dados:
        esportes_do_banco_de_dados.append(i[0])

    esportes_do_banco_de_dados.pop(0)
    return esportes_do_banco_de_dados

def inserir_no_usuario_banco_de_dados(databese, tabela, nome, senha):
    banco_de_dados = mysql.connector.connect(host= 'localhost', user= 'root', password= '', database= f'{databese}')
    comando = f'INSERT INTO {tabela} (nome, senha, adm) VALUES ("{nome}", "{senha}", {False})'
    cursor = banco_de_dados.cursor() 
    cursor.execute(comando)
    banco_de_dados.commit()

def editar_senha_no_banco_de_dados(databese, tabela, nome, senha):
    banco_de_dados = mysql.connector.connect(host= 'localhost', user= 'root', password= '', database= f'{databese}')
    comando = f'UPDATE usuarios SET senha = "{senha}" WHERE nome = "{nome}"'
    cursor = banco_de_dados.cursor() 
    cursor.execute(comando)
    banco_de_dados.commit()