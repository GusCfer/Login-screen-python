import sqlite3
import customtkinter as ctk
import tkinter as tk
from customtkinter import *
import requests
from PIL import Image, ImageTk
import io

#conexão com banco de dados
conn = sqlite3.connect(r'C:\SQLITE\BANCOTESTE\DATA.db')
cursor = conn.cursor()

#definiçãoda função do clima
def clima(namecity):
    #toda configuração para trazer e armazenar os dados da requisição em variaveis
    global dados,icon,localizacao,temperatuura,condicoes,city_name
    city_name = namecity
    api_key = 'API_KEY_HERE'
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
    estado = localizacao['region']


   #WIDGETS DO CLIMA
    #chamando a requisição para buscar imagem do clima e inserindo na tela
    image = ("https:" + icon)
    requisicaoimagem = requests.get(image)
    image_data = requisicaoimagem.content
    image_pillow = Image.open(io.BytesIO(image_data))  
    image_ctk = ctk.CTkImage(light_image=image_pillow, size=(100,100))
    #chamando widgets da imagem 
    imagelabel = ctk.CTkLabel(master=root2,image=image_ctk,text='')
    imagelabel.place(relx=0.623,rely=0.05)
    #divisão
    divisao = ctk.CTkFrame(master=root2,height=400,width=6,fg_color='gray')
    divisao.place(relx=0.68,rely=0.25)
    #chamando os dados do clima e colocando na tela
    temp = ctk.CTkLabel(root2,text='Temperatura c°',font=('Calibri',20),text_color='#8651e8')
    temp.place(relx=0.45,rely=0.25)
    tempcity = ctk.CTkLabel(root2,text=temperatura,font=('Calibri',20))
    tempcity.place(relx=0.45,rely=0.3)
    #EM F
    temp2 = ctk.CTkLabel(root2,text='Temperatura f°',font=('Calibri',20),text_color='#8651e8')
    temp2.place(relx=0.75,rely=0.25)
    tempcity2 = ctk.CTkLabel(root2,text=temperaturaf,font=('Calibri',20))
    tempcity2.place(relx=0.75,rely=0.3)
    #status
    statusvar = ctk.CTkLabel(root2,text='Status',font=('Calibri',20),text_color='#8651e8')
    statusvar.place(relx=0.45,rely=0.35)
    statusvar = ctk.CTkLabel(root2,text=situacao,font=('Calibri',20))
    statusvar.place(relx=0.45,rely=0.4)
    #country
    temp = ctk.CTkLabel(root2,text='Pais',font=('Calibri',20),text_color='#8651e8')
    temp.place(relx=0.75,rely=0.355)
    tempcity = ctk.CTkLabel(root2,text=pais,font=('Calibri',20))
    tempcity.place(relx=0.75,rely=0.4)
    #ultimaconsulta
    temp = ctk.CTkLabel(root2,text='Ultima consulta',font=('Calibri',20),text_color='#8651e8')
    temp.place(relx=0.45,rely=0.45)
    tempcity = ctk.CTkLabel(root2,text=uconsulta,font=('Calibri',20))
    tempcity.place(relx=0.45,rely=0.5)
    #ESTADO
    estadlabel = ctk.CTkLabel(root2,text='Estado',font=('Calibri',20),text_color='#8651e8')
    estadlabel.place(relx=0.75,rely=0.45)
    estad = ctk.CTkLabel(root2,text=estado,font=('Calibri',20))
    estad.place(relx=0.75,rely=0.5)

    
#configuração padrão da janela
root2= ctk.CTk()
root2.geometry('800x600')
root2.resizable(False,False)
ctk.set_default_color_theme("green")
ctk.set_appearance_mode("dark")

#canva
frame = ctk.CTkFrame(root2,width=290,height=700,fg_color='#3d3d3d')
frame.place(relx=0.0,rely=-0.1)

#widgets padrão
label1 = ctk.CTkLabel(frame,text='Digite a Cidade:',font=('Calibri',15))
label1.place(relx=0.3,rely=0.35)

