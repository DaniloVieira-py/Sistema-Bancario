def saque(saldo):
    while True:
        valor = int(input('Quanto Deseja Sacar?:'))
        if valor > saldo:
            print(f'Valor Insuficiente Para o Saque, Voce Tem R$ {saldo},00 Disponivel.')
            continue

        else:
            print('Saque Realizado Com Sucesso!!!')
            saldo -= valor
            return saldo