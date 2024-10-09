from tkinter import *
from tkinter import ttk
from subprocess import call
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'persistencia')))
from funcoes_triagem import * # type: ignore

######### FUNCOES #########
def nova_senha():
    nome = str(entrada_usuario.get())
    senha = str(entrada_senha.get())
    if nome == '' or senha == '':
        texto_de_erro['text'] = '*Algum campo está em branco'

    elif len(senha) < 6:
        texto_de_erro['text'] = '*A senha deve ter, no mínimo, 6 digitos'

    else:
        if mudar_senha(nome, senha): # type: ignore
            janela_nova_senha.destroy()
            
        else:
            texto_de_erro['text'] = '*Usuário não encontrado'

######### INTERFACE #########
janela_nova_senha = Tk()
janela_nova_senha.title('Nova Senha - ScoreGame')
janela_nova_senha.geometry('480x400')
janela_nova_senha.config(background='#292929')

######### STYLES #########
from styles import * # type: ignore

######### COMPONENTES #########
#entradas#
entrada_usuario = ttk.Entry(janela_nova_senha, style='TEntry', font=('Calibri', 12, 'bold'))
entrada_senha = ttk.Entry(janela_nova_senha, style='TEntry', font=('Calibri', 12, 'bold'))

#textos#
texto_titulo = ttk.Label(janela_nova_senha, text='NOVA SENHA', style='titulo_geral.TLabel')
texto_usuario = ttk.Label(janela_nova_senha, text='Digite o Usuario', style='TLabel')
texto_senha = ttk.Label(janela_nova_senha, text='Digite sua Nova Senha', style='TLabel')
texto_de_erro = ttk.Label(janela_nova_senha, text='', style='erro.TLabel')

#botoes#
botao_entrar = ttk.Button(janela_nova_senha, text='CRIAR NOVA SENHA', style='principal.TButton', command=nova_senha)

######### POSICAO DOS COMPONENTES #########
#titulo#
texto_titulo.grid(row=0, column=0, padx=(50, 0), pady=(35, 0))

#entradas#
texto_usuario.grid(row=1, column=0, padx=(0, 190), pady=(35, 0))
entrada_usuario.grid(row=2,column=0, padx=(50, 0), pady=(5, 0), ipadx= 100, ipady= 3)
texto_senha.grid(row=3,column=0, padx=(0, 140), pady=(15, 0))
entrada_senha.grid(row=4,column=0, padx=(50, 0), pady=(5, 0), ipadx= 100, ipady= 3)

#botao de entrada#
botao_entrar.grid(row=5, column=0, padx=(50, 0), pady=(25, 0), ipadx= 70)

#texto de erro#
texto_de_erro.grid(row=6, column=0, padx=(50, 0), pady=(15, 0))

janela_nova_senha.mainloop()