import deposito
import saque
import trasferencias


def menu_usuario(nome, cpf, saldo):

    while True:
        print('\n===== MENU DO USUÁRIO =====')
        print('1 - Depositar')
        print('2 - Consultar saldo')
        print('3 - Sacar')
        print('4 - Transferências')
        print('5 - Sair')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            saldo = deposito.deposito(cpf,saldo)

        elif opcao == '2':
            print(f'Seu saldo é R$ {saldo:.2f}')

        elif opcao == '3':
            saldo = saque.saque(saldo)

        elif opcao == '4':
            saldo = trasferencias.transferencia(cpf, saldo)

        elif opcao == '5':
            print('Saindo...')
            break

        else:
            print('Opção inválida!')