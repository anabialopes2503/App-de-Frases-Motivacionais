from tkinter import *     # Importa biblioteca tkinter

class Informacao(Toplevel):   # Tela de login
    #Cores
    cor1 = '#ffffff'
    cor2 = '#000000'
    cor3 = '#ffc2e2'
    cor4 = '#9BF6FF'
    cor5 = '#b892ff'

    def __init__(self, original):
        self.frame_original = original

        Toplevel.__init__(self)  # Importando Método construtor
        self.geometry('375x667+979+15')   #Geometria
        self.iconbitmap("f2.ico")  # Ícone
        self.title('Menu')  # Título
        self.configure(bg=self.cor2)  # Cor de fundo
        self.frames()  # Mostrar frames
        self.widgets_frame1()  # Mostrar widgets

        self.btn = Button(  # Configuração do botão
            self,
            text= 'VOLTAR', # Texto
            bg=self.cor2, # Cor do botão
            activebackground=self.cor2,  # Cor clicado
            fg=self.cor5, # Cor da fonte
            activeforeground=self.cor5,  # Cor fonte clicado
            command=self.onClose)  # Comando do Botão
        self.btn.place(relx=0.050, rely=0)  # Medida do botão

    def onClose(self):  # Função do botão
        self.destroy()  # Fechar a janela
        self.frame_original.show()  # Mostrar janela anterior

    def frames(self):
        # Frame 1
        self.frame1 = Frame(self, bg=self.cor4)
        self.frame1.place(
            relx=0.05,  # Onde começa horizontal
            rely=0.05,  # Onde começa vertical
            relwidth=0.9,  # Largura do frame
            relheight=0.1)  # Altura do frame

        # Frame 2
        self.frame2 = Frame(self, bg=self.cor1)
        self.frame2.place(relx=0.080, rely=0.06, relwidth=0.84, relheight=0.08)

        # Frame 3
        self.frame3 = Frame(self, bg=self.cor4)
        self.frame3.place(relx=0.05, rely=0.200, relwidth=0.9, relheight=0.70)

        titulo = Label(  # Configuração do texto
            self.frame2, # Onde está localizado
            text='INFORMAÇAO DO APP',  # Texto
            font=('Times New Roman', 20, 'bold'),  # Fonte, Tamanho e Negrito
            bg=self.cor4,  # Cor do fundo do texto
            fg=self.cor5)  # Cor da fonte
        titulo.pack(padx=0, pady=9)  # Distância do texto

        inform = Label(  # Configuração do texto
            self.frame3,  # Onde está localizado
            text='Polisipo',  # Texto
            font=('Times New Roman', 25),  # Fonte, Tamanho
            bg=self.cor2,  # Cor do fundo do texto
            fg=self.cor5)  # Cor da fonte
        inform.pack(padx=0, pady=40)  # Distância do texto

        inform = Label(  # Configuração do texto
            self.frame3,  # Onde está localizado
            text='Criado por Ana Beatriz Lopes,\n Anna Gabriela Nascimento,\n Emanuelle Oliveira,\n Júlia Corrêa,\n Thayssa Porto e\n Yasmim Mota',  # Texto
            font=('Times New Roman', 10),  # Fonte, Tamanho
            bg=self.cor2,  # Cor do fundo do texto
            fg=self.cor5)  # Cor da fonte
        inform.pack(padx=0, pady=40)  # Distância do texto

        inform = Label(  # Configuração do texto
            self.frame3,  # Onde está localizado
            text='Data da criação = 24/05/2021',  # Texto
            font=('Times New Roman', 12),  # Fonte, Tamanho
            bg=self.cor2,  # Cor do fundo do texto
            fg=self.cor5)  # Cor da fonte
        inform.pack(padx=0, pady=40)  # Distância do texto

        inform = Label(  # Configuração do texto
            self.frame3,  # Onde está localizado
            text='Versão: 1.1',  # Texto
            font=('Times New Roman', 11),  # Fonte e Tamanho
            bg=self.cor2,  # Cor do fundo do texto
            fg=self.cor5)  # Cor da fonte
        inform.pack(padx=0, pady=15)  # Distância do texto

    def widgets_frame1(self):  # Botão
        # Configuração dos botões
        self.btn_fechar = Button(
            self,
            text='FECHAR',  # Texto
            bg=self.cor2,  # Cor do botão
            activebackground=self.cor2,  # Cor clicado
            fg=self.cor5,  # Cor da fonte
            activeforeground=self.cor5,  # Cor fonte clicado
            command=self.fechar)  # Comando do botão
        self.btn_fechar.place(relx=0.8, rely=0)  # Medidas do botão

    def fechar(self):
        self.destroy() # Fechar janela

