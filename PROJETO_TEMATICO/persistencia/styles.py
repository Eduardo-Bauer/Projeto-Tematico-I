from tkinter import ttk

style = ttk.Style()
style.theme_use('default')

######### TREEVIEWS #########
style_tv = ttk.Style()
style_tv.configure("dados.Treeview", font=('Calibri', 13), background='white', anchor='center', foreground='#292929', fieldbackground="white")
style_tv.configure("dados.Treeview.Heading", font=('Calibri', 14,'bold'), background='#d9d9d9', anchor='center', foreground='#292929', relief='none')

style_tv = ttk.Style()
style_tv.configure("pesquisa.Treeview", font=('Calibri', 13), background='white', anchor='center', foreground='black', fieldbackground="white")
style_tv.configure('pesquisa.Treeview.Heading', font=('Calibri', 14), background='#d9d9d9', anchor='center', foreground='black', relief='none')

######### BOTÃO PRINCIPAL VERDE #########
botao_principal = ttk.Style()
botao_principal.configure('principal.TButton', font=('Calibri', 12, 'bold'), relief = "solid", background='white', foreground='green')
botao_principal.map("principal.TButton", background=[("active", "#e0ffd3")], foreground=[("pressed", "black")])

######### BOTÃO SECUNDARIO #########
botao_secundario = ttk.Style()
botao_secundario.configure('TButton', font=('Calibri', 10, 'bold'), relief="solid", background='white')
botao_principal.map("TButton", background=[("active", "#defcff")], foreground=[("pressed", "black")])

######### ENTRADAS #########
entrada = ttk.Style()
entrada.configure('TEntry', relief="solid", background='black')

######### TITULO #########
titulo = ttk.Style()
titulo.configure('titulo.TLabel', background='white', foreground='black', font=('Calibri', 30, 'bold'))

titulo = ttk.Style()
titulo.configure('titulo_treeview.TLabel', background='#d9d9d9', foreground='black', font=('Calibri', 20, 'bold'))

titulo = ttk.Style()
titulo.configure('titulo_geral.TLabel', background='#292929', foreground='white', font=('Calibri', 30, 'bold'))

######### TEXTOS #########
texto = ttk.Style()
texto.configure('TLabel', background='#292929', foreground='white', font=('Calibri', 14, 'bold'))

######### TEXTO ERRO #########
texto_erro = ttk.Style()
texto_erro.configure('erro.TLabel', background='#292929', foreground='red', font=('Calibri', 13, 'bold'))
