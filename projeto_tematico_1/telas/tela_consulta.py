from tkinter import *
from tkinter import ttk
import tkinter as tk
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'persistencia')))
from funcoes_triagem import * # type: ignore

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
    trocar_ativo(usuario_ativo_sem_(), 0) # type: ignore
    janela_de_consulta.destroy()

def demostracao_dos_dados():
    pesquisa = tv_filtragem.focus()
    if len(pesquisa) > 4:
        for item in tv_dados.get_children():
            tv_dados.delete(item)
            
        titulo['text'] = f'{pesquisa.replace('_', ' ')}'

        valores = pesquisar_dados(pesquisa) # type: ignore

        for i in range(0, len(valores[0])):
            tv_dados.insert('', 'end', values=(valores[0][i].replace('_', ' '), valores[1][i], valores[2][i], valores[3][i]))

    else:
        titulo['text'] = 'Erro ao Pesquisar'
        for item in tv_dados.get_children():
            tv_dados.delete(item)

def demostracao_dos_dados_favoritos():
    try:
        pesquisa = tv_favoritos.focus()
        for item in tv_dados.get_children():
            tv_dados.delete(item)

        titulo['text'] = f'{pesquisa.replace('_', ' ')}'

        valores = pesquisar_dados_favoritos(pesquisa) # type: ignore

        for i in range(0, len(valores[0])):
            tv_dados.insert('', 'end', values=(valores[0][i].replace('_', ' '), valores[1][i], valores[2][i], valores[3][i]))
    except mysql.connector.errors.ProgrammingError: # type: ignore
        titulo['text'] = 'Erro ao Pesquisar'
        for item in tv_dados.get_children():
            tv_dados.delete(item)

def favoritar():
    try:
        pesquisa = tv_filtragem.focus()

        if add_favorito(pesquisa): # type: ignore
            recarregar_favoritos()
            demostracao_dos_dados()
            titulo['text'] = f'{pesquisa.replace('_', ' ')}'

        else:
            titulo['text'] = 'Erro ao Favoritar'
            for item in tv_dados.get_children():
                tv_dados.delete(item)

    except mysql.connector.errors.ProgrammingError: # type: ignore
        titulo['text'] = 'Erro ao Favoritar'
        for item in tv_dados.get_children():
            tv_dados.delete(item)

def desfavoritar():
    pesquisa = tv_favoritos.focus()
    if pesquisa == '':
        titulo['text'] = 'Erro ao desfavoritar'

    else:
        try:
            remover_favorito(pesquisa) # type: ignore
            recarregar_favoritos()

            titulo['text'] = 'SCOREGAME'

        except mysql.connector.errors.ProgrammingError: # type: ignore
            titulo['text'] = 'Erro ao desfavoritar'

    for item in tv_dados.get_children():
        tv_dados.delete(item)

def recarregar_favoritos():
    usuario = usuario_ativo() # type: ignore

    for item in tv_favoritos.get_children():
            tv_favoritos.delete(item)

    resultado = recarregar(usuario) # type: ignore

    for i in resultado:
        tv_favoritos.insert('', 'end', f'{i[1]}_{i[2]}', values=(i[1], i[2].replace('_', ' ')))

######### COMPONENTES #########
#textos#
texto_da_lista_anos = ttk.Label(quadro_de_pesquisa, text = 'Edições - Olimpiadas', style = 'titulo_treeview.TLabel')
texto_de_favoritos = ttk.Label(quadro_de_pesquisa, text = 'Favoritos', style = 'titulo_treeview.TLabel')
titulo = ttk.Label(quadro_de_dados, text='SCOREGAME', style='titulo.TLabel', anchor='center')

#botoes#
botao_de_pesquisa = ttk.Button(quadro_de_pesquisa, text = 'Pesquisar', style = 'principal.TButton', command = demostracao_dos_dados)
botao_favoritar = ttk.Button(quadro_de_pesquisa, text = 'Favoritar', style = 'TButton', command = favoritar)
botao_de_pesquisa_favorito = ttk.Button(quadro_de_pesquisa, text='Pesquisar', style='principal.TButton', command = demostracao_dos_dados_favoritos)
botao_desfavoritar = ttk.Button(quadro_de_pesquisa, text='Desfavoritar', style='TButton', command = desfavoritar)

#### QUADRO DE PESQUISA ####
y_filtragem_scrollbar = tk.Scrollbar(quadro_de_pesquisa, orient = tk.VERTICAL)
tv_filtragem = ttk.Treeview(quadro_de_pesquisa, yscrollcommand = y_filtragem_scrollbar.set, style = 'pesquisa.Treeview', show = 'tree')
y_filtragem_scrollbar['command'] = tv_filtragem.yview

dados = criar_tela_de_filtragem() # type: ignore

for i in range(0, len(dados[2])):
    tv_filtragem.insert('',f'{i}', f'{dados[2][i]}', text = f'{dados[2][i]}')

for i in dados[0]:
    cont = 1
    for j in dados[1]:
        if i[cont] == 1:
            tv_filtragem.insert(f'{i[0]}', 'end', f'{i[0]}_{j}', text = f'{j.replace('_', ' ')}')
        cont += 1

tv_filtragem.bind('<ButtonRelease-1>')

#### QUADRO DE FAVORITOS ####
y_favoritos_scrollbar = tk.Scrollbar(quadro_de_pesquisa, orient = tk.VERTICAL)
columns = ('Ano', 'Modalidade')
tv_favoritos = ttk.Treeview(quadro_de_pesquisa, columns = columns, style = 'pesquisa.Treeview', yscrollcommand = y_favoritos_scrollbar.set, show = 'headings')

for i in columns:
    tv_favoritos.heading(i, text = i, anchor = 'center')
    tv_favoritos.column(i, width = 100)

y_favoritos_scrollbar['command'] = tv_favoritos.yview

if usuario_ativo(): # type: ignore
    recarregar_favoritos()

#### QUADRO DE DADOS ####
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