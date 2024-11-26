from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'persistencia')))
from funcoes_triagem import * # type: ignore

######### INTERFACE #########
janela_administrativa = Tk()
janela_administrativa.title('tela adm - ScoreGame')
janela_administrativa.geometry('1395x560')
janela_administrativa.config(background='white')

######### LABELS #########
quadro_de_dados = LabelFrame(janela_administrativa, background='white', borderwidth=0)
quadro_de_dados.grid(row=0, column=1)

quadro_de_filtragem = LabelFrame(janela_administrativa, background='white', borderwidth=0)
quadro_de_filtragem.grid(row=1, column=1, ipadx=96, ipady=5)

quadro_de_acoes = LabelFrame(janela_administrativa, background='white', borderwidth=0)
quadro_de_acoes.grid(row=0, column=0, ipadx=10, ipady=5, pady=(0, 87))

quadro_de_erro_acoes = LabelFrame(janela_administrativa, background='white', borderwidth=0)
quadro_de_erro_acoes.grid(row=1, column=0, ipadx=10, ipady=5, pady=(0, 20))

######### STYLES #########
from styles import * # type: ignore

######### FUNCOES #########
def atualizar_anos_modalidades():
    dados = criar_tela_de_filtragem() # type: ignore
    lista_modalidade.config(values=dados[1])
    lista_ano.config(values=dados[2])

def demostracao_dos_dados():
    try:
        resultado = lista_ano.get() + '_' + lista_modalidade.get()
        for item in tv_dados.get_children():
            tv_dados.delete(item)

        valores = pesquisar_dados(resultado) # type: ignore

        for i in range(0, len(valores[0])):
            tv_dados.insert('', 'end', f'{valores[0][i].replace('_', ' ')}_{valores[1][i]}_{valores[2][i]}_{valores[3][i]}', values=(valores[0][i].replace('_', ' '), valores[1][i], valores[2][i], valores[3][i]))
        
        texto_erro_filtragem.config(text='')
        
    except mysql.connector.errors.ProgrammingError: # type: ignore
        texto_erro_filtragem.config(text='pesquisa não encontrada')

def modificar_texto_erro(resultado):
    biblioteca_de_casos = {0:'Ano Deve Ter Apenas Numeros', 1:'Ano Não Encontrado', 2:'Ano Encontrado', 3:'Modalidade Não Encontrada', 
    4:'Modalidade Encontrada', 5:'Estatistica Não Encontrada', 6:'Estatistica Já Encontrada', 7: 'Sua Ação Ocorreu Com Sucesso!'}

    if resultado == 7:
        texto_erro_acoes.config(text=biblioteca_de_casos[resultado], foreground='green')

    else:
        texto_erro_acoes.config(text=biblioteca_de_casos[resultado], foreground='red')

def puxar_dados():
    dados = pesquisa_dados(tv_dados.focus()) # type: ignore
    
    entrada_ano.delete(0, 'end')
    entrada_modalidade.delete(0, 'end')
    entrada_estatistica.delete(0, 'end')
    entrada_primeiro.delete(0, 'end')
    entrada_segundo.delete(0, 'end')
    entrada_terceiro.delete(0, 'end')

    entrada_ano.insert(0, lista_ano.get())
    entrada_modalidade.insert(0, lista_modalidade.get())
    entrada_estatistica.insert(0, dados[0])
    entrada_primeiro.insert(0, dados[1])
    entrada_segundo.insert(0, dados[2])
    entrada_terceiro.insert(0, dados[3])

def inserir():
    ano = entrada_ano.get()
    modalidade = entrada_modalidade.get()
    estatistica = entrada_estatistica.get()
    primeiro = entrada_primeiro.get()
    segundo = entrada_segundo.get()
    terceiro = entrada_terceiro.get()

    texto_erro_acoes.config(foreground='red', text='')

    if ano and modalidade and estatistica:
        resultado = inserir_estatistica(ano, modalidade, estatistica) # type: ignore
        modificar_texto_erro(resultado)
        if (primeiro != '' or segundo != '' or terceiro != ''):
            editar_estatistica(ano, modalidade, estatistica, primeiro, segundo, terceiro) # type: ignore
        demostracao_dos_dados()

    elif ano and modalidade and not estatistica:
        resultado = inserir_modalidade(ano, modalidade) # type: ignore
        modificar_texto_erro(resultado)
        atualizar_anos_modalidades()

    elif ano and not modalidade and not estatistica:
        resultado = inserir_ano(ano) # type: ignore
        modificar_texto_erro(resultado)
        atualizar_anos_modalidades()

    else:
        texto_erro_acoes.config(text='Não Entendi o Que Você Está Inserindo')

