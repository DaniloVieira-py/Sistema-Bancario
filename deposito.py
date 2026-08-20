from pathlib import Path

ARQUIVO = Path(__file__).parent / 'contas.txt'


def deposito(cpf, saldo):

    valor = int(input('Qual o Valor Do Deposito?: '))

    if valor <= 0:
        print('Digite um valor maior que zero.')
        return saldo

    saldo += valor

    contas = []

    with open(ARQUIVO, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:

            if not linha.strip():
                continue

            dados = linha.strip().split(';')

            if len(dados) < 4:
                continue

            if dados[1] == cpf:
                dados[3] = str(saldo)

            contas.append(dados)

    with open(ARQUIVO, 'w', encoding='utf-8') as arquivo:
        for conta in contas:
            arquivo.write(';'.join(conta) + '\n')

    print('Valor Depositado Com Sucesso!!')

    return saldo