from tkinter import *
from cores import *

janela = Tk()


class App_login():
    def __init__(self):
        self.janela = janela

        # Atributos do logo
        self.foto_logo = PhotoImage(file='imagens/logo.png')
        self.logo = Label(image=self.foto_logo)

        # Atributos das labels
        self.label_usuario = Label(text='Usuário: ')
        self.label_senha = Label(text='Senha: ')

        # Atributos para os inputs
        self.img_inputs = PhotoImage(file='imagens/inputs.png')
        self.img_input_usuario = Label(image=self.img_inputs, bd=0, bg=vermelho_fundo)
        self.img_input_senha = Label(image=self.img_inputs, bd=0, bg=vermelho_fundo)
        self.input_usuario = Entry()
        self.input_senha = Entry()

        #  Atributos para o botão de jogin da janela de login
        self.img_btn_login = PhotoImage(file='imagens/bt_login.png')
        self.bt_login = Button(image=self.img_btn_login, background=vermelho_fundo, bd=0,
                               activebackground=vermelho_fundo)

        self.login()

        janela.mainloop()

    def login(self):
        # Tela de login
        self.janela.title('Login')
        self.janela.configure(background=vermelho_fundo)
        #  self.janela.attributes('-alpha', 0.7)
        self.janela.geometry('500x500')
        self.janela.resizable(False, False)

        # Logo centrarl
        self.logo.place(x=200, y=53, width=140, height=140)
        self.logo.configure(bg=vermelho_fundo, bd=0)

        # Labels e inputs para login
        # ------------------------------------------------- Usuário ----------------------------------------------------
        self.label_usuario.place(x=70, y=250)
        self.label_usuario.configure(background=vermelho_fundo, font=('Arial', 15), fg='white')
        self.input_usuario.place(x=160, y=253, width=270, height=20)
        self.input_usuario.configure(bg='#D9D9D9', bd=0, font=('Arial', 12))
        self.img_input_usuario.place(x=150, y=245, width=290, height=50)
        self.img_input_usuario.configure(bd=0)
        # --------------------------------------------------------------------------------------------------------------
        # ------------------------------------------------- Senha ------------------------------------------------------
        self.label_senha.place(x=80, y=307)
        self.label_senha.configure(background=vermelho_fundo, font=('Arial', 15), fg='white')
        self.input_senha.place(x=160, y=315, width=270, height=20)
        self.input_senha.configure(bg='#D9D9D9', bd=0, show='*', font=('Arial', 15))
        self.img_input_senha.place(x=150, y=305, width=290, height=50)
        # --------------------------------------------------------------------------------------------------------------
        # Botão de login da janela
        self.bt_login.place(x=180, y=392, width=177, height=45)


