import uuid as id

class Pessoa:

    def __init__(self, nome, telefone, cpf):
        self.__id = id.uuid4()
        self._nome = nome
        self._telefone = telefone
        self._cpf = cpf

    @property
    def get_nome(self):
        return self.__nome

    @property
    def get_cpf(self):
        return self.__cpf
    
    @property
    def get_telefone(self):
        return self.__telefone

    def __str__(self) -> str:
        return f'Dados Cliente: \n\nId: {self.__id} \nNome: {self._nome} \nCPF: {self._cpf} \nTelefone: {self._telefone}'