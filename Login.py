import sqlite3
import customtkinter as ctk
import tkinter as tk
from customtkinter import *
import requests
from PIL import Image, ImageTk
import io

conn = sqlite3.connect(r'C:\SQLITE\BANCOTESTE\data.db')
cursor = conn.cursor()

def clima(namecity):
    #toda configuração para trazer e armazenar os dados da requisição em variaveis
    global dados,icon,localizacao,temperatuura,condicoes,city_name
    city_name = namecity
    api_key = '7a803f7c90c542eea80192316241007'
    link = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name}&aqi=no"
    requisicao = requests.get(link)
    data = requisicao.json()
    dados = data['current']
    localizacao = data['location']
    temperatura = dados['temp_c']
    temperaturaf = dados['temp_f']
    condicoes = dados['condition']
    icon = condicoes['icon']
    situacao = condicoes['text']
    uconsulta = dados['last_updated']
    pais = localizacao['country']

   #WIDGETS DO CLIMA
    #chamando a requisição para buscar imagem do clima e inserindo na tela
    image = ("https:" + icon)
    requisicaoimagem = requests.get(image)
    image_data = requisicaoimagem.content
    image_pillow = Image.open(io.BytesIO(image_data))  
    image_ctk = ctk.CTkImage(light_image=image_pillow, size=(image_pillow.width,50))
    #chamando widgets da imagem 
    imagelabel = ctk.CTkLabel(master=root2,image=image_ctk,text='')
    imagelabel.place(relx=0.33,rely=0.329)
    #chamando os dados do clima e colocando na tela
    temp = ctk.CTkLabel(root2,text='Temperatura c°',font=('Arial',10),text_color='#6da4a4')
    temp.place(relx=0.1,rely=0.5)
    tempcity = ctk.CTkLabel(root2,text=temperatura,font=('Arial',10))
    tempcity.place(relx=0.1,rely=0.56)
    #EM F
    temp2 = ctk.CTkLabel(root2,text='Temperatura f°',font=('Arial',10),text_color='#6da4a4')
    temp2.place(relx=0.55,rely=0.5)
    tempcity2 = ctk.CTkLabel(root2,text=temperaturaf,font=('Arial',10))
    tempcity2.place(relx=0.55,rely=0.56)
    #status
    temp = ctk.CTkLabel(root2,text='Status',font=('Arial',10),text_color='#6da4a4')
    temp.place(relx=0.1,rely=0.62)
    tempcity = ctk.CTkLabel(root2,text=situacao,font=('Arial',10))
    tempcity.place(relx=0.1,rely=0.68)
    #country
    temp = ctk.CTkLabel(root2,text='Pais',font=('Arial',10),text_color='#6da4a4')
    temp.place(relx=0.55,rely=0.62)
    tempcity = ctk.CTkLabel(root2,text=pais,font=('Arial',10))
    tempcity.place(relx=0.55,rely=0.68)
    #ultimaconsulta
    temp = ctk.CTkLabel(root2,text='Ultima consulta',font=('Arial',10),text_color='#6da4a4')
    temp.place(relx=0.1,rely=0.74)
    tempcity = ctk.CTkLabel(root2,text=uconsulta,font=('Arial',10))
    tempcity.place(relx=0.1,rely=0.81)
    
#configuração padrão da janela
root2= ctk.CTk()
root2.geometry('200x300')
root2.resizable(False,False)
ctk.set_default_color_theme("green")
ctk.set_appearance_mode("system")

#widgets padrão
label1 = ctk.CTkLabel(root2,text='Digite a Cidade:',font=('Arial',15))
label1.place(relx=0.23,rely=0.02)
#campo para entrada de texto
selectioncity = ctk.CTkEntry(root2,width=160,height=10)
selectioncity.place(relx=0.1,rely=0.13)
selectioncity.insert(ctk.END,'')

#botão para chamar as informações
button = ctk.CTkButton(root2,width=100,height=30,text='Pesquisar',fg_color='#6da4a4',command=lambda: clima(selectioncity.get()),text_color='black')
button.place(relx=0.25,rely=0.23)

#definindo a função para validar usuario e senha
def logar(name,password):
    nome_login= name
    senha_login = password
    
    #mensagem de senha ou usuario errado
    def errorlogin(mensage):
        mensagem= mensage
        failedlogin= ctk.CTkLabel(graycanva,text=mensagem,font=('calibri',15))
        failedlogin.place(relx=0.36,rely=0.55)

    cursor.execute("SELECT senha FROM usuarios WHERE nome = ?",(nome_login,))
    try:
        senha_banco = cursor.fetchone()[0]
        
        if senha_banco == senha_login:
            print("Login efetuado com sucesso!")
            root.withdraw()
            root2.mainloop()

        else:
            errorlogin('senha incorreta!!!')

    except Exception as e:
        errorlogin('Usuario incorreto!')

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
ususenha= ctk.CTkEntry(graycanva,width=160,height=10,placeholder_text='Senha',show='*')
ususenha.place(relx=0.23,rely=0.45)
#botão de login

buttonlogin = ctk.CTkButton(graycanva,width=120,height=20,text='Entrar',fg_color='#8651e8',text_color='#333233',command=lambda:logar(usuentry.get(),int(ususenha.get())))
buttonlogin.place(relx=0.3,rely=0.5)


root.mainloop()

