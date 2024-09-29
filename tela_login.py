from tkinter import *
from tkinter import ttk
from subprocess import call
from funcoes_banco_da_dados import *

######### FUNCOES / JANELAS #########
try:
    resultado = filtrar_modalidades('olimpiadas', 'anos')
    resultado = pesquisa_banco_de_dados('cadastro', 'usuarios')
except mysql.connector.errors.DatabaseError:
    quit()

def fechar_tudo():
    quit()

def entrada():
    usuario = str(entrada_usuario.get())
    senha = str(entrada_senha.get())
    if len(usuario) == 0 or len(senha) == 0:
        texto_de_erro['text'] = '*Usuário ou senha não informados'

    else:
        for i in resultado:
            if usuario == i[1] and senha == i[2]:
                texto_de_erro['text'] = ''
                if i[3] == 0:
                    janela_login.destroy()
                    entrar_tela_de_consulta()
                else:
                    janela_login.destroy()
                    entrar_administrador()

        texto_de_erro['text'] = '*Usuário ou senha inválido'

def entrar_administrador():
    janela_login.destroy()
    call(['python', 'tela_de_administrativa.py'])

def entrar_tela_de_consulta():
    janela_login.destroy()
    call(['python', 'tela_de_consulta.py'])

def criar_cadastro():
    call(['python', 'tela_cadastro.py'])

def criar_nova_senha():
    call(['python', 'tela_nova_senha.py'])

######### INTERFACE #########
janela_login = Tk()
janela_login.title('ScoreGame') 
janela_login.geometry('550x560')
janela_login.config(background='#292929')

######### STYLES #########
import styles

######### COMPONENTES #########
#logo#
logo = PhotoImage(file='imagens/foto_da_logo.png')
logo = logo.subsample(12,12)
figura_login = Label(image=logo, background='#292929')

#entradas#
entrada_usuario = ttk.Entry(janela_login, style='TEntry')
entrada_senha = ttk.Entry(janela_login, style='TEntry')

#textos#
texto_usuario = ttk.Label(janela_login, text='Digite o Usuario', style='TLabel')
texto_senha = ttk.Label(janela_login, text='Digite sua Senha', style='TLabel')
texto_de_erro = ttk.Label(janela_login, text='', style='erro.TLabel')

#botoes#
botao_entrar = ttk.Button(janela_login, text='ENTRAR', style='principal.TButton', command=entrada)
botao_sem_login = ttk.Button(janela_login, text='Continuar s/Login', style='TButton', command=entrar_tela_de_consulta)
botao_cadastro = ttk.Button(janela_login, text='Cadastre-se', style='TButton', command=criar_cadastro)
botao_esqueci_senha = ttk.Button(janela_login, text='Esqueci a Senha', style='TButton', command=criar_nova_senha)

######### POSICAO DOS COMPONENTES #########
#figura#
figura_login.grid(row=0, column=0, padx=(50, 0), pady=(35, 0))

#entradas#
texto_usuario.grid(row=1, column=0, padx=(0, 170), pady=(15, 0))
entrada_usuario.grid(row=2,column=0, padx=(50, 0), pady=(5, 0), ipadx= 100, ipady= 3)
texto_senha.grid(row=3,column=0, padx=(0, 165), pady=(15, 0))
entrada_senha.grid(row=4,column=0, padx=(50, 0), pady=(5, 0), ipadx= 100, ipady= 3)

#botao de entrada#
botao_entrar.grid(row=5, column=0, padx=(50, 0), pady=(25, 0), ipadx= 90)

#texto de erro#
texto_de_erro.grid(row=6, column=0, padx=(50, 0), pady=(15, 0))

#botoes adicionais#
botao_sem_login.grid(row=7, column=0, padx=(50, 300), pady=(30, 0), ipadx= 15)
botao_cadastro.grid(row=7, column=0, padx=(50, 0), pady=(30, 0), ipadx= 15)
botao_esqueci_senha.grid(row=7, column=0, padx=(340, 0), pady=(30, 0), ipadx= 15)

janela_login.protocol("WM_DELETE_WINDOW", fechar_tudo)
janela_login.mainloop()