from domain.tipo_emprestimo import *
import uuid as id

class Emprestimo:

    def __init__(self, valor_emprestimo, numero_parcelas, numero_parcelas_pagas, pessoa, tipo_emprestimo):
        self.__id = id.uuid4()
        self.__valor_emprestimo = valor_emprestimo
        self.__numero_parcelas = numero_parcelas
        self.__numero_parcelas_pagas = numero_parcelas_pagas
        self.__cliente = pessoa
        self.__tipo_emprestimo = TipoEmprestimo(tipo_emprestimo)
        self.__aplicar_taxa_juros()

    def get_id(self) -> str:
        return self.__id

    def get_valor_emprestimo(self) -> float:
        return self.__valor_emprestimo

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

    def __aplicar_taxa_juros(self):
        taxa = 2.5
        if self.__numero_parcelas > 5 and taxa > 0:
            self.__valor_emprestimo += self.__valor_emprestimo * (taxa / 100)

    def _validar_emprestimo(self):
        if self.__cliente is None:
            print('Não foi possível cadastrar o Empréstimo. Cliente é obrigatório! Tente novamente.')
            return False

        if self.__valor_emprestimo is None or self.__valor_emprestimo <= 0:
            print('Não foi possível cadastrar o Empréstimo. Valor deve ser maior que zero! Tente novamente.')
            return False

        if self.__numero_parcelas is None or self.__numero_parcelas <= 0:
            print('Não foi possível cadastrar o Empréstimo. Prazo deve ser maior que zero! Tente novamente.')
            return False

        if self.__tipo_emprestimo is None or self.__tipo_emprestimo == '':
            print('Não foi possível cadastrar o Empréstimo. Tipo é obrigatório! Tente novamente.')
            return False

        if self.__numero_parcelas_pagas is None or self.__numero_parcelas_pagas < 0:
            print('Não foi possível cadastrar o Empréstimo. Número de Parcelas Pagas deve ser igual ou maior que zero! Tente novamente.')
            return False
        
        return True

    def verificar_emprestimo_quitado(self):
        return (self.__numero_parcelas - self.__numero_parcelas_pagas) == 0

    def imprimir_valor_parcela(self):
        print(f'Valor Parcela: R$ {(self.__valor_emprestimo / self.__numero_parcelas):.2f}')

    def imprimir_valor_pago(self):
        print(f'Valor Já Pago Empréstimo: R$ {((self.__valor_emprestimo / self.__numero_parcelas) * self.__numero_parcelas_pagas):.2f}')

    def imprimir_valor_restante_quitacao(self):
        print(f'Valor Restante Para Quitação: R$ {self.__valor_emprestimo - ((self.__valor_emprestimo / self.__numero_parcelas) * self.__numero_parcelas_pagas):.2f}')

    def __str__(self) -> str:
        return f'Dados Empréstimo: \n\nId: {self.__id} \nValor: R$ {self.__valor_emprestimo:.2f} \nPrazo: {self.__numero_parcelas} \nParcelas Pagas: {self.__numero_parcelas_pagas} \nTipo Empréstimo: {self.__tipo_emprestimo.name} \n\n{self.__cliente.__str__()}'