class Motivacao(Toplevel):
    # Cores
    cor1 = '#ffffff'
    cor2 = '#000000'
    cor3 = '#ffc2e2'
    cor4 = '#9BF6FF'
    cor5 = '#b892ff'

    def __init__(self, original):
        self.frame_original = original

        Toplevel.__init__(self)  # Importando Método construtor
        self.geometry('375x667+979+15')  # Geometria
        self.iconbitmap("f2.ico")  # Ícone
        self.title('Mensagens Motivacionais')  # Título
        self.configure(bg=self.cor2)  # Cor de fundo
        self.frames()  # Mostrar frames
        self.widgets_frame1()  # Mostrar widgets

        self.btn = Button(  # Configuração do botão
            self,
            text='VOLTAR',  # Texto
            bg=self.cor2,  # Cor do botão
            activebackground=self.cor2,  # Cor clicado
            fg=self.cor5,  # Cor da fonte
            activeforeground=self.cor5 ,  # Cor fonte clicado
            command=self.onClose)  # Comando do botão
        self.btn.place(relx=0.050, rely=0)  # Medidas do botão

    def onClose(self):
        self.destroy()  # Fechar janela
        self.frame_original.show()  # Mostrar janela anterior

    def frames(self):
        # Frame 1
        self.frame1 = Frame(self, bg=self.cor4)
        self.frame1.place(relx=0.05, rely=0.060, relwidth=0.9, relheight=0.8)

        # Frases
        msgm1 = Label(
            self.frame1,  # Onde está localizado
            text='Apaixone-se pelo processo de se tornar a melhor versão de você.',
            font=('Times New Roman', 9, 'bold'),  #
            bg=self.cor2,
            fg=self.cor5)
        msgm1.pack(padx=0, pady=40)

        msgm2 = Label(
            self.frame1,
            text='Não importa a cor do céu, quem faz o dia bonito é você.',  # Texto
            font=('Times New Roman', 9, 'bold'),  # Fonte, tamanho e negrito
            bg=self.cor2,
            fg=self.cor5)
        msgm2.pack(padx=0, pady=45)

        msgm3 = Label(
            self.frame1,
            text='Que o dia comece bem e termine ainda melhor.',
            font=('Times New Roman', 9, 'bold'),
            bg=self.cor2,  # Cor de fundo
            fg=self.cor5)  # Cor da fonte
        msgm3.pack(padx=0, pady=50)

        msgm4 = Label(
            self.frame1,
            text='Você é forte, suficiente e capaz.',
            font=('Times New Roman', 9, 'bold'),
            bg=self.cor2,
            fg=self.cor5)
        msgm4.pack(padx=0, pady=60)  # Medidas do texto

    def widgets_frame1(self):  # Botão
        # Configuração dos botões
        self.btn_fechar = Button(
            self,
            text='FECHAR',  # Texto
            bg=self.cor2,  # Cor do botão
            activebackground=self.cor2,  # Cor clicado
            fg=self.cor5,  # Cor da fonte
            activeforeground=self.cor5,  # Cor fonte clicado
            command=self.fechar)  # Comando do botão
        self.btn_fechar.place(relx=0.8, rely=0)  # Medidas do botão

    def fechar(self):
        self.destroy()  # Fechar janela

