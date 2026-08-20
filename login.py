from pathlib import Path
import usuario

ARQUIVO = Path(__file__).parent / 'contas.txt'


def login():

    print('=' * 30)
    print('MENU DE LOGIN'.center(30))
    print('=' * 30)

    tentativas = 0

    while tentativas < 3:

        nome = input('Nome: ')
        senha = input('Senha: ')

        encontrado = False

        with open(ARQUIVO, 'r', encoding='utf-8') as arquivo:

            for linha in arquivo:

                if not linha.strip():
                    continue

                dados = linha.strip().split(';')

                nome_arquivo = dados[0]
                cpf_arquivo = dados[1]
                senha_arquivo = dados[2]
                saldo = float(dados[3])

                if nome == nome_arquivo and senha == senha_arquivo:

                    encontrado = True

                    print('\033[32mLogin bem-sucedido!\033[m')

                    usuario.menu_usuario(
                        nome,
                        cpf_arquivo,
                        saldo
                    )

                    return

        if not encontrado:

            tentativas += 1

            print(
                f'\033[31mLogin inválido!\033[m '
                f'(Tentativa = {tentativas})'
            )

            if tentativas == 3:
                print('Número de tentativas excedido!')
                return