from src.main.domain.pessoa import *

class PessoaJuridica(Pessoa):
    
    def __init__(self, nome, telefone, cnpj, inscricao_estadual):
        super().__init__(nome, telefone)
        self.__cnpj = cnpj
        self.__inscricao_estadual = inscricao_estadual

    def _aplicar_taxa_juros(self) -> int:
        return 5

    def _validar_cliente(self) -> bool:
        if super().get_nome() is None or super().get_nome() == '':
            print('Não foi possível cadastrar Cliente. Nome é obrigatório! Tente novamente.')
            return False

        if super().get_telefone() is None or super().get_telefone() == '':
            print('Não foi possível cadastrar Cliente. Telefone é obrigatório! Tente novamente.')
            return False
        
        if self.__cnpj is None or self.__cnpj == '':
            print('Não foi possível cadastrar Cliente. CNPJ é obrigatório! Tente novamente.')
            return False

        if self.__inscricao_estadual is None or self.__inscricao_estadual == '':
            print('Não foi possível cadastrar Cliente. Inscrição Estadual é obrigatório! Tente novamente.')
            return False

    def __eq__(self, other):
        return self.__id == other.__id and self.__cnpj == other.__cnpj

    def __str__(self) -> str:
        return super().__str__() + f'\nCNPJ: {self.__cnpj} \nIncrição Estadual: {self.__inscricao_estadual}'
