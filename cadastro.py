from pathlib import Path

ARQUIVO = Path(__file__).parent / 'contas.txt'


def cadastro_usuario():

    print('=' * 30)
    print('MENU DE CADASTRO'.center(30))
    print('=' * 30)

    while True:
        nome = input('Nome: ')
        cpf = input('CPF: ')
        senha = input('Senha: ')
        saldo = 0

        if len(senha) < 8:
            print('Senha deve ter no mínimo 8 caracteres.')
            continue

        if len(cpf) != 11:
            print('CPF deve ter 11 caracteres.')
            continue

        cpf_existente = False

        # Verificar se o CPF já existe
        if ARQUIVO.exists():

            with open(ARQUIVO, 'r', encoding='utf-8') as arquivo:

                for linha in arquivo:

                    if not linha.strip():
                        continue

                    dados = linha.strip().split(';')

                    if len(dados) < 4:
                        continue

                    if dados[1] == cpf:
                        print('Usuário já existente!')
                        cpf_existente = True
                        break

        if cpf_existente:
            continue

        with open(ARQUIVO, 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{nome};{cpf};{senha};{saldo}\n')

        break

    print(f'Usuário {nome} cadastrado com sucesso!')