class Reflexao(Toplevel):
    #Cores
    cor1 = '#ffffff'
    cor2 = '#000000'
    cor3 = '#ffc2e2'
    cor4 = '#9BF6FF'
    cor5 = '#b892ff'

    def __init__(self, original):
        self.frame_original = original

        Toplevel.__init__(self)  # Importando Método construtor
        self.geometry('375x667+979+15')  # Geometria
        self.iconbitmap("f2.ico")  # Ícone
        self.title('Mensagem de reflexão')  # Título
        self.configure(bg=self.cor2)  # Cor de fundo
        self.frames()  # Mostrar frames
        self.widgets_frame1()  # Mostrar widgets

        self.btn = Button(  # Configuração do botão
            self,
            text='VOLTAR', # Texto
            bg=self.cor2, # Cor do botão
            activebackground=self.cor2, # Cor clicado
            fg=self.cor5, # Cor da fonte
            activeforeground=self.cor5,  # Cor fonte clicado
            command=self.onClose) # Comando do botão
        self.btn.place(relx=0.050, rely=0) # Medidas do botão

    def onClose(self):
        self.destroy()  # Fechar a janela
        self.frame_original.show() # Mostrar janela anterior

    def frames(self):
        # Frame 1
        self.frame1 = Frame(self, bg=self.cor4)
        self.frame1.place(relx=0.05, rely=0.060, relwidth=0.9, relheight=0.8)

        # Frases
        msg1 = Label( # Configuração do texto
            self.frame1, # Onde está localizado
            text='Tudo o que um sonho precisa para ser realizado\n é alguém que acredite que ele possa ser realizado.', # Texto
            font=('Times New Roman', 9, 'bold'), # Fonte e Tamanho
            bg=self.cor2, # Cor do fundo do texto
            fg=self.cor5) # Cor da fonte
        msg1.pack(padx=0, pady=40) # Distância do texto

        msg2 = Label( # Configuração do texto
            self.frame1, # Onde está localizado
            text='Não espere por uma crise para descobrir\n o que é importante em sua vida.', # Texto
            font=('Times New Roman', 9, 'bold'), # Fonte, Tamanho e Negrito
            bg=self.cor2, # Cor do fundo do texto
            fg=self.cor5) # Cor da fonte
        msg2.pack(padx=0, pady=45) # Distância do texto

        msg3 = Label( # Configuração do texto
            self.frame1, # Onde está localizado
            text='Pessimismo leva à fraqueza,\n otimismo ao poder.', # Texto
            font=('Times New Roman', 9, 'bold'), # Fonte, Tamanho e Negrito
            bg=self.cor2, # Cor do fundo do texto
            fg=self.cor5)  # Cor da fonte
        msg3.pack(padx=0, pady=50) # Distância do texto

        msg4 = Label( # Configuração do texto
            self.frame1, # Onde está localizado
            text='Somente quando encontramos o amor,\n é que descobrimos o que nos faltava na vida.', # Texto
            font=('Times New Roman', 9, 'bold'), # Fonte, Tamanho e Negrito
            bg=self.cor2, # Cor do fundo do texto
            fg=self.cor5)  # Cor da fonte
        msg4.pack(padx=0, pady=55) # Distância do texto

    def widgets_frame1(self):
        # Configuração dos botões
        self.btn_fechar = Button(
            self,
            text='FECHAR', # Texto
            bg=self.cor2, # Cor do botão
            activebackground=self.cor2,
            fg=self.cor5, # Cor da fonte
            activeforeground=self.cor5,
            command=self.fechar) # Comando do botão
        self.btn_fechar.place(relx=0.8, rely=0) # Medidas do botão

    def fechar(self):
        self.destroy() # Fechar janela

