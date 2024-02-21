from src.main.domain.tipo_emprestimo import *
import uuid as id

class Emprestimo:

    def __init__(self, valor_emprestimo, numero_parcelas, numero_parcelas_pagas, pessoa, tipo_emprestimo):
        self.__validar_emprestimo(valor_emprestimo, numero_parcelas, numero_parcelas_pagas, pessoa, tipo_emprestimo)
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

    def get_numero_parcelas(self) -> int:
        return self.__numero_parcelas

    def get_numero_parcelas_pagas(self) -> int:
        return self.__numero_parcelas_pagas

    def realizar_pagamento(self, numero_parcelas_pagamento: str):
        if not isinstance(numero_parcelas_pagamento, int):
            raise Exception(f'Número de Parcelas para Pagamento inválido! Informe um número inteiro.')
        
        numero_parcelas_restantes = self.__numero_parcelas - self.__numero_parcelas_pagas
        if numero_parcelas_pagamento > 0 and not self.verificar_emprestimo_quitado() and numero_parcelas_pagamento <= numero_parcelas_restantes and self.__numero_parcelas_pagas <= self.__numero_parcelas:
            self.__numero_parcelas_pagas += numero_parcelas_pagamento
            print(f'Pagamento de {numero_parcelas_pagamento} parcelas realizado com sucesso.')
        elif numero_parcelas_pagamento > 0 and self.verificar_emprestimo_quitado():
            raise Exception(f'Não foi possível realizar o pagamento de {numero_parcelas_pagamento} parcelas. Empréstimo encontra-se Quitado!')
        elif numero_parcelas_pagamento == 0:
            raise Exception(f'Não foi possível realizar o pagamento de {numero_parcelas_pagamento} parcelas. Valor deve ser maior que zero!')
        else:
            raise Exception(f'Não foi possível realizar o pagamento de {numero_parcelas_pagamento} parcelas, pois faltam {numero_parcelas_restantes} parcelas para quitação do Empréstimo.')

    def __aplicar_taxa_juros(self):
        taxa_emprestimo = 2.5 # taxa deve ser aplicada se numero de parcelas for maior que 5
        if self.__numero_parcelas > 5 and taxa_emprestimo > 0:
            self.__valor_emprestimo += self.__valor_emprestimo * (taxa_emprestimo / 100)
    
        taxa_cliente = self.__cliente._aplicar_taxa_juros()
        if taxa_cliente > 0:
            self.__valor_emprestimo += self.__valor_emprestimo * (taxa_cliente / 100)

    def __validar_emprestimo(self, valor_emprestimo, numero_parcelas, numero_parcelas_pagas, pessoa, tipo_emprestimo):
        if pessoa is None:
            raise Exception('Não foi possível cadastrar o Empréstimo. Cliente é obrigatório! Tente novamente.')

        if valor_emprestimo is None or valor_emprestimo <= 0:
            raise Exception('Não foi possível cadastrar o Empréstimo. Valor deve ser maior que zero! Tente novamente.')

        if numero_parcelas is None or numero_parcelas <= 0:
            raise Exception('Não foi possível cadastrar o Empréstimo. Prazo deve ser maior que zero! Tente novamente.')

        if tipo_emprestimo is None or not isinstance(tipo_emprestimo, int):
            raise Exception('Não foi possível cadastrar o Empréstimo. Tipo de Empréstimo inválido! Tente novamente.')

        if numero_parcelas_pagas is None or numero_parcelas_pagas < 0:
            raise Exception('Não foi possível cadastrar o Empréstimo. Número de Parcelas Pagas deve ser igual ou maior que zero! Tente novamente.')

        if numero_parcelas_pagas > numero_parcelas:
            raise Exception('Não foi possível cadastrar o Empréstimo. Número de Parcelas Pagas não pode ser superior ao Número de Parcelas do Empréstimo! Tente novamente.')

    def __calcular_valor_parcela(self) -> float:
        return (self.__valor_emprestimo / self.__numero_parcelas)

    def verificar_emprestimo_quitado(self):
        return (self.__numero_parcelas - self.__numero_parcelas_pagas) == 0

    def imprimir_valor_parcela(self):
        print(f'Valor Parcela: R$ {self.__calcular_valor_parcela():.2f}')

    def imprimir_valor_pago(self):
        print(f'Valor Já Pago Empréstimo: R$ {((self.__valor_emprestimo / self.__numero_parcelas) * self.__numero_parcelas_pagas):.2f}')

    def imprimir_valor_restante_quitacao(self):
        print(f'Valor Restante Para Quitação: R$ {self.__valor_emprestimo - ((self.__valor_emprestimo / self.__numero_parcelas) * self.__numero_parcelas_pagas):.2f}')

    def __eq__(self, other):
        return self.__id == other.__id

    def __str__(self) -> str:
        return f'Dados Empréstimo: \n\nId: {self.__id} \nValor: R$ {self.__valor_emprestimo:.2f} \nPrazo: {self.__numero_parcelas} \nParcelas Pagas: {self.__numero_parcelas_pagas} \nTipo Empréstimo: {self.__tipo_emprestimo.name} \n\n{self.__cliente.__str__()}'
