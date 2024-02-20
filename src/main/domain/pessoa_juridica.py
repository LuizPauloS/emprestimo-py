from src.main.domain.pessoa import *

class PessoaJuridica(Pessoa):
    
    def __init__(self, nome, telefone, cnpj, inscricao_estadual):
        super().__init__(nome, telefone)
        self.__cnpj = cnpj
        self.__inscricao_estadual = inscricao_estadual

    def _aplicar_taxa_juros(self) -> int:
        return 5

    def _validar_cliente(self) -> bool:
        return True

    def __str__(self) -> str:
        return super().__str__() + f'\nCNPJ: {self.__cnpj} \nIncrição Estadual: {self.__inscricao_estadual}'