class Menu(Toplevel):
    # Cores
    cor1 = '#ffffff'
    cor2 = '#000000'
    cor3 = '#ffc2e2'
    cor4 = '#9BF6FF'
    cor5 = '#b892ff'

    def __init__(self, original):
        self.frame_original = original

        Toplevel.__init__(self) # Importando Método construtor
        self.geometry('375x667+979+15') # Geometria
        self.iconbitmap("f2.ico")  # Ícone
        self.title('Menu') # Título
        self.configure(bg=self.cor2) # Cor de fundo
        self.frames() # Mostrar frames
        self.widgets_frame1() # Mostrar widgets

        self.btn = Button( #Configuração do botão
            self,
            text= 'VOLTAR', #Texto
            bg=self.cor2, #Cor do botão
            activebackground=self.cor2,  #Cor clicado
            fg=self.cor5, #Cor da fonte
            activeforeground=self.cor5,  #Cor fonte clicado
            command=self.onClose) #Comando do botão
        self.btn.place(relx=0.050, rely=0) #Medida do botão

    def onClose(self):
        self.destroy() #Fechar janela
        self.frame_original.show() #Abrir janela anterior

    def frames(self):
        # Frame 1
        self.frame1 = Frame(self, bg=self.cor1)
        self.frame1.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.1)

        # Frame 2
        self.frame2 = Frame(self, bg=self.cor4)
        self.frame2.place(relx=0.080, rely=0.06, relwidth=0.84, relheight=0.08)

        # Frame 3
        self.frame3 = Frame(self, bg=self.cor4)
        self.frame3.place(relx=0.05, rely=0.200, relwidth=0.9, relheight=0.70)

        mn = Label( #Configuração do texto
            self.frame2, #Onde está localizado
            text='MENU', #Texto
            font=('Times New Roman', 20, 'bold'), #Fonte, Tamanho e Negrito
            bg=self.cor2, #Cor do fundo do texto
            fg=self.cor1) #Cor da fonte
        mn.pack(padx=0, pady=9) #Distância do texto

    def widgets_frame1(self): #Botões
        # Configuração dos botões
        self.btn_clicar1 = Button(
            self.frame3, #Onde está localizado
            text='Mensagens de reflexão', #Texto
            bg=self.cor2, #Cor do botão
            activebackground=self.cor2,  # Cor clicado
            font=('Times New Roman', 15), #Fonte e Tamanho
            fg=self.cor1, #Cor da fonte
            activeforeground=self.cor1,  #Cor fonte clicado
            command=self.clicar1) #Comando do botão
        self.btn_clicar1.pack(padx=0, pady=45) #Distância do botão

        self.btn_clicar2 = Button(
            self.frame3, #Onde está localizado
            text='Mensagens motivacionais', #Texto
            bg=self.cor2, #Cor do botão
            activebackground=self.cor2,
            font=('Times New Roman', 15), #Fonte e Tamanho
            fg=self.cor1, #Cor da fonte
            activeforeground=self.cor1,
            command=self.clicar2) #Comando do botão
        self.btn_clicar2.pack(padx=0, pady=60) #Distância do botão

        self.btn_clicar3 = Button(
            self.frame3, #Onde está localizado
            text='Informação do app', #Texto
            bg=self.cor2, #Cor do botão
            activebackground=self.cor2,
            font=('Times New Roman', 15),#Fonte e Tamanho
            fg=self.cor1, #Cor da fonte
            activeforeground=self.cor1,
            command=self.clicar3) #Comando do botão
        self.btn_clicar3.pack(padx=0, pady=65) #Distância do botão

        self.btn_fechar = Button(
            self,
            text='FECHAR', #Texto
            bg=self.cor2, #Cor do botão
            activebackground=self.cor2,
            fg=self.cor5, #Cor da fonte
            activeforeground=self.cor5,
            command=self.fechar) #Comando do botão
        self.btn_fechar.place(relx=0.8, rely=0) #Medida do botão

    def clicar1(self):
        self.hide() #Esconder janela
        self.subFrame = Reflexao(self) #Janela que irá abrir

    def clicar2(self):
        self.hide() #Esconder janela
        self.subFrame = Motivacao(self) #Janela que irá abrir

    def clicar3(self):
        self.hide() #Esconder janela
        self.subFrame = Informacao(self) #Janela que irá abrir

    def fechar(self):
        self.destroy() #Fechar janela

    def hide(self): #Esconder janela
        self.withdraw()

    def show(self): #Mostrar a outra janela
        self.update()
        self.deiconify()

