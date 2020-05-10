import sqlite3

class Usuario:
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco

    def insercao(self):
        try:
            con = sqlite3.connect('pizza.db')
            cursor = con.cursor()
            self.nome = input('Nome:')
            self.telefone = input('Telefone:')
            self.endereco = input('Endereço')
            cursor.execute("""insert into cliente (nome, telefone, endereco) values (?, ?, ?);""", (self.nome, self.telefone, self.endereco))
            con.commit()
            con.close()
            return print('Cadastro feito com sucesso !')
        except:
            return print('Erro no Cadastro')

    def select_usuario(self):
        con = sqlite3.connect('pizza.db')
        cursor = con.cursor()
        cursor.execute("""select * from cliente""")
        for linha in cursor.fetchall():
            print(linha)
        cursor.close()




