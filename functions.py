from tkinter import *
import sqlite3


class Functions:
    def variaveis(self):
        self.codigo = self.codigoEntry.get()
        self.nome = self.nomeEntry.get()
        self.telefone = self.telefoneEntry.get()
        self.cidade = self.cidadeEntry.get()

    def limparEntries(self):
        self.codigoEntry.delete(0, END)
        self.nomeEntry.delete(0, END)
        self.telefoneEntry.delete(0, END)
        self.cidadeEntry.delete(0, END)

    def conectaBancoDeDados(self):
        self.connection = sqlite3.connect("clientes.bd")
        self.cursor = self.connection.cursor()
        print("\033[32mConectou com o Banco De Dados!\033[m")

    def desconectaBancoDeDados(self):
        self.connection.close()
        print("\033[32mDesconectou com o Banco De Dados!\033[m")

    def criarTabelaCliente(self):
        try:
            self.conectaBancoDeDados()
        except Exception as Error:
            print(f'\033[31mFalha na conexão com o Banco de Dados! {Error}\033[m')
        else:
            self.cursor.execute("""  
                        CREATE TABLE IF NOT EXISTS clientes (                
                        cod INTEGER PRIMARY KEY AUTOINCREMENT,                
                        nome_cliente CHAR(50) NOT NULL,                
                        telefone CHAR(16),                
                        cidade CHAR(40));        
            """)
            self.connection.commit()
            print("\033[32mTabela Cliente criada com sucesso!\033[m")
            self.desconectaBancoDeDados()

    def cadastrarCliente(self):
        self.variaveis()
        self.conectaBancoDeDados()

        self.cursor.execute("""
        INSERT INTO clientes (nome_cliente, telefone, cidade) VALUES (?, ?, ?)
        """, (self.nome, self.telefone, self.cidade))
        self.connection.commit()
        self.desconectaBancoDeDados()
        self.exibirDados()
        self.limparEntries()

    def exibirDados(self):
        self.tabela.delete(*self.tabela.get_children())
        self.conectaBancoDeDados()
        dados = self.cursor.execute("""
        SELECT cod, nome_cliente, telefone, cidade FROM clientes;
        """)
        for dado in dados:
            self.tabela.insert("", END, values=dado)
        self.desconectaBancoDeDados()

    def onDoubleClick(self, event):
        self.limparEntries()
        for n in self.tabela.selection():
            column1, column2, column3, column4 = self.tabela.item(n, "values")
            self.codigoEntry.insert(END, column1)
            self.nomeEntry.insert(END, column2)
            self.telefoneEntry.insert(END, column3)
            self.cidadeEntry.insert(END, column4)

    def deletarCliente(self):
        self.variaveis()
        self.conectaBancoDeDados()
        self.cursor.execute("""DELETE FROM clientes WHERE cod = ?;""", [self.codigo])
        self.connection.commit()
        self.desconectaBancoDeDados()
        self.limparEntries()
        self.exibirDados()

    def editarCliente(self):
        self.variaveis()
        self.conectaBancoDeDados()
        self.cursor.execute("""UPDATE clientes SET nome_cliente = ?, telefone = ?, cidade = ? WHERE cod = ?;""",
                            (self.nome, self.telefone, self.cidade, self.codigo))
        self.connection.commit()
        self.desconectaBancoDeDados()
        self.exibirDados()
        self.limparEntries()