class Inicio(Toplevel):
    # Cores
    cor1 = '#ffffff'
    cor2 = '#000000'
    cor3 = '#ffc2e2'
    cor4 = '#9BF6FF'
    cor5 = '#b892ff'

    def __init__(self, original):
        self.frame_original = original

        Toplevel.__init__(self) #Importando Método construtor
        self.geometry('375x667+979+15') #Geometria
        self.iconbitmap("f2.ico")  # Ícone
        self.title('Pagina Inicial') #Título
        self.configure(bg=self.cor2) #Cor da tela
        self.frames() #Mostrar frames
        self.widgets_frame1() #Mostrar widgets

        self.btn = Button( #Configuração do botão
            self,
            text='VOLTAR', #Texto
            bg=self.cor2, #Cor do botão
            activebackground=self.cor2,
            fg=self.cor5, #Cor da fonte
            activeforeground=self.cor5,
            command=self.onClose) #Comando do botão
        self.btn.place(relx=0.050, rely=0) #Medida do botão

    def onClose(self):
        self.destroy() #Fechar janela
        self.frame_original.show() #Mostrar janela anterior

    def frames(self):
        # Frame 1
        self.frame1 = Frame(self, bg=self.cor4)
        self.frame1.place(relx=0.05, rely=0.060, relwidth=0.9, relheight=0.8)

        # Textos
        inicial = Label( #Configuração do texto
            self.frame1, #Onde está localizado
            text='SEJA BEM-VINDO (A)', #Texto
            font=('Times New Roman', 20, 'bold'), #Fonte, Tamanho e Negrito
            bg=self.cor4, #Cor do fundo do texto
            fg=self.cor2) #Cor da fonte
        inicial.pack(padx=0, pady=45) #Distância do texto

        apresentacao = Label( #Configuração do texto
            self.frame1, #Onde está localizado
            text='Quero primeiramente deixar registrado que: ', #Texto
            font=('Times New Roman', 13), #Fonte e Tamanho
            bg=self.cor4, #Cor do fundo do texto
            fg=self.cor2) #Cor da fonte
        apresentacao.pack(padx=0, pady=60) #Distância do texto

        frase = Label( #Configuração do texto
            self.frame1, #Onde está localizado
            text=' Este é o lugar onde se encontra a paz! ', #Texto
            font=('Times New Roman', 15),  #Fonte e Tamanho
            bg=self.cor4, #Cor do fundo do texto
            fg=self.cor2) #Cor da fonte
        frase.pack(padx=0, pady=65) #Distância do texto

    def widgets_frame1(self): #Botões
        self.btn_confirmar = Button( #Configuração do botão
            self.frame1, #Onde está localizado
            text='Ok!', #Texto
            bg=self.cor4, #Cor do botão
            activebackground=self.cor4,
            font=('Times New Roman', 15, 'bold'), #Fonte, Tamanho e Negrito
            fg=self.cor2, #Cor da fonte
            activeforeground=self.cor2,
            command=self.confirmar) #Comando do botão

        self.btn_confirmar.place( #Configuração das medidas do botão
            relx=0.3, #Onde começa horizontal
            rely=0.80, #Onde começa vertical
            relwidth=0.4, #Largura
            relheight=0.1) #Altura

        self.btn_fechar = Button(self, text='FECHAR', bg=self.cor2, activebackground=self.cor2, fg=self.cor5,
                                 activeforeground=self.cor5, command=self.fechar)
        self.btn_fechar.place(relx=0.8, rely=0)

    def confirmar(self):
        self.hide() #Esconder janela
        self.subFrame = Menu(self) #Janela que irá abrir

    def fechar(self):
        self.destroy() #Fechar janela

    def hide(self): #Esconder janela
        self.withdraw()

    def show(self): #Mostrar outra janela
        self.update()
        self.deiconify()

