from tkinter import *
from utils import Funcoes as f
from cores import *


class App(f):
    def __init__(self):
        self.janela = Tk()

        # ---------------------------------- Atributos da tela de login ------------------------------------------------
        # Atributos do logo
        self.foto_logo = PhotoImage(file='imagens/logo.png')
        self.logo = Label(image=self.foto_logo)
        # Atributos das labels
        self.label_usuario = Label(text='Usuário: ')
        self.label_senha = Label(text='Senha: ')
        # Atributos para os inputs
        self.img_inputs = PhotoImage(file='imagens/inputs.png')
        self.img_input_usuario = Label(image=self.img_inputs, bd=0, bg=fundo_login)
        self.img_input_senha = Label(image=self.img_inputs, bd=0, bg=fundo_login)
        self.input_usuario = Entry()
        self.input_senha = Entry()
        #  Atributos para o botão de jogin da janela de login
        self.img_btn_login = PhotoImage(file='imagens/bt_login.png')
        self.bt_login = Button(image=self.img_btn_login, background=fundo_login, bd=0,
                               activebackground=fundo_login, command=self.logar)
        # --------------------------------------------------------------------------------------------------------------
        # -------------------------------------- Atributos da tela principal -------------------------------------------
        self.frame_lateral = Frame()
        self.frame_superior = Frame()
        self.frame_inferior = Frame()

        self.principal()
        self.janela.mainloop()

    def login(self):
        # Configurações da tela de login
        self.janela.title('Login')
        self.janela.configure(background=fundo_login)
        #  self.janela.attributes('-alpha', 0.7)
        self.janela.geometry('500x500')
        self.janela.resizable(False, False)

        # Logo centrarl
        self.logo.place(x=200, y=53, width=140, height=140)
        self.logo.configure(bg=fundo_login, bd=0)

        # Labels e inputs para login
        # ------------------------------------------------- Usuário ----------------------------------------------------
        self.label_usuario.place(x=70, y=250)
        self.label_usuario.configure(background=fundo_login, font=('Arial', 15), fg='white')
        self.input_usuario.place(x=160, y=253, width=270, height=20)
        self.input_usuario.configure(bg='#D9D9D9', bd=0, font=('Arial', 12))
        self.img_input_usuario.place(x=150, y=245, width=290, height=50)
        self.img_input_usuario.configure(bd=0)
        # --------------------------------------------------------------------------------------------------------------
        # ------------------------------------------------- Senha ------------------------------------------------------
        self.label_senha.place(x=80, y=307)
        self.label_senha.configure(background=fundo_login, font=('Arial', 15), fg='white')
        self.input_senha.place(x=160, y=315, width=270, height=20)
        self.input_senha.configure(bg='#D9D9D9', bd=0, show='*', font=('Arial', 15))
        self.img_input_senha.place(x=150, y=305, width=290, height=50)
        # --------------------------------------------------------------------------------------------------------------
        # Botão de login da janela
        self.bt_login.place(x=180, y=392, width=177, height=45)

    def principal(self):
        # Configurações da tela principal
        self.janela.title('Principal')
        self.janela.geometry('800x800')
        self.janela.minsize(width=800, height=800)
        self.janela.resizable(True, True)
        self.janela.configure(bg=fundo_principal)

        # ------------------------------------------- Frames -----------------------------------------------------------
        # Frame lateral
        self.frame_lateral.place(relx=0.01, rely=0.02, relheight=0.96, relwidth=0.15)
        self.frame_lateral.configure(highlightbackground='#474747', highlightthickness=3)
        # Frame superior
        self.frame_superior.place(relx=0.18, rely=0.02, relwidth=0.81, relheight=0.47)
        self.frame_superior.configure(highlightbackground='#474747', highlightthickness=3)
        # Frame inferior
        self.frame_inferior.place(relx=0.18, rely=0.53, relwidth=0.81, relheight=0.45)
        self.frame_inferior.configure(highlightbackground='#474747', highlightthickness=3)

    def logar(self):
        usuario = self.input_usuario.get()
        senha = self.input_senha.get()

        if usuario == 'admin' and senha == 'admin':
            self.principal()
            self.input_senha.destroy()
            self.label_senha.destroy()
            self.img_input_senha.destroy()
            self.input_usuario.destroy()
            self.img_input_usuario.destroy()
            self.label_usuario.destroy()
            self.bt_login.destroy()
            self.logo.destroy()
