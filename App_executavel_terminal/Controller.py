import sqlite3
import emoji


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
            self.endereco = input('Endereço:')
            cursor.execute("""insert into cliente (nome, telefone, endereco) values (?, ?, ?);""", (self.nome, self.telefone, self.endereco))
            con.commit()
            con.close()
            return print(emoji.emojize('Cadastro feito com sucesso ! :sunglasses:', use_aliases=True))
        except:
            return print(emoji.emojize('Erro no Cadastro :tired_face:', use_aliases=True))

    def select_usuario(self):
        con = sqlite3.connect('pizza.db')
        cursor = con.cursor()
        cursor.execute("""select * from cliente""")
        for linha in cursor.fetchall():
            print(linha)
        cursor.close()

