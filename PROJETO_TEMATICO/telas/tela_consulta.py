from tkinter import *
from tkinter import ttk
import tkinter as tk
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'persistencia')))
from funcoes_banco_de_dados import * # type: ignore

######### INTERFACE #########
janela_de_consulta = Tk()
janela_de_consulta.title('ScoreGame')
janela_de_consulta.geometry('1200x840')
janela_de_consulta.config(background='white')

######### LABELS #########
quadro_de_pesquisa = LabelFrame(janela_de_consulta, background='#d9d9d9')
quadro_de_pesquisa.grid(row=0, column=0)

quadro_de_dados = LabelFrame(janela_de_consulta, background='white', borderwidth=0)
quadro_de_dados.grid(row=0, column=1, padx=(50, 0), pady=(0, 0))

######### STYLES #########
from styles import * # type: ignore

######### FUNCOES #########
def fechar():
    usuario = usuario_ativo()
    editar_banco_de_dados('cadastro', 'usuarios', 'nome', 'ativo', usuario, 0) # type: ignore
    janela_de_consulta.destroy()

def usuario_ativo():
    resultado = pesquisa_banco_de_dados('cadastro', 'usuarios') # type: ignore
    for i in resultado:
        if i[4] == 1:
            return i[1]
    return 0

def demostracao_dos_dados():
    pesquisa = tv_filtragem.focus()
    if len(pesquisa) > 4:
        for item in tv_dados.get_children():
            tv_dados.delete(item)
        titulo['text'] = f'{pesquisa}'
        resultado = pesquisa_banco_de_dados('olimpiadas', f'{pesquisa}') # type: ignore
        colunas_de_tv_dados = filtrar_modalidades('olimpiadas', f'{pesquisa}') # type: ignore

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

        for i in range(0, len(valores[0])):
            tv_dados.insert('', 'end', values=(valores[0][i], valores[1][i], valores[2][i], valores[3][i]))

    else:
        titulo['text'] = 'TITULO'

def demostracao_dos_dados_favoritos():
    try:
        resultado = pesquisa_banco_de_dados('cadastro', f'favoritos_{usuario_ativo()}') # type: ignore
        pesquisa = tv_favoritos.focus()
        for item in tv_dados.get_children():
            tv_dados.delete(item)

        titulo['text'] = f'{pesquisa}'

        resultado = pesquisa_banco_de_dados('olimpiadas', f'{pesquisa}') # type: ignore
        colunas_de_tv_dados = filtrar_modalidades('olimpiadas', f'{pesquisa}') # type: ignore

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

        for i in range(0, len(valores[0])):
            tv_dados.insert('', 'end', values=(valores[0][i], valores[1][i], valores[2][i], valores[3][i]))
    except mysql.connector.errors.ProgrammingError: # type: ignore
        titulo['text'] = 'TITULO'

def favoritar():
    try:
        pesquisa = tv_filtragem.focus()
        ano = ''
        for i in pesquisa:
            if i == '_':
                break
            else:
                ano += i
        modalidade = pesquisa[len(ano)+1:]

        resultado = pesquisa_banco_de_dados('cadastro', f'favoritos_{usuario_ativo()}') # type: ignore
        cont = 0
        for i in resultado:
            if ano in i and modalidade in i:
                cont = 1
                break
        if cont == 0:
            inserir_favorito_banco_de_dados('cadastro', f'favoritos_{usuario_ativo()}', ano, modalidade) # type: ignore
            recarregar_favoritos()
    except mysql.connector.errors.ProgrammingError: # type: ignore
        titulo['text'] = 'TITULO'

def desfavoritar():
    try:
        pesquisa = tv_favoritos.focus()
        ano = pesquisa[:4]
        modalidade = pesquisa[5:]
        remover_favorito_banco_de_dados('cadastro', f'favoritos_{usuario_ativo()}', ano, modalidade) # type: ignore
        recarregar_favoritos()
    except mysql.connector.errors.ProgrammingError: # type: ignore
        titulo['text'] = 'TITULO'

def recarregar_favoritos():
    usuario = usuario_ativo()
    for item in tv_favoritos.get_children():
            tv_favoritos.delete(item)
    resultado = pesquisa_banco_de_dados('cadastro', f'favoritos_{usuario}') # type: ignore
    for i in resultado:
        tv_favoritos.insert('', 'end', f'{i[1]}_{i[2]}', values=(i[1], i[2]))

######### COMPONENTES #########
#### QUADRO DE PESQUISA ####
texto_da_lista_anos = ttk.Label(quadro_de_pesquisa, text = 'Edições - Olimpiadas', style = 'titulo_treeview.TLabel')