def editar():
    ano = entrada_ano.get()
    modalidade = entrada_modalidade.get()
    estatistica = entrada_estatistica.get()
    primeiro = entrada_primeiro.get()
    segundo = entrada_segundo.get()
    terceiro = entrada_terceiro.get()
    ano_selecionado = lista_ano.get()
    modalidade_selecionada = lista_modalidade.get()
    estatistica_selecionada = pesquisa_dados(tv_dados.focus()) # type: ignore
    texto_erro_acoes.config(foreground='red', text='')

    if ano != ano_selecionado and (ano != '' and ano_selecionado != ''):
        if messagebox.askokcancel(title='Editar', message=f'Você está editando o ano {ano_selecionado} para {ano}, você deseja continuar?'):
            resultado = edita_ano(ano, ano_selecionado) # type: ignore
            modificar_texto_erro(resultado)
            atualizar_anos_modalidades()

    elif modalidade != modalidade_selecionada and (modalidade != '' and modalidade_selecionada != ''):
        if messagebox.askokcancel(title='Editar', message=f'Você está editando a modalidade {modalidade_selecionada} para {modalidade}, você deseja continuar?'):
            resultado = editar_modalidade(modalidade, modalidade_selecionada) # type: ignore
            modificar_texto_erro(resultado)
            atualizar_anos_modalidades()

    elif (ano == ano_selecionado and modalidade == modalidade_selecionada and estatistica == estatistica_selecionada[0]) and (ano != '' and modalidade != '' and estatistica != '' and estatistica_selecionada[0] != ''):
        if messagebox.askokcancel(title='Editar', message=f'Você está editando os dados da estatistica {estatistica} da tabela {ano_selecionado}/{modalidade_selecionada}, você deseja continuar?'):
            resultado = editar_estatistica(ano, modalidade, estatistica, primeiro, segundo, terceiro) # type: ignore
            modificar_texto_erro(resultado)
            demostracao_dos_dados()

    elif (ano == ano_selecionado and modalidade == modalidade_selecionada and estatistica != estatistica_selecionada[0]) and (ano != '' and modalidade != '' and estatistica != '' and estatistica_selecionada[0] != ''):
        if messagebox.askokcancel(title='Editar', message=f'Você está editando o nome da estatistica {estatistica_selecionada[0]} para {estatistica} da tabela {ano_selecionado}/{modalidade_selecionada}, você deseja continuar?'):
            resultado = editar_texto_estatistica(ano, modalidade, estatistica, estatistica_selecionada[0]) # type: ignore
            modificar_texto_erro(resultado)
            demostracao_dos_dados()

    else:
        texto_erro_acoes.config(text='Não Entendi o Que Você Está Editando')

def excluir():
    ano = entrada_ano.get()
    modalidade = entrada_modalidade.get()
    estatistica = entrada_estatistica.get()
    
    texto_erro_acoes.config(foreground='red', text='')

    if ano and modalidade and estatistica:
        if messagebox.askyesno(title='Excluir', message=f'Você está excluindo a estatistica {estatistica} do {ano}/{modalidade}, você deseja continuar?'):
            resultado = remover_estatistica(ano, modalidade, estatistica) # type: ignore
            modificar_texto_erro(resultado)
            demostracao_dos_dados()

    elif ano and modalidade and not estatistica:
        if messagebox.askyesno(title='Excluir', message=f'Você está excluindo a tabela {ano}/{modalidade}, você deseja continuar?'):
            resultado = remover_tabela(ano, modalidade) # type: ignore
            modificar_texto_erro(resultado)
    
    elif ano and not modalidade and not estatistica:
        if messagebox.askyesno(title='Excluir', message=f'Você está excluindo a olipíada do ano {ano}, você deseja continuar?'):
            resultado = remover_ano(ano) # type: ignore
            modificar_texto_erro(resultado)
            atualizar_anos_modalidades()

    elif not ano and modalidade and not estatistica:
        if messagebox.askyesno(title='Excluir', message=f'Você está excluindo a modalidade {modalidade} de todas as olimpiadas, você deseja continuar?'):
            resultado = remover_modalidade(modalidade) # type: ignore
            modificar_texto_erro(resultado)
            atualizar_anos_modalidades()

    else:
        texto_erro_acoes.config(text='Não Entendi o Que Você Está Excluindo')

######### COMPONENTES #########
#textos#
titulo_dados = ttk.Label(quadro_de_dados, text='SCOREGAME', style='titulo.TLabel', anchor='center')
titulo_acoes = ttk.Label(quadro_de_acoes, text='CRUD', style='titulo.TLabel', anchor='center')

