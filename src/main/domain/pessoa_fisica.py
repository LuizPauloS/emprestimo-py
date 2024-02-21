from src.main.domain.pessoa import *

class PessoaFisica(Pessoa):

    def __init__(self, nome, telefone, cpf, titulo_eleitor):
        super().__init__(nome, telefone)
        self.__validar_cliente(cpf, titulo_eleitor)
        self.__cpf = cpf
        self.__titulo_eleitor = titulo_eleitor

    def _aplicar_taxa_juros(self) -> int:
        return 10

    def __validar_cliente(self, cpf, titulo_eleitor):
        if cpf is None or cpf == '':
            raise Exception('Não foi possível cadastrar Cliente PF. CPF é obrigatório! Tente novamente.')

        if titulo_eleitor is None or titulo_eleitor == '':
            raise Exception('Não foi possível cadastrar Cliente PF. Título de Eleitor é obrigatório! Tente novamente.')

    def __eq__(self, other) -> bool:
        return (self.get_id(), self.__cpf, type(self)) == (other.get_id(), other.__cpf, type(other))

    def __str__(self) -> str:
        return super().__str__() + f'\nCPF: {self.__cpf} \nTitulo Eleitor: {self.__titulo_eleitor}'
