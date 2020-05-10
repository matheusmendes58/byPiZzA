import sqlite3


class Banco:
    con = sqlite3.connect('pizza.db')

    cursor = con.cursor()
    tabela1 = """
          create table cliente (idcliente integer not null primary key autoincrement,
                                     nome text,
                                     telefone txt, 
                                     endereco txt);"""

    tabela2 = """create table pedido (idpedido integer not null primary key autoincrement,
                 nome_pizza text,
                 valor real);"""
    cursor.execute(tabela1)
    cursor.execute(tabela2)
    con.commit()
    con.close()
