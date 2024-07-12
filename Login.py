import sqlite3
import customtkinter as ctk

conn = sqlite3.connect(r'C:\SQLITE\BANCOTESTE\data.db')
cursor = conn.cursor()

def logar(name,password):
    nome_login= name
    senha_login = password

    cursor.execute("SELECT senha FROM usuarios WHERE nome = ?",(nome_login,))
    try:
        senha_banco = cursor.fetchone()[0]
        
        if senha_banco == senha_login:
            print("Login efetuado com sucesso!")
        else:
            print('senha incorreta!')

    except Exception as e:
        print('Usuario não encontrado!')

root = ctk.CTk()
root.geometry('400x300')
root.resizable(False,False)
ctk.set_default_color_theme("dark-blue")
ctk.set_appearance_mode("dark")

root.mainloop()

 