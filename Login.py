import sqlite3
import customtkinter as ctk
import tkinter as tk
from customtkinter import *

conn = sqlite3.connect(r'C:\SQLITE\BANCOTESTE\data.db')
cursor = conn.cursor()

#definindo a função para validar usuario e senha
def logar(name,password):
    nome_login= name
    senha_login = password

    def errorlogin(mensage):
        mensagem= mensage
        failedlogin= ctk.CTkLabel(graycanva,text=mensagem,font=('calibri',15))
        failedlogin.grid_remove
        failedlogin.place(relx=0.36,rely=0.55)

    cursor.execute("SELECT senha FROM usuarios WHERE nome = ?",(nome_login,))
    try:
        senha_banco = cursor.fetchone()[0]
        
        if senha_banco == senha_login:
            print("Login efetuado com sucesso!")
        else:
            print('senha incorreta!')
            errorlogin('senha incorreta')

    except Exception as e:
        print('Usuario não encontrado!')
        errorlogin('Usuario não encontrado!')

#inicação da criação da janela e configuração padrão
root = ctk.CTk()
root.geometry('800x600')
root.title('Climatempo')
root.resizable(False,False)
#definição de tema
ctk.set_appearance_mode("dark")
#inicio da definição do widgets
#configuração do canva cinza que fica na direita
graycanva = ctk.CTkFrame(root,width=290,height=700,fg_color='#3d3d3d')
graycanva.place(relx=0.65,rely=-0.1)
#widget texto e campo de digitação:
#FAÇA O LOGIN
text1 = ctk.CTkLabel(graycanva,text='Faça o Login:',font=('Calibri',15),text_color='#b1b2b3')
text1.place(relx=0.36,rely=0.35)
#USUENTRY
usuentry= ctk.CTkEntry(graycanva,width=160,height=10,placeholder_text='Usuário')
usuentry.place(relx=0.23,rely=0.4)
#USUSENHA
ususenha= ctk.CTkEntry(graycanva,width=160,height=10,placeholder_text='Senha')
ususenha.place(relx=0.23,rely=0.45)
#botão de login
buttonlogin = ctk.CTkButton(graycanva,width=120,height=20,text='Entrar',fg_color='#8651e8',text_color='#333233',command=lambda:logar(usuentry.get(),int(ususenha.get())))
buttonlogin.place(relx=0.3,rely=0.5)
#mensagem de senha ou usuario errado


root.mainloop()