#campo para entrada de texto
selectioncity = ctk.CTkEntry(frame,width=160,height=10,placeholder_text='digite aqui!')
selectioncity.place(relx=0.2,rely=0.4)
selectioncity.insert(ctk.END,'')

#botão para chamar as informações
button = ctk.CTkButton(frame,width=100,height=30,text='PESQUISAR',fg_color='#8651e8',
                       command= lambda: clima(selectioncity.get()),text_color='black')
button.place(relx=0.3,rely=0.45)

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
#imagem background da tela de login
'''background = Image.open('C:\imagem\BACKGROUND.png')
image_ctk = ctk.CTkImage(light_image=background, size=(background.width,background.height))
backgroundlabel = ctk.CTkLabel(master=root,image=image_ctk,text='')
backgroundlabel.place(relx=0,rely=0)'''

#configuração do canva cinza que fica na direita (frame cinza)
graycanva = ctk.CTkFrame(root,width=290,height=700,fg_color='#3d3d3d')
graycanva.place(relx=0.65,rely=-0.1)
#widget texto e campo de digitação:
#FAÇA O LOGIN (Label)
text1 = ctk.CTkLabel(graycanva,text='Faça o Login:',font=('Calibri',15),text_color='#b1b2b3')
text1.place(relx=0.36,rely=0.35)
#USUENTRY (Entry) 
usuentry= ctk.CTkEntry(graycanva,width=160,height=10,placeholder_text='Usuário')
usuentry.place(relx=0.23,rely=0.4)
#USUSENHA (Entry)
ususenha= ctk.CTkEntry(graycanva,width=160,height=10,placeholder_text='Senha',show='*')
ususenha.place(relx=0.23,rely=0.45)

#botão de login (button)
buttonlogin = ctk.CTkButton(graycanva,width=120,height=20,text='ENTRAR',fg_color='#8651e8',text_color='#333233',
                            command=lambda:logar(usuentry.get(),int(ususenha.get())))
buttonlogin.place(relx=0.3,rely=0.5)

#definindo função de criar usuario
def createusu():
    #configurações da janela
    root3= ctk.CTkToplevel()
    root3.geometry('200x150')
    root3.resizable(False,False)
    #Criação dos widgets
    labelnewusu = ctk.CTkLabel(root3,text='Crie seu usuario! \n digite abaixo:', font=('Arial',15))
    labelnewusu.place(relx=0.25,rely=0.05)
    #entry para nome
    newusu= ctk.CTkEntry(root3,height=20,width=100,placeholder_text='Usuário')
    newusu.place(relx=0.27,rely=0.3)
    #entry para nova senha
    newpass= ctk.CTkEntry(root3,height=20,width=100,placeholder_text='Senha')
    newpass.place(relx=0.27,rely=0.45)
    
    #função para inserir novo usuario
    def insertnewusu(usu,senha):
        try:
            cursor.execute(f"insert into usuarios(nome,senha) values('{usu}',{senha})")
            conn.commit()
            mensagem = ctk.CTkLabel(root3,text='Criado com sucesso!',font=('Calibri',15),text_color='Green')
            mensagem.place(relx=0.2,rely=0.8)
        except Exception as e:
            mensagem = ctk.CTkLabel(root3,text='Erro!',font=('Calibri',15),text_color='Red')
            mensagem.place(relx=0.2,rely=0.8)
            print(e)
    
    buttoncreate = ctk.CTkButton(root3,height=20,width=70,text='CRIAR',text_color='Black',
                                 command=lambda:insertnewusu(str(newusu.get()),int(newpass.get())),fg_color='#8651e8')
    buttoncreate.place(relx=0.34,rely=0.64)

    root3.mainloop()

#botão de criar usuario
buttonusu = ctk.CTkButton(graycanva,width=120,height=15,text='criar usuario', fg_color='#3d3d3d',command=createusu)
buttonusu.place(relx=0.3,rely=0.53)

root.mainloop()

