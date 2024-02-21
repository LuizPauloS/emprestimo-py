from src.main.domain.pessoa import *

class PessoaFisica(Pessoa):

    def __init__(self, nome, telefone, cpf, titulo_eleitor):
        super().__init__(nome, telefone)
        self.__cpf = cpf
        self.__titulo_eleitor = titulo_eleitor

    def _aplicar_taxa_juros(self) -> int:
        return 10

    def _validar_cliente(self) -> bool:
        if super().get_nome() is None or super().get_nome() == '':
            print('Não foi possível cadastrar Cliente. Nome é obrigatório! Tente novamente.')
            return False

        if super().get_telefone() is None or super().get_telefone() == '':
            print('Não foi possível cadastrar Cliente. Telefone é obrigatório! Tente novamente.')
            return False
        
        if self.__cpf is None or self.__cpf == '':
            print('Não foi possível cadastrar Cliente. CPF é obrigatório! Tente novamente.')
            return False

        if self.__titulo_eleitor is None or self.__titulo_eleitor == '':
            print('Não foi possível cadastrar Cliente. Título de Eleitor é obrigatório! Tente novamente.')
            return False
        
        return True

    def __str__(self) -> str:
        return super().__str__() + f'\nCPF: {self.__cpf} \nTitulo Eleitor: {self.__titulo_eleitor}'
