import tkinter as tk
from tkinter import ttk

# Cria a janela principal
root = tk.Tk()
root.title("Exemplo Treeview")

# Define o Treeview com 3 colunas
tree = ttk.Treeview(root, columns=("coluna1", "coluna2", "coluna3"), show="headings")

# Define os títulos das colunas
tree.heading("coluna1", text="Coluna 1")
tree.heading("coluna2", text="Coluna 2")
tree.heading("coluna3", text="Coluna 3")

# Define o tamanho das colunas
tree.column("coluna1", width=100)
tree.column("coluna2", width=100)
tree.column("coluna3", width=100)

lista = ['1', 2]
# Adiciona uma linha preenchendo apenas a segunda coluna
tree.insert("", tk.END, values=("", lista, ""))

# Exibe o Treeview
tree.pack()

# Inicia o loop da interface
root.mainloop()