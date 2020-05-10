from time import sleep
from App_executavel_terminal.Controller import Usuario
class Main(Usuario):
        print('\033[31m****' * 100)
        titulo = 'Seja Bem vindo ao seu APP rapido byPiZzA'
        print(titulo.center(150, '*'))
        print('\033[31m****' * 100)
        while True:
            print('\n[ 1 ] Cadastrar cliente'
                  '\n[ 2 ] Consultar Cliente'
                  '\n[ 3 ] Alterar Cliente'
                  '\n[ 4 ] Cadastrar Pedidos'
                  '\n[ 5 ] Consultar Pedidos'
                  '\n[ 6 ] Sair Do Progama')
            opcao = int(input('Qual sua opção:'))
            sleep(0)

            if opcao == 1:
                metodo = Usuario
                metodo.insercao(metodo)

            if opcao == 2:
                print('Consulta Dos Cliente')
                all_selecao = Usuario
                all_selecao.select_usuario(all_selecao)