y_filtragem_scrollbar = tk.Scrollbar(quadro_de_pesquisa, orient = tk.VERTICAL)
tv_filtragem = ttk.Treeview(quadro_de_pesquisa, yscrollcommand = y_filtragem_scrollbar.set, style = 'pesquisa.Treeview', show = 'tree')
y_filtragem_scrollbar['command'] = tv_filtragem.yview

resultado = pesquisa_banco_de_dados('olimpiadas', 'anos') # type: ignore
modalidades = filtrar_modalidades('olimpiadas', 'anos') # type: ignore
anos_olimpiada = []
for i in resultado:
    anos_olimpiada.append(i[0])
for i in range(0, len(anos_olimpiada)):
    tv_filtragem.insert('',f'{i}', f'{anos_olimpiada[i]}', text = f'{anos_olimpiada[i]}')
for i in resultado:
    cont = 1
    for j in modalidades:
        if i[cont] == 1:
            tv_filtragem.insert(f'{i[0]}', 'end', f'{i[0]}_{j}', text = f'{j}')
        cont += 1
tv_filtragem.bind('<ButtonRelease-1>')

botao_de_pesquisa = ttk.Button(quadro_de_pesquisa, text = 'Pesquisar', style = 'principal.TButton', command = demostracao_dos_dados)
botao_favoritar = ttk.Button(quadro_de_pesquisa, text = 'Favoritar', style = 'TButton', command = favoritar)

#### QUADRO DE FAVORITOS ####
y_favoritos_scrollbar = tk.Scrollbar(quadro_de_pesquisa, orient = tk.VERTICAL)
texto_de_favoritos = ttk.Label(quadro_de_pesquisa, text = 'Favoritos', style = 'titulo_treeview.TLabel')
columns = ('Ano', 'Modalidade')
tv_favoritos = ttk.Treeview(quadro_de_pesquisa, columns = columns, style = 'pesquisa.Treeview', yscrollcommand = y_favoritos_scrollbar.set, show = 'headings')
for i in columns:
    tv_favoritos.heading(i, text = i, anchor = 'center')
    tv_favoritos.column(i, width = 100)

y_favoritos_scrollbar['command'] = tv_favoritos.yview

botao_de_pesquisa_favorito = ttk.Button(quadro_de_pesquisa, text='Pesquisar', style='principal.TButton', command = demostracao_dos_dados_favoritos)
botao_desfavoritar = ttk.Button(quadro_de_pesquisa, text='Desfavoritar', style='TButton', command = desfavoritar)

if usuario_ativo():
    recarregar_favoritos()

#### QUADRO DE DADOS ####
titulo = ttk.Label(quadro_de_dados, text='TITULO', style='titulo.TLabel', anchor='center')
columns = ('Estatísticas', 'Primeiro', 'Segundo', 'Terceiro')
y_dados_scrollbar = tk.Scrollbar(quadro_de_dados, orient=tk.VERTICAL)
tv_dados = ttk.Treeview(quadro_de_dados, columns=columns, show='headings', yscrollcommand=y_dados_scrollbar.set, style='dados.Treeview')
for i in columns:
    tv_dados.heading(i, text=i)
    tv_dados.column(i, anchor='center')
tv_dados.column('Estatísticas', anchor='w')
y_dados_scrollbar['command'] = tv_dados.yview

######### POSICAO DOS COMPONENTES #########
#### QUADRO DE PESQUISA ####
texto_da_lista_anos.grid(row=0, column=0, padx=(15, 0))
tv_filtragem.grid(row=1, column=0, ipady=50, sticky=tk.N+tk.S+tk.E+tk.W)
y_filtragem_scrollbar.grid(row=1, column=1, sticky=tk.N+tk.S)
botao_de_pesquisa.grid(row=2, column=0, pady=(15, 0), ipadx=40, sticky=tk.W)
botao_favoritar.grid(row=2, column=0, pady=(15, 0), sticky=tk.E)

#### QUADRO DE FAVORITOS ####
texto_de_favoritos.grid(row=3, column=0, padx=(15, 0), pady=(30, 0))
tv_favoritos.grid(row=4, column=0, ipadx=50, ipady=50, sticky=tk.N+tk.S+tk.E+tk.W)
y_favoritos_scrollbar.grid(row=4, column=1, sticky=tk.N+tk.S)
botao_de_pesquisa_favorito.grid(row=5, column=0, pady=(15, 15), sticky=tk.W, ipadx=40)
botao_desfavoritar.grid(row=5, column=0, pady=(15, 15), sticky=tk.E)

#### QUADRO DE DADOS ####
titulo.grid(row=0, column=0, ipady=35)
tv_dados.grid(row=1, column=0, ipady=245, sticky=tk.N+tk.S+tk.E+tk.W)
y_dados_scrollbar.grid(row=1, column=1, sticky=tk.N+tk.S)

janela_de_consulta.protocol("WM_DELETE_WINDOW", fechar)
janela_de_consulta.mainloop()