texto_erro_filtragem = ttk.Label(quadro_de_filtragem, text='', style='erro.TLabel', background='white')
texto_erro_acoes  = ttk.Label(quadro_de_erro_acoes, text='', style='erro.TLabel', background='white')
texto_ano = ttk.Label(quadro_de_acoes, text='Ano', style='telas_gerais.TLabel')
texto_modalidade = ttk.Label(quadro_de_acoes, text='Modalidade', style='telas_gerais.TLabel')
texto_estatistica = ttk.Label(quadro_de_acoes, text='Estatistica', style='telas_gerais.TLabel')
texto_primeiro = ttk.Label(quadro_de_acoes, text='Primeiro', style='telas_gerais.TLabel')
texto_segundo = ttk.Label(quadro_de_acoes, text='Segundo', style='telas_gerais.TLabel')
texto_terceiro = ttk.Label(quadro_de_acoes, text='Terceiro', style='telas_gerais.TLabel' )

#entradas#
entrada_ano = ttk.Entry(quadro_de_acoes, style='TEntry', font=('Calibri', 12, 'bold'))
entrada_modalidade = ttk.Entry(quadro_de_acoes, style='TEntry', font=('Calibri', 12, 'bold'))
entrada_estatistica = ttk.Entry(quadro_de_acoes, style='TEntry', font=('Calibri', 12, 'bold'))
entrada_primeiro = ttk.Entry(quadro_de_acoes, style='TEntry', font=('Calibri', 12, 'bold'))
entrada_segundo = ttk.Entry(quadro_de_acoes, style='TEntry', font=('Calibri', 12, 'bold'))
entrada_terceiro = ttk.Entry(quadro_de_acoes, style='TEntry', font=('Calibri', 12, 'bold'))

#listas#
dados = criar_tela_de_filtragem() # type: ignore
lista_modalidade = ttk.Combobox(quadro_de_filtragem, style='TCombobox', values=dados[1])
lista_ano = ttk.Combobox(quadro_de_filtragem, style='TCombobox', values=dados[2])

#botoes#
botao_filtrar = ttk.Button(quadro_de_filtragem, text='Filtrar', style='principal.TButton', command=demostracao_dos_dados)
botao_inserir = ttk.Button(quadro_de_acoes, text='Inserir', style='azul.TButton', command=inserir)
botao_editar = ttk.Button(quadro_de_acoes, text='Editar', style='verde.TButton', command=editar)
botao_excluir = ttk.Button(quadro_de_acoes, text='Excluir', style='vermelho.TButton', command=excluir)
botao_puxar_dados = ttk.Button(quadro_de_acoes, text='Puxar Dados', style='laranja.TButton', command=puxar_dados)

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
#### QUADRO DE DADOS ####
titulo_dados.grid(row=0, column=0)
tv_dados.grid(row=1, column=0, ipady=100, sticky=tk.N+tk.S+tk.E+tk.W)
y_dados_scrollbar.grid(row=1, column=1, sticky=tk.N+tk.S)

#### QUADRO DE FILTRAGEM ####
lista_ano.grid(row=0, column=0, padx=(50, 0), pady=(10, 0), ipady=5, ipadx=20)
lista_modalidade.grid(row=0, column=1, padx=(50, 0), pady=(10, 0), ipady=5, ipadx=20)
botao_filtrar.grid(row=0, column=2, padx=(50, 0), pady=(10, 0), ipadx=20)
texto_erro_filtragem.grid(row=1, column=1, padx=(50, 0), pady=(10, 0))

#### QUADRO DE ACOES ####
titulo_acoes.grid(row=0, column=1, padx=(20, 0))

texto_ano.grid(row=1, column=0, padx=(20, 0), pady=(15, 0))
entrada_ano.grid(row=2, column=0, padx=(20, 0))

texto_modalidade.grid(row=1, column=2, padx=(20, 0), pady=(15, 0))
entrada_modalidade.grid(row=2, column=2, padx=(20, 0))

texto_estatistica.grid(row=3, column=0, padx=(20, 0), pady=(30, 0))
entrada_estatistica.grid(row=4, column=0, padx=(20, 0))

texto_primeiro.grid(row=5, column=0, padx=(20, 0), pady=(30, 0))
entrada_primeiro.grid(row=6, column=0, padx=(20, 0))

texto_segundo.grid(row=5, column=1, padx=(20, 0), pady=(30, 0))
entrada_segundo.grid(row=6, column=1, padx=(20, 0))

texto_terceiro.grid(row=5, column=2, padx=(20, 0), pady=(30, 0))
entrada_terceiro.grid(row=6, column=2, padx=(20, 0))

botao_inserir.grid(row=7, column=0, padx=(20, 0), pady=(30, 0), ipadx=20)
botao_editar.grid(row=7, column=1, padx=(20, 0), pady=(30, 0), ipadx=20)
botao_excluir.grid(row=7, column=2, padx=(20, 0), pady=(30, 0), ipadx=20)
botao_puxar_dados.grid(row=8, column=1, padx=(20, 0), pady=(30, 0), ipadx=20)

texto_erro_acoes.grid(row=9, column=1, padx=(20, 0))

janela_administrativa.mainloop()