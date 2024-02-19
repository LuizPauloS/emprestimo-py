from domain.tipo_emprestimo import * 

class Emprestimo:

    def __init__(self, valor_emprestimo, numero_parcelas, numero_parcelas_pagas, pessoa, tipo_emprestimo):
        self.__valor_emprestimo = valor_emprestimo
        self.__numero_parcelas = numero_parcelas
        self.__numero_parcelas_pagas = numero_parcelas_pagas
        self.__pessoa = pessoa
        self.__tipo_emprestimo = TipoEmprestimo(tipo_emprestimo)

    def get_valor_emprestimo(self):
        return self.__valor_emprestimo

    def get_numero_parcelas(self):
        return self.__numero_parcelas
    
    def get_numero_parcelas_pagas(self):
        return self.__numero_parcelas_pagas

    def get_pessoa(self):
        return self.__pessoa
    
    def get_tipo_emprestimo(self):
        return self.__tipo_emprestimo.name

    def realizar_pagamento(self, numero_parcelas_pagamento):
        numero_parcelas_restantes = self.__numero_parcelas - self.__numero_parcelas_pagas
        if numero_parcelas_pagamento > 0 and not self.verificar_emprestimo_quitado() and numero_parcelas_pagamento <= numero_parcelas_restantes and self.__numero_parcelas_pagas <= self.__numero_parcelas:
            self.__numero_parcelas_pagas += numero_parcelas_pagamento
            print(f'Pagamento de {numero_parcelas_pagamento} parcelas realizado com sucesso.')
        elif numero_parcelas_pagamento > 0 and self.verificar_emprestimo_quitado():
            print(f'Não foi possível realizar o pagamento de {numero_parcelas_pagamento} parcelas. Empréstimo encontra-se Quitado!')
        elif numero_parcelas_pagamento <= 0:
            print(f'Não foi possível realizar o pagamento de {numero_parcelas_pagamento} parcelas. Valor deve ser maior que zero!')
        else:
            print(f'Não foi possível realizar o pagamento de {numero_parcelas_pagamento} parcelas, pois faltam {numero_parcelas_restantes} parcelas para quitação do Empréstimo.')

    def verificar_emprestimo_quitado(self):
        return (self.__numero_parcelas - self.__numero_parcelas_pagas) == 0

    def imprimir_valor_parcela(self):
        print(f'Valor Parcela: R$ {(self.__valor_emprestimo / self.__numero_parcelas):.2f}')

    def imprimir_valor_pago(self):
        print(f'Valor Já Pago Empréstimo: R$ {((self.__valor_emprestimo / self.__numero_parcelas) * self.__numero_parcelas_pagas):.2f}')

    def imprimir_valor_restante_quitacao(self):
        print(f'Valor Restante Para Quitação: R$ {self.__valor_emprestimo - ((self.__valor_emprestimo / self.__numero_parcelas) * self.__numero_parcelas_pagas):.2f}')

    def __str__(self) -> str:
        return f'Dados Empréstimo: \nValor: R$ {self.__valor_emprestimo} \nPrazo: {self.__numero_parcelas} \nParcelas Pagas: {self.__numero_parcelas_pagas} \nTipo Empréstimo: {self.__tipo_emprestimo.name} \n\n{self.__pessoa.__str__()}'
