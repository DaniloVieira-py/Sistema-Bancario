import login
import cadastro

def menu():
    while True:
        print('-'*40)
        print('MENU BANCARIO'.center(40))
        print('-'*40)
        print('[1] - Entrar Com Usuario')
        print('[2] - Cadastrar Usuario')
        print('[3] - Sair')
        try:
            opcao = int(input('\033[33mSua Opção: \033[m'))
            if opcao == 1:
                login.login()
            elif opcao == 2:
                cadastro.cadastro_usuario()
            elif opcao == 3:
                print('Encerrando...')
                break
            else:
                print('OPCAO INCORRETA!!')
        except ValueError:
            print('USE SOMENTE NUMEROS PARA DIGITAR A OPCAO!')

menu()
