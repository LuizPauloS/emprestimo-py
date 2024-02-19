from domain.emprestimo import *
from domain.pessoa import *


def main():
    continuar = True
    emprestimo = None
    cliente = None
    lista_emprestimos = []

    while continuar:

        print(('-' * 21) + ' MENU ' + ('-' * 21))
        print('[1] Cadastrar Cliente')
        print('[2] Cadastrar Novo Empréstimo')
        print('[3] Imprimir Dados Empréstimo')
        print('[4] Realizar Pagamento')
        print('[5] Imprimir Valor Já Pago')
        print('[6] Verificar Empréstimo Quitado')
        print('[7] Sair')
        print('-' * 48)
        opcao = int(input('Informe a opção escolhida: '))

        match opcao:
            case 1: # Cadastrar Cliente
                print('-' * 48)
                print('Dados do Cliente')
                nome = str(input('Informe o Nome: '))
                telefone = str(input('Informe o Telefone: '))
                cpf = str(input('Informe o CPF: '))
                cliente = Pessoa(nome, telefone, cpf)

            case 2: # Cadastrar Novo Empréstimo
                print('-' * 48)
                valor_emprestimo = float(input('Informe o Valor do Empréstimo: R$ '))
                numeroParcelas = int(input('Informe o Prazo do Empréstimo: '))
                numeroParcelasPagas = int(input('Informe a Quantidade de Parcelas Pagas do Empréstimo: '))

                print(('-' * 9) + ' Tipo de Empréstimo ' + ('-' * 9))
                print('[1] - PESSOAL')
                print('[2] - ROTATIVO')
                print('[3] - CONSIGNADO')
                print('-' * 48)
                tipoEmprestimo = int(input('Selecione o Tipo de Empréstimo: '))

                if cliente is None:
                    print('Não foi possível Cadastrar o Empréstimo. Cliente é obrigatório! Tente novamente.')
                    continue

                emprestimo = Emprestimo(valor_emprestimo, numeroParcelas, numeroParcelasPagas, cliente, tipoEmprestimo)
                lista_emprestimos.append(emprestimo)
                print(lista_emprestimos)

            case 3: #Imprimir Dados Empréstimo')
                if emprestimo is not None:
                    print('-' * 48)
                    print(emprestimo.__str__())
                else:
                    print('Nenhum Empréstimo cadastrado até o momento! Tente novamente.')
                
            case 4: # Realizar Pagamento
                if emprestimo is not None:
                    print('-' * 48)
                    quantidadeParcelasPagamento = int(input('Informe a quantidade de parcelas que deseja realizar pagamento: '))
                    if quantidadeParcelasPagamento > 0:
                        emprestimo.realizar_pagamento(quantidadeParcelasPagamento)
                    else:
                        print('Pagamento Não Realizado. É necessário informar um valor maior que zero! Tente novamente.')
                else:
                    print('Nenhum Empréstimo cadastrado até o momento! Tente novamente.')

            case 5: # Imprimir Valor Já Pago
                if emprestimo is not None:
                    print('-' * 48)
                    emprestimo.imprimir_valor_pago()
                else:
                    print('Nenhum Empréstimo cadastrado até o momento! Tente novamente.')
            
            case 6: # Verificar Empréstimo Quitado
                if emprestimo is not None:
                    print('Situação do Empréstimo: ' + ('Quitado' if emprestimo.verificar_emprestimo_quitado() else 'Em Aberto'))
                    if not emprestimo.verificar_emprestimo_quitado():
                        emprestimo.imprimir_valor_restante_quitacao()
                else:
                    print('Nenhum Empréstimo cadastrado até o momento! Tente novamente.')
            
            case 7: # Sair
                continuar = False
                print('Encerrando Sistema de Empréstimos.')
            
            case _:
                print('Opção Selecionada é Inválida! Tente novamente.')

main()
