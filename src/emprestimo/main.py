from domain.emprestimo import *
from domain.pessoa import *


def main():
    print('-' * 48)
    print('Dados do Cliente')
    nome = str(input('Informe o Nome: '))
    telefone = str(input('Informe o Telefone: '))
    cpf = str(input('Informe o CPF: '))
    pessoa = Pessoa(nome, telefone, cpf)

    valor_emprestimo = float(input('Informe o Valor do Empréstimo: R$ '))
    numeroParcelas = int(input('Informe o Prazo do Empréstimo: '))
    numeroParcelasPagas = int(input('Informe a Quantidade de Parcelas Pagas do Empréstimo: '))
    emprestimo = Emprestimo(valor_emprestimo, numeroParcelas, numeroParcelasPagas, pessoa)

    emprestimo.imprimir_dados_emprestimo()
    emprestimo.realizar_pagamento(3)
    emprestimo.realizar_pagamento(3)
    emprestimo.realizar_pagamento(0)
    print(f'Situação do Empréstimo: {"Quitado" if emprestimo.emprestimo_quitado() else "Em Aberto"}')
    emprestimo.imprimir_valor_parcela()
    emprestimo.imprimir_valor_pago()
    emprestimo.imprimir_valor_restante_quitacao()

main()
