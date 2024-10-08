from tkinter import *
from tkinter import ttk
from subprocess import call
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'persistencia')))
from funcoes_banco_de_dados import * # type: ignore

######### FUNCOES #########
def cadastrar():
    nome = str(entrada_usuario.get())
    senha = str(entrada_senha.get())
    if nome == '' or senha == '':
        texto_de_erro['text'] = '*Algum campo está em branco'

    elif len(senha) < 6:
        texto_de_erro['text'] = '*A senha deve ter, no mínimo, 6 digitos'

    elif len(nome) < 3:
        texto_de_erro['text'] = '*O nome dever ter, no mínimo, 3 digitos'
    
    else:
        resultado = pesquisa_banco_de_dados('cadastro', 'usuarios') # type: ignore
        encontrado = 0
        for i in resultado:
            if i[1] == nome:
                texto_de_erro['text'] = '*Usuário ja cadastrado'
                encontrado = 1
                break

        if encontrado == 0:
            inserir_no_usuario_banco_de_dados('cadastro', 'usuarios', nome, senha)# type: ignore
            nome = nome.replace(' ', '_')
            criar_nova_tabela('cadastro', nome)# type: ignore
            janela_cadastro.destroy()

######### INTERFACE #########
janela_cadastro = Tk()
janela_cadastro.title('Cadastro - ScoreGame')
janela_cadastro.geometry('480x400')
janela_cadastro.config(background='#292929')

######### STYLES #########
from styles import * # type: ignore

######### COMPONENTES #########
#entradas#
entrada_usuario = ttk.Entry(janela_cadastro, style='TEntry', font=('Calibri', 12, 'bold'))
entrada_senha = ttk.Entry(janela_cadastro, style='TEntry', font=('Calibri', 12, 'bold'))

#textos#
texto_titulo = ttk.Label(janela_cadastro, text='CADASTRE-SE', style='titulo_geral.TLabel')
texto_usuario = ttk.Label(janela_cadastro, text='Digite o Usuario', style='TLabel')
texto_senha = ttk.Label(janela_cadastro, text='Digite sua Senha', style='TLabel')
texto_de_erro = ttk.Label(janela_cadastro, text='', style='erro.TLabel')

#botoes#
botao_cadastrar = ttk.Button(janela_cadastro, text='CADASTRAR-SE', style='principal.TButton', command=cadastrar)

######### POSICAO DOS COMPONENTES #########
#titulo#
texto_titulo.grid(row=0, column=0, padx=(50, 0), pady=(35, 0))

#entradas#
texto_usuario.grid(row=1, column=0, padx=(0, 190), pady=(35, 0))
entrada_usuario.grid(row=2,column=0, padx=(50, 0), pady=(5, 0), ipadx= 100, ipady= 3)

texto_senha.grid(row=3,column=0, padx=(0, 185), pady=(15, 0))
entrada_senha.grid(row=4,column=0, padx=(50, 0), pady=(5, 0), ipadx= 100, ipady= 3)

#botao de entrada#
botao_cadastrar.grid(row=5, column=0, padx=(50, 0), pady=(25, 0), ipadx= 70)

#texto de erro#
texto_de_erro.grid(row=6, column=0, padx=(50, 0), pady=(15, 0))

janela_cadastro.mainloop()