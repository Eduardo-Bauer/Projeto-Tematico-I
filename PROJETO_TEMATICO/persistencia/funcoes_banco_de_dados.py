import mysql.connector #pip install mysql-connector-python

def pesquisa_banco_de_dados(database, tabela):
    banco_de_dados = mysql.connector.connect(host= 'localhost', user= 'root', password= '', database= f'{database}')
    cursor = banco_de_dados.cursor() 
    comando = f'SELECT * FROM {tabela}'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    return resultado

def filtrar_modalidades(database, tabela):
    banco_de_dados = mysql.connector.connect(host= 'localhost', user= 'root', password= '', database= f'{database}')
    cursor = banco_de_dados.cursor() 
    comando = f'SHOW COLUMNS FROM {database}.{tabela}'
    cursor.execute(comando)
    modalidades_no_banco_de_dados = cursor.fetchall()
    esportes_do_banco_de_dados = []
    for i in modalidades_no_banco_de_dados:
        esportes_do_banco_de_dados.append(i[0])

    esportes_do_banco_de_dados.pop(0)
    return esportes_do_banco_de_dados

def criar_nova_tabela(databese, nome_da_tabela):
    banco_de_dados = mysql.connector.connect(host= 'localhost', user= 'root', password= '', database= f'{databese}')
    cursor = banco_de_dados.cursor() 
    comando = f'CREATE TABLE favoritos_{nome_da_tabela}(id int primary key auto_increment, ano varchar(50), modalidade varchar(50))'
    cursor.execute(comando)
    banco_de_dados.commit()

def inserir_no_usuario_banco_de_dados(database, tabela, nome, senha):
    banco_de_dados = mysql.connector.connect(host= 'localhost', user= 'root', password= '', database= f'{database}')
    comando = f'INSERT INTO {tabela} (nome, senha, adm) VALUES ("{nome}", "{senha}", {False})'
    cursor = banco_de_dados.cursor() 
    cursor.execute(comando)
    banco_de_dados.commit()

def editar_banco_de_dados(database, tabela, onde_mudar, oque_mudar, nome, senha):
    banco_de_dados = mysql.connector.connect(host= 'localhost', user= 'root', password= '', database= f'{database}')
    comando = f'UPDATE {tabela} SET {oque_mudar} = "{senha}" WHERE {onde_mudar} = "{nome}"'
    cursor = banco_de_dados.cursor() 
    cursor.execute(comando)
    banco_de_dados.commit()

def inserir_favorito_banco_de_dados(database, tabela, ano, modalidade):
    banco_de_dados = mysql.connector.connect(host= 'localhost', user= 'root', password= '', database= f'{database}')
    comando = f'INSERT INTO {tabela} (ano, modalidade) VALUES ("{ano}", "{modalidade}")'
    cursor = banco_de_dados.cursor() 
    cursor.execute(comando)
    banco_de_dados.commit()

def remover_favorito_banco_de_dados(database, tabela, ano, modalidade):
    banco_de_dados = mysql.connector.connect(host= 'localhost', user= 'root', password= '', database= f'{database}')
    comando = f'DELETE FROM {database}.{tabela} WHERE (ano = "{ano}" and modalidade = "{modalidade}")'
    cursor = banco_de_dados.cursor() 
    cursor.execute(comando)
    banco_de_dados.commit()
