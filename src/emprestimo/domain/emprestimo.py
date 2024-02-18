from domain.tipo_emprestimo import * 

class Emprestimo:

    def __init__(self, valorEmprestimo, numeroParcelas, numeroParcelasPagas, pessoa, tipoEmprestimo):
        self.valorEmprestimo = valorEmprestimo
        self.numeroParcelas = numeroParcelas
        self.numeroParcelasPagas = numeroParcelasPagas
        self.pessoa = pessoa
        self.tipoEmprestimo = TipoEmprestimo(tipoEmprestimo)

    def realizar_pagamento(self, numeroParcelasPagamento):
        numeroParcelasRestantes = self.numeroParcelas - self.numeroParcelasPagas
        if numeroParcelasPagamento > 0 and not self.emprestimo_quitado() and numeroParcelasPagamento <= numeroParcelasRestantes and self.numeroParcelasPagas <= self.numeroParcelas:
            self.numeroParcelasPagas += numeroParcelasPagamento
            print(f'Pagamento de {numeroParcelasPagamento} parcelas realizado com sucesso.')
        elif numeroParcelasPagamento > 0 and self.emprestimo_quitado():
            print(f'Não foi possível realizar o pagamento de {numeroParcelasPagamento} parcelas. Empréstimo encontra-se Quitado!')
        elif numeroParcelasPagamento <= 0:
            print(f'Não foi possível realizar o pagamento de {numeroParcelasPagamento} parcelas. Valor deve ser maior que zero!')
        else:
            print(f'Não foi possível realizar o pagamento de {numeroParcelasPagamento} parcelas, pois faltam {numeroParcelasRestantes} parcelas para quitação do Empréstimo.')

    def emprestimo_quitado(self):
        return self.numeroParcelas - self.numeroParcelasPagas == 0

    def imprimir_dados_emprestimo(self):
        print('-' * 48)
        print(f'Dados Empréstimo:\n'
              f'Valor: R$ {self.valorEmprestimo}\n'
              f'Prazo: {self.numeroParcelas}\n'
              f'Parcelas Pagas: {self.numeroParcelasPagas}\n'
              f'Tipo Empréstimo: {self.tipoEmprestimo.name}\n')
        print(f'Dados Cliente:')
        self.pessoa.imprimir_dados_pessoa()

    def imprimir_valor_parcela(self):
        print(f'Valor Parcela: R$ {(self.valorEmprestimo / self.numeroParcelas):.2f}')

    def imprimir_valor_pago(self):
        print(f'Valor Pago: R$ {((self.valorEmprestimo / self.numeroParcelas) * self.numeroParcelasPagas):.2f}')

    def imprimir_valor_restante_quitacao(self):
        print(f'Valor Restante: R$ {self.valorEmprestimo - ((self.valorEmprestimo / self.numeroParcelas) * self.numeroParcelasPagas):.2f}')
