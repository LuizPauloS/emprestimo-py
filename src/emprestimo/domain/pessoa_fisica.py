from domain.pessoa import *

class PessoaFisica(Pessoa):

    def __init__(self, nome, telefone, cpf, titulo_eleitor):
        super().__init__(nome, telefone)
        self.__cpf = cpf
        self.__titulo_eleitor = titulo_eleitor

    def _valor_percentual_taxa_juros(self) -> int:
        return 10

    def _validar_cliente(self) -> bool:
        return True

    def __str__(self) -> str:
        return super().__str__() + f'\nCPF: {self.__cpf} \nTitulo Eleitor: {self.__titulo_eleitor}'