class Cadastro(Toplevel):
     # Cores
    cor1 = '#ffffff'
    cor2 = '#000000'
    cor3 = '#ffc2e2'
    cor4 = '#ff90b3'
    cor5 = '#b892ff'

    def __init__(self, original):
        self.frame_original = original

        Toplevel.__init__(self) #Importando Método construtor
        self.geometry('375x667+979+15') #Geometria
        
        self.title('Login') #Título
        self.configure(bg=self.cor2) #Cor de fundo
        self.frames() #Mostrar frames
        self.widgets_frame1() #Mostrar widgets
        self.iconbitmap("f3.ico")  # Ícone

        self.btn = Button( #Configuração do botão
            self,
            text='VOLTAR', #Texto
            bg=self.cor2, #Cor do botão
            activebackground=self.cor2,
            fg=self.cor5, #Cor da fonte
            activeforeground=self.cor5,
            command=self.onClose) #Comando do botão
        self.btn.place(relx=0.050, rely=0) #Medida do botão

    def onClose(self):
        self.destroy() #Fechar janela
        self.frame_original.show() #Mostrar janela anterior

    def frames(self):
        # Frame 1
        self.frame1 = Frame(self, bg=self.cor1)
        self.frame1.place(relx=0.05, rely=0.060, relwidth=0.9, relheight=0.8)

        # Frame 2
        self.frame2 = Frame(self, bg=self.cor2)
        self.frame2.place(relx=0.10, rely=0.11, relwidth=0.8, relheight=0.7)

        # Textos
        entrada = Label( #Configuração do texto
            self.frame2, #Onde está localizado
            text='CADASTRO:', #Texto
            font=('Times New Roman', 25, 'bold'), #Fonte, Tamanho e Negrito
            bg=self.cor2, #Cor do fundo do texto
            fg=self.cor1) #Cor da fonte
        entrada.pack(padx=0, pady=45) #Distância do texto

        text_nome = Label( #Configuração do texto
            self.frame2, #Onde está localizado
            text='Nome:', #Texto
            font=('Times New Roman', 15, 'bold'), #Fonte, Tamanho e Negrito
            bg=self.cor2,  #Cor do fundo do texto
            fg=self.cor5)  #Cor da fonte
        text_nome.place(relx=0.08, rely=0.25) #Medida do texto

        ent_nome = Entry(  # Entrada de texto
            self.frame2,
        )
        ent_nome.place(relx=0.09, rely=0.30, width=105)

        text_sobrenome = Label( #Configuração do texto
            self.frame2, #Onde está localizado
            text='Sobrenome:', #Texto
            font=('Times New Roman', 15, 'bold'), #Fonte, Tamanho e Negrito
            bg=self.cor2, #Cor do fundo do texto
            fg=self.cor5) #Cor da fonte
        text_sobrenome.place(relx=0.50, rely=0.25) #Medida do texto

        ent_sobrenome = Entry(
            self.frame2,
        )
        ent_sobrenome.place(relx=0.51, rely=0.30, width=119)  # Localização

        text_email = Label( #Configuração do texto
            self.frame2, #Onde está localizado
            text='Email:', #Texto
            font=('Times New Roman', 15, 'bold'), #Fonte, Tamanho e Negrito
            bg=self.cor2, #Cor do fundo do texto
            fg=self.cor5) #Cor da fonte
        text_email.place(relx=0.08, rely=0.35) #Medida do texto

        ent_email = Entry(
            self.frame2,
        )
        ent_email.place(relx=0.09, rely=0.40, width=245)

        text_senha = Label( self.frame2, text='Senha:', font=('Times New Roman', 15, 'bold'), bg=self.cor2, fg=self.cor5)
        text_senha.place(relx=0.08, rely=0.45)

        ent_senha = Entry(
            self.frame2
        )
        ent_senha.place(relx=0.09, rely=0.50, width=245)

        text_lgn = Label( #Configuração do texto
            self.frame2, #Onde está localizado
            text='Já tem uma conta?', #Texto
            font=('Times New Roman', 15), #Fonte e Tamanho
            bg=self.cor2, #Cor do fundo do texto
            fg=self.cor5) #Cor da fonte
        text_lgn.place(relx=0.08, rely=0.80) #Medida do texto


    def widgets_frame1(self): #Botões
        # Configuração dos botões
        self.btn_cadastro = Button(
            self.frame2, #Onde está localizado
            text='Cadastrar', #Texto
            bg=self.cor1, #Cor do botão
            activebackground=self.cor1,
            font=('Times New Roman', 15), #Fonte e Tamanho
            fg=self.cor2, #Cor da fonte
            activeforeground=self.cor2,
            command=self.entrar) #Comando do botão

        self.btn_cadastro.place( #Medida do botão
            relx=0.3, #Onde começa horizontal
            rely=0.58, #Onde começa vertical
            relwidth=0.4, #Largura
            relheight=0.1) #Altura

        self.btn_login = Button(self.frame2, text='Login', bg=self.cor1, activebackground=self.cor1, font=('Times New Roman', 15),
                                fg=self.cor2, activeforeground=self.cor2, command=self.voltar)

        self.btn_login.place(relx=0.59, rely=0.8, relwidth=0.35, relheight=0.06)

        self.btn_fechar = Button(
            self,
            text='FECHAR', #Texto
            bg=self.cor2, #Cor do botão
            activebackground=self.cor2,
            fg=self.cor5, #Cor da fonte
            activeforeground=self.cor5,
            command=self.fechar) #Comando do botão
        self.btn_fechar.place(relx=0.8, rely=0) #Medida do botão

    def entrar(self):
        self.hide() #Esconder janela
        self.subFrame = Inicio(self) #Janela que irá abrir

    def voltar(self):
        self.hide() #Esconder janela
        self.subFrame = Login(self) #Janela que irá abrir

    def fechar(self):
        self.destroy() #Fechar janela

    def hide(self): #Esconder janela
        self.withdraw()

    def show(self): #Mostrar outra janela
        self.update()
        self.deiconify()

