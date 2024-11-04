from funcoes_banco_de_dados import *

def verificação():
    try:
        filtrar_modalidades('olimpiadas', 'anos')
        pesquisa_banco_de_dados('cadastro', 'usuarios')
        return 1
    except mysql.connector.errors.DatabaseError:
        return 0

def verificar_usuario(usuario, senha):
    resultado = pesquisa_banco_de_dados('cadastro', 'usuarios')
    for i in resultado:
            if usuario == i[1] and senha == i[2]:
                if i[3] == 0:
                    trocar_ativo(usuario, 1)
                    return 1
                else:
                    return 2
    return 0        
    
def trocar_ativo(usuario, valor):
    editar_banco_de_dados('cadastro', 'usuarios', 'nome', 'ativo', usuario, valor)

def usuario_ativo_sem_():
    resultado = pesquisa_banco_de_dados('cadastro', 'usuarios')
    for i in resultado:
        if i[4] == 1:
            return i[1]
    return 0

def usuario_ativo():
    resultado = pesquisa_banco_de_dados('cadastro', 'usuarios')
    for i in resultado:
        if i[4] == 1:
            nome = i[1].replace(' ', '_')
            return nome
    return 0

def criar_cadastro(nome, senha):
    resultado = pesquisa_banco_de_dados('cadastro', 'usuarios')
    for i in resultado:
            if i[1] == nome:
                return 1
    
    inserir_no_usuario_banco_de_dados('cadastro', 'usuarios', nome, senha)
    nome = nome.replace(' ', '_')
    criar_nova_tabela('cadastro', nome)
    return 0

def mudar_senha(nome, senha):
    resultado = pesquisa_banco_de_dados('cadastro', 'usuarios')
    for i in resultado:
        if i[1] == nome:
            editar_banco_de_dados('cadastro', 'usuarios', 'nome', 'senha', nome, senha)
    return 1

def pesquisar_dados(pesquisa):
    resultado = pesquisa_banco_de_dados('olimpiadas', f'{pesquisa}')
    colunas_de_tv_dados = filtrar_modalidades('olimpiadas', f'{pesquisa}')

    valores = ['']*4
    valores[0] = colunas_de_tv_dados

    cont = 1
    for paises in resultado:
        pais = []
        for i in paises:
            pais.append(i)
        pais.pop(0)
        valores[cont] = pais
        cont += 1

    return valores

def pesquisar_dados_favoritos(pesquisa):
    resultado = pesquisa_banco_de_dados('olimpiadas', f'{pesquisa}')
    colunas_de_tv_dados = filtrar_modalidades('olimpiadas', f'{pesquisa}')

    valores = ['']*4
    valores[0] = colunas_de_tv_dados

    cont = 1
    for paises in resultado:
        pais = []
        for i in paises:
            pais.append(i)
        pais.pop(0)
        valores[cont] = pais
        cont += 1

    return valores

def add_favorito(pesquisa):
    ano = pesquisa[:4]
    modalidade = pesquisa[5:]

    resultado = pesquisa_banco_de_dados('cadastro', f'favoritos_{usuario_ativo()}')
    
    for i in resultado:
        if ano in i and modalidade in i:
            return 0
    
    inserir_favorito_banco_de_dados('cadastro', f'favoritos_{usuario_ativo()}', ano, modalidade)
    return 1

def remover_favorito(pesquisa):
    ano = pesquisa[:4]
    modalidade = pesquisa[5:]
    remover_favorito_banco_de_dados('cadastro', f'favoritos_{usuario_ativo()}', ano, modalidade)
    return 1

def recarregar(usuario):
    return pesquisa_banco_de_dados('cadastro', f'favoritos_{usuario}')

def criar_tela_de_filtragem():
    dados = [0, 1, 2]
    dados[0] = pesquisa_banco_de_dados('olimpiadas', 'anos')
    dados[1] = filtrar_modalidades('olimpiadas', 'anos')
    
    anos_olimpiada = []
    for i in dados[0]:
        anos_olimpiada.append(i[0])

    dados[2] = anos_olimpiada

    return dados

def add_novo_ano(ano):
    resultado = pesquisa_banco_de_dados('olimpiadas', 'anos')
    for i in resultado:
        if i[0] == ano:
            return 0
    inserir_na_tabela_anos('olimpiadas', 'anos', ano)
    return 1

def remover_estatistica(ano, modalidade, estatistica):
    estatistica = estatistica.replace(' ', '_')
    dados = [0, 1]
    dados[0] = pesquisa_banco_de_dados('olimpiadas', 'anos')
    dados[1] = filtrar_modalidades('olimpiadas', 'anos')
    
    try:
        int(ano)
    except ValueError:
        return 0

    for i in range(0, len(dados[0])):
        if int(ano) == dados[0][i][0]:
            for j in range(0, len(dados[1])):
                if dados[1][j] == modalidade and dados[0][i][j + 1] == 1:
                    resultado = ano + '_' + modalidade
                    resultado = pesquisar_dados(resultado)
                    for k in resultado[0]:
                        if estatistica == k:
                            remover_estatistica_dados('olimpiadas', f'{ano}_{modalidade}', estatistica)
                            return 4
                    return 3
            return 2
    return 1

def remover_tabela(ano, modalidade):
    dados = [0, 1]
    dados[0] = pesquisa_banco_de_dados('olimpiadas', 'anos')
    dados[1] = filtrar_modalidades('olimpiadas', 'anos')

    try:
        int(ano)
    
    except ValueError:
        return 0

    for i in range(0, len(dados[0])):
        if int(ano) == dados[0][i][0]:
            for j in range(0, len(dados[1])):
                if modalidade == dados[1][j] and dados[0][i][j + 1] == 1:
                    remover_tabela_dados('olimpiadas', f'{ano}_{modalidade}', ano, modalidade)
                    return 4
            return 2
    return 1

def remover_ano(ano):
    dados = [0, 1]
    dados[0] = pesquisa_banco_de_dados('olimpiadas', 'anos')
    dados[1] = filtrar_modalidades('olimpiadas', 'anos')
    try:
        int(ano)
    
    except ValueError:
        return 0
    for i in range(0, len(dados[0])):
        if int(ano) == dados[0][i][0]:
            for j in range(0, len(dados[1])):
                if dados[0][i][j + 1] == 1:
                    remover_tabela_dados('olimpiadas', f'{ano}_{dados[1][j]}', ano, f'{dados[1][j]}')

            remover_ano_dados('olimpiadas', ano)
            return 4
    return 1

def pesquisa_dados(resultado):
    valor = 0
    lista = ['', '', '', '']
    
    for i in resultado:
        if i != '_' and valor == 0:
            lista[0] += i
        
        elif i != '_' and valor == 1:
            lista[1] += i

        elif i != '_' and valor == 2:
            lista[2] += i

        elif i != '_' and valor == 3:
            lista[3] += i
        
        else:
            valor += 1
        
    return lista