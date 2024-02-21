from src.main.domain.pessoa import *

class PessoaJuridica(Pessoa):
    
    def __init__(self, nome, telefone, cnpj, inscricao_estadual):
        super().__init__(nome, telefone)
        self.__validar_cliente(cnpj, inscricao_estadual)
        self.__cnpj = cnpj
        self.__inscricao_estadual = inscricao_estadual

    def _aplicar_taxa_juros(self) -> int:
        return 5

    def __validar_cliente(self, cnpj, inscricao_estadual):
        if cnpj is None or cnpj == '':
            raise Exception('Não foi possível cadastrar Cliente PJ. CNPJ é obrigatório! Tente novamente.')

        if inscricao_estadual is None or inscricao_estadual == '':
            raise Exception('Não foi possível cadastrar Cliente PJ. Inscrição Estadual é obrigatório! Tente novamente.')

    def __eq__(self, other) -> bool:
        return (self.get_id(), self.__cnpj, type(self)) == (other.get_id(), other.__cnpj, type(other))

    def __str__(self) -> str:
        return super().__str__() + f'\nCNPJ: {self.__cnpj} \nIncrição Estadual: {self.__inscricao_estadual}'