class Login(Toplevel):
    #  Cores
    cor1 = '#ffffff'
    cor2 = '#000000'
    cor3 = '#ffc2e2'
    cor4 = '#ff90b3'
    cor5 = '#b892ff'

    def __init__(self, original):
        self.frame_original = original

        Toplevel.__init__(self) #Importando Método construtor
        self.geometry('375x667+979+15') #Geometria
        self.iconbitmap("f3.ico")
        self.title('Login') #Título
        self.configure(bg=self.cor2) #Cor da tela
        self.frames() #Mostrar frames
        self.widgets_frame1() #Mostrar widgets

        self.btn = Button( #Configuração do botão
            self,
            text='VOLTAR', #Texto
            bg=self.cor2,#Cor do botão
            activebackground=self.cor2,
            fg=self.cor5, #Cor da fonte
            activeforeground=self.cor5,
            command=self.onClose) #Comando do botão
        self.btn.place(relx=0.050, rely=0) #Medida do botão

    def onClose(self):
        self.destroy() #Fechar janela
        self.frame_original.show() #Mostrar janela anterior

    def frames(self):
        # Frame 1
        self.frame1 = Frame(self, bg=self.cor1)
        self.frame1.place(relx=0.05, rely=0.060, relwidth=0.9, relheight=0.8)

        self.frame2 = Frame(self, bg=self.cor2)
        self.frame2.place(relx=0.10, rely=0.11, relwidth=0.8, relheight=0.7)

        entrada = Label( #Configuração do texto
            self.frame2, #Onde está localizado
            text='LOGIN', #Texto
            font=('Times New Roman', 25, 'bold'), #Fonte, Tamanho e Negrito
            bg=self.cor2, #Cor do fundo do texto
            fg=self.cor1) #Cor da fonte
        entrada.pack(padx=0, pady=45) #Distância do texto

        text_login = Label( #Configuração do texto
            self.frame2, #Onde está localizado
            text='Usuário:', #Texto
            font=('Times New Roman', 15, 'bold'), #Fonte, Tamanho e Negrito
            bg=self.cor2, #Cor do fundo do texto
            fg=self.cor5) #Cor da fonte
        text_login.place(relx=0.08, rely=0.25) #Medida do texto

        ent_login = Entry(
            self.frame2,
        )
        ent_login.place(relx=0.09, rely=0.30, width=230)

        text_senha = Label( #Configuração do texto
            self.frame2, #Onde está localizado
            text='Senha:', #Texto
            font=('Times New Roman', 15, 'bold'), #Fonte, Tamanho e Negrito
            bg=self.cor2, #Cor do fundo do texto
            fg=self.cor5) #Cor da fonte
        text_senha.place(relx=0.08, rely=0.40) #Medida do texto

        ent_senha = Entry(   # Entrada de texto
            self.frame2
        )
        ent_senha.place(relx=0.09, rely=0.45, width=230)

    def widgets_frame1(self): #Botões
        # Configuração dos botões
        self.btn_entrar = Button(
            self.frame2, #Onde está localizado
            text='Entrar', #Texto
            bg=self.cor1, #Cor do botão
            activebackground=self.cor1,
            font=('Times New Roman', 15), #Fonte e Tamanho
            fg=self.cor2, #Cor da fonte
            activeforeground=self.cor2,
            command=self.entrar) #Comando do botão

        self.btn_entrar.place( #Medida do botão
            relx=0.3, #Onde começa horizontal
            rely=0.55, #Onde começa vertical
            relwidth=0.4, #Largura
            relheight=0.1) #Altura

        self.btn_fechar = Button(
            self,
            text='FECHAR', #Texto
            bg=self.cor2, #Cor do botão
            activebackground=self.cor2,
            fg=self.cor5, #Cor da fonte
            activeforeground=self.cor5,
            command=self.fechar) #Comando do botão
        self.btn_fechar.place(relx=0.8, rely=0) #Medida do botão

    def entrar(self):
        self.hide() #Esconder janela
        self.subFrame = Inicio(self) #Janela que irá abrir

    def fechar(self):
        self.destroy() #Fechar janela

    def hide(self): #Esconder janela
        self.withdraw()

    def show(self): #Mostrar outra janela
        self.update()
        self.deiconify()

class App:
    #Cores
    cor1 = '#ffffff'
    cor2 = '#000000'
    cor3 = '#ffc2e2'
    cor4 = '#ff90b3'
    cor5 = '#b892ff'
    

    def __init__(self): # O que vai rodar
        self.root = root
        self.tela()
        self.frames()
        self.widgwts_frame1()
        self.widgets_frame2()
        root.mainloop()

    def tela(self):
        self.root.geometry('375x667+978+15') #Geometria
        self.root.iconbitmap("f4_1.ico")  # Ícone
        self.root.title('Polisipo Motivation') #Título
        self.root.configure(bg=self.cor2) #Cor de fundo

    def frames(self):
        # Frame 1
        self.frame1 = Frame(root, bg=self.cor1)
        self.frame1.place(relx=0.05, rely=0.04, relwidth=0.9, relheight=0.70)

        # Frame 2
        self.frame2 = Frame(self.root, bg=self.cor2)
        self.frame2.place(relx=0.05, rely=0.8, relwidth=0.9, relheight=0.175)

        # Frame 3
        self.frame3 = Frame(root, bg=self.cor2)
        self.frame3.place(relx=0.1, rely=0.52, relwidth=0.8, relheight=0.200)

        # Texto
        entrada = Label( #Configuração do texto
            self.frame3, #Onde está localizado
            text='Polisipo Motivation', #Texto
            font=('Times New Roman', 23), #Fonte e Tamanho
            bg=self.cor2, #Cor do fundo
            fg=self.cor5) #Cor da fonte
        entrada.pack(padx=0, pady=15) #Distância do texto

        log3 = Label( self.frame3, text='Lugar para se encontar a paz!', font=('Times New Roman', 12), bg=self.cor2,
                      fg=self.cor5)
        log3.pack()

    def widgets_frame1(self):
        self.fundo = PhotoImage(file="f1_1.png")  # Imagem
        self.img1 = Label(self.frame1,  # local onde vai aparecer o arquivo
                          image=self.fundo,
                          bd=0)
        self.img1.place(relx=0, rely=0.0, relwidth=1, relheight=0.65)

    
    def widgets_frame2(self): #Botões
        #Configuração dos botões
        self.btn_entrar = Button(self.frame2, text='Entrar', bg=self.cor1, activebackground=self.cor1, font=('helvetica', 15),
                                 fg=self.cor2, activeforeground=self.cor2, command=self.entrar)

        self.btn_entrar.place( #Medida do botão
            relx=0, #Onde começa horizontal
            rely=0,  #Onde começa vertical
            relwidth=0.48, #Largura
            relheight=0.8) #Altura

        self.btn_cadastrar = Button(
            self.frame2, #Onde está localizado
            text='Criar conta', #Texto
            bg=self.cor1, #Cor do botão
            activebackground=self.cor1, #Botão continua com a mesma cor quando aperta
            font=('Helvetica', 15), #Fonte e Tamanho
            fg=self.cor2, #Cor da fonte
            activeforeground=self.cor5,
            command=self.cadastrar) #Comando do botão

        self.btn_cadastrar.place(relx=0.50, rely=0, relwidth=0.50, relheight=0.8)

# Entrar em outra janela

    def entrar(self): #Comando btn
        self.hide() #Esconder janela
        self.subFrame = Login(self) #Janela que irá abrir

    def cadastrar(self): #Comando btn
        self.hide() #Esconder janela
        self.subFrame = Cadastro(self) #Janela que irá abrir

    def confirmar(self): #Comando btn
        self.hide() #Esconder janela
        self.subFrame = Menu(self) #Janela que irá abrir

    def clicar1(self): #Comando btn
        self.hide() #Esconder janela
        self.subFrame = Reflexao(self) #Janela que irá abrir

    def clicar2(self): #Comando btn
        self.hide() #Esconder janela
        self.subFrame = Motivacao(self) #Janela que irá abrir

    def clicar3(self): #Comando btn
        self.hide() #Esconder janela
        self.subFrame = Informacao(self) #Janela que irá abrir

    def fechar(self): #Comando btn
        self.root.destroy() #Fechar janela

    def hide(self): #Esconder a root
        self.root.withdraw()

    def show(self): #Mostrar a outra janela
        self.root.update()
        self.root.deiconify()

## programa principal ##
root = Tk()
App()