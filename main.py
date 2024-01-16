from tkinter import ttk
from functions import *

window = Tk()


class Application(Functions):
    def __init__(self):
        self.window = window
        self.tela()
        self.frameDaTela()
        self.widgetsFrame1()
        self.tabelaClientes()
        self.criarTabelaCliente()
        self.exibirDados()
        self.menus()
        window.mainloop()

    def tela(self):
        self.window.title("Cadastro de Clientes")
        self.window.config(background='#2e3758')
        self.window.geometry("700x500")
        self.window.resizable(True, True)
        self.window.maxsize(width=900, height=700)
        self.window.minsize(width=500, height=400)

    def frameDaTela(self):
        self.frame1 = Frame(self.window,
                            background="#ededf2",
                            border=4,
                            highlightbackground="#386dbd",
                            highlightthickness=3)
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        self.frame2 = Frame(self.window,
                            background="#ededf2",
                            border=4,
                            highlightbackground="#386dbd",
                            highlightthickness=3)
        self.frame2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgetsFrame1(self):
        self.btLimpar = Button(self.frame1, text="Limpar", bg="#45b5c4", fg="white", font="Arial 8 bold",
                               command=self.limparEntries)
        self.btLimpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        self.btBuscar = Button(self.frame1, text="Buscar", bg="#45b5c4", fg="white", font="Arial 8 bold")
        self.btBuscar.place(relx=0.31, rely=0.1, relwidth=0.1, relheight=0.15)
        self.btNovo = Button(self.frame1, text="Novo", bg="#45b5c4", fg="white", font="Arial 8 bold",
                             command=self.cadastrarCliente)
        self.btNovo.place(relx=0.62, rely=0.1, relwidth=0.1, relheight=0.15)
        self.btAlterar = Button(self.frame1, text="Alterar", bg="#45b5c4", fg="white", font="Arial 8 bold",
                                command=self.editarCliente)
        self.btAlterar.place(relx=0.73, rely=0.1, relwidth=0.1, relheight=0.15)
        self.btApagar = Button(self.frame1, text="Apagar", bg="#45b5c4", fg="white", font="Arial 8 bold",
                               command=self.deletarCliente)
        self.btApagar.place(relx=0.84, rely=0.1, relwidth=0.1, relheight=0.15)

        # Criação da Label e a entrada do código
        self.lbCodigo = Label(self.frame1, text="Código", background="#ededf2", foreground="#45b5c4",
                              font="Arial 9 bold")
        self.lbCodigo.place(relx=0.05, rely=0.05)

        self.codigoEntry = Entry(self.frame1, background="#cfd5e1")
        self.codigoEntry.place(relx=0.05, rely=0.15, relwidth=0.08)

        # Criação da Label e a entrada do nome
        self.lbNome = Label(self.frame1, text="Nome", background="#ededf2", foreground="#45b5c4", font="Arial 9 bold")
        self.lbNome.place(relx=0.05, rely=0.35)

        self.nomeEntry = Entry(self.frame1, background="#cfd5e1")
        self.nomeEntry.place(relx=0.05, rely=0.45, relwidth=0.7)

        # Criação da Label e a entrada do telefone
        self.lbTelefone = Label(self.frame1, text="Telefone", background="#ededf2", foreground="#45b5c4",
                                font="Arial 9 bold")
        self.lbTelefone.place(relx=0.05, rely=0.6)

        self.telefoneEntry = Entry(self.frame1, background="#cfd5e1")
        self.telefoneEntry.place(relx=0.05, rely=0.7, relwidth=0.2)

        # Criação da Label e a entrada da cidade
        self.lbCidade = Label(self.frame1, text="Cidade", background="#ededf2", foreground="#45b5c4",
                              font="Arial 9 bold")
        self.lbCidade.place(relx=0.5, rely=0.6)

        self.cidadeEntry = Entry(self.frame1, background="#cfd5e1")
        self.cidadeEntry.place(relx=0.5, rely=0.7, relwidth=0.25)

    def tabelaClientes(self):
        style = ttk.Style(self.frame2)
        style.theme_use('clam')

        self.tabela = ttk.Treeview(self.frame2, height=3, columns=("column1", "column2", "column3", "column4"))
        self.tabela.heading("#0", text="")
        self.tabela.heading("#1", text="Cod")
        self.tabela.heading("#2", text="Nome")
        self.tabela.heading("#3", text="Telefone")
        self.tabela.heading("#4", text="Cidade")

        self.tabela.column("#0", width=1, stretch=NO)
        self.tabela.column("#1", width=50, minwidth=50)
        self.tabela.column("#2", width=200, minwidth=200)
        self.tabela.column("#3", width=125, minwidth=125)
        self.tabela.column("#4", width=125, minwidth=125)

        self.tabela.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scrollTabela = Scrollbar(self.frame2, orient="vertical", command=self.tabela.yview)

        self.tabela.config(yscrollcommand=self.scrollTabela.set)
        self.scrollTabela.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.tabela.bind("<Double-1>", self.onDoubleClick)

    def menus(self):
        menubar = Menu(self.window)
        self.window.config(menu=menubar)
        fileMenu1 = Menu(menubar, tearoff=0)
        fileMenu2 = Menu(menubar, tearoff=0)

        def quit():
            self.window.destroy()

        menubar.add_cascade(label="Opções", menu=fileMenu1)
        menubar.add_cascade(label="Sobre", menu=fileMenu2)

        fileMenu1.add_command(label="Sair", command=quit)
        fileMenu1.add_command(label="Limpa Cliente", command=self.limparEntries)


Application()
