from tkinter import *
from tkinter import ttk
from subprocess import call
from time import sleep
import tkinter as tk
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', 'persistencia')))
from funcoes_triagem import * # type: ignore

######### INTERFACE #########
janela_login = Tk()
janela_login.title('ScoreGame') 
janela_login.geometry('550x570')
janela_login.config(background='#292929')

######### STYLES #########
from persistencia.styles import *

######### FUNCOES / JANELAS #########
def mostrar_senha():
    if sensura.get() == 1:
        entrada_senha.config(show='')
    else:
        entrada_senha.config(show='*')

def entrada():
    usuario = str(entrada_usuario.get())
    senha = str(entrada_senha.get())
    if len(usuario) == 0 or len(senha) == 0:
        texto_de_erro['text'] = '*Usuário ou senha não informados'

    else:
        resultado = verificar_usuario(usuario, senha) # type: ignore
        if resultado == 1:
            entrar_tela_de_consulta()

        elif resultado == 2:
            entrar_tela_administrador()
            
        else:
            texto_de_erro['text'] = '*Usuário ou senha incorretos'

def entrar_tela_administrador():
    janela_login.destroy()
    call(['python', 'telas\\tela_de_administrativa.py'])

def entrar_tela_de_consulta():
    janela_login.destroy()
    call(['python', 'telas\\tela_consulta.py'])
    
def criar_cadastro():
    call(['python', 'telas\\tela_cadastro.py'])

def criar_nova_senha():
    call(['python', 'telas\\tela_nova_senha.py'])

######### COMPONENTES #########
#logo#
logo = PhotoImage(file='imagens/foto_da_logo.png')
logo = logo.subsample(12,12)
figura_login = Label(image=logo, background='#292929')

#entradas#
entrada_usuario = ttk.Entry(janela_login, style = 'TEntry', font=('Calibri', 12, 'bold'))
entrada_senha = ttk.Entry(janela_login, style = 'TEntry', font=('Calibri', 12, 'bold'), show='*')

#textos#
texto_usuario = ttk.Label(janela_login, text = 'Digite o Usuario', style = 'TLabel')
texto_senha = ttk.Label(janela_login, text = 'Digite sua Senha', style = 'TLabel')
texto_de_erro = ttk.Label(janela_login, text = '', style = 'erro.TLabel')

#botoes#
botao_entrar = ttk.Button(janela_login, text = 'ENTRAR', style = 'principal.TButton', command = entrada)
botao_sem_login = ttk.Button(janela_login, text='Continuar s/Login', style='TButton', command = entrar_tela_de_consulta)
botao_cadastro = ttk.Button(janela_login, text='Cadastre-se', style = 'TButton', command = criar_cadastro)
botao_esqueci_senha = ttk.Button(janela_login, text='Esqueci a Senha', style='TButton', command=criar_nova_senha)
sensura = tk.IntVar()
botao_sensura = ttk.Checkbutton(janela_login, text = 'Mostrar senha', style = "TCheckbutton", variable = sensura, onvalue = 1, offvalue = 0, command = mostrar_senha)

######### POSICAO DOS COMPONENTES #########
#figura#
figura_login.grid(row=0, column=0, padx=(50, 0), pady=(35, 0))

#entradas#
texto_usuario.grid(row=1, column=0, padx=(0, 190), pady=(15, 0))
entrada_usuario.grid(row=2,column=0, padx=(50, 0), pady=(5, 0), ipadx= 100, ipady= 3)
texto_senha.grid(row=3,column=0, padx=(0, 185), pady=(15, 0))
entrada_senha.grid(row=4,column=0, padx=(50, 0), pady=(5, 0), ipadx= 100, ipady= 3)

#botao de sensura#
botao_sensura.grid(row=5, column=0, padx=(0, 196), pady=(5, 0))

#botao de entrada#
botao_entrar.grid(row=6, column=0, padx=(50, 0), pady=(25, 0), ipadx= 90)

#texto de erro#
texto_de_erro.grid(row=7, column=0, padx=(50, 0), pady=(15, 0))

#botoes adicionais#
botao_sem_login.grid(row=8, column=0, padx=(50, 300), pady=(30, 0), ipadx= 15)
botao_cadastro.grid(row=8, column=0, padx=(50, 0), pady=(30, 0), ipadx= 15)
botao_esqueci_senha.grid(row=8, column=0, padx=(340, 0), pady=(30, 0), ipadx= 15)

if not verificação(): # type: ignore
    texto_de_erro['text'] = '*Banco de dados não encontrado'
    sleep(5)
    janela_login.destroy()

janela_login.mainloop()