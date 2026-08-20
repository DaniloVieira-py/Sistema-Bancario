from pathlib import Path

ARQUIVO = Path(__file__).parent / 'contas.txt'


def transferencia(cpf_remetente, saldo):

    cpf_destino = input('Digite o CPF do destinatário: ').strip()

    contas = []

    with open(ARQUIVO, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:

            if not linha.strip():
                continue

            dados = linha.strip().split(';')

            if len(dados) < 4:
                continue

            contas.append(dados)

    remetente = None
    destinatario = None

    # Procurar as duas contas
    for conta in contas:

        cpf_conta = conta[1].strip()

        if cpf_conta == cpf_remetente.strip():
            remetente = conta

        if cpf_conta == cpf_destino:
            destinatario = conta

    # Verificar remetente
    if remetente is None:
        print('Conta do remetente não encontrada.')
        return saldo

    # Verificar destinatário
    if destinatario is None:
        print('Usuário não encontrado.')
        return saldo

    # Impedir transferência para a própria conta
    if cpf_destino == cpf_remetente.strip():
        print('Você não pode transferir para sua própria conta.')
        return saldo

    print(f'Usuário encontrado: {destinatario[0]}')

    # Valor da transferência
    try:
        valor = float(input('Qual o valor da transferência: R$ '))
    except ValueError:
        print('Digite um valor válido.')
        return saldo

    if valor <= 0:
        print('O valor deve ser maior que zero.')
        return saldo

    if valor > saldo:
        print('Transferência incompleta, saldo insuficiente.')
        return saldo

    # Mini PIX
    print()
    print('=' * 35)
    print('           PAGAMENTO PIX')
    print('=' * 35)
    print(f'Destinatário: {destinatario[0]}')
    print(f'CPF:          {destinatario[1]}')
    print(f'Valor:        R$ {valor:.2f}')
    print('-' * 35)
    print(f'Seu saldo:    R$ {saldo:.2f}')
    print(f'Após PIX:     R$ {saldo - valor:.2f}')
    print('=' * 35)

    # Confirmação
    while True:

        opcao = input('Confirmar transferência? [S/N]: ').lower()

        if opcao == 's':

            # Retira do remetente
            saldo -= valor

            # Adiciona ao destinatário
            saldo_destino = float(destinatario[3])
            saldo_destino += valor

            # Atualiza os dados
            remetente[3] = str(saldo)
            destinatario[3] = str(saldo_destino)

            # Salva tudo novamente
            with open(ARQUIVO, 'w', encoding='utf-8') as arquivo:

                for conta in contas:
                    arquivo.write(';'.join(conta) + '\n')

            print()
            print('Transferência concluída com sucesso!')

            return saldo

        elif opcao == 'n':

            print('Transferência cancelada.')
            return saldo

        else:

            print('Resposta incorreta. Digite S ou N.')