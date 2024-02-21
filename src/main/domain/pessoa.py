from abc import ABC, abstractmethod 
import uuid as id

class Pessoa(ABC):

    def __init__(self, nome, telefone):
        self.__validar_cliente(nome, telefone)
        self.__id = id.uuid4()
        self._nome = nome
        self._telefone = telefone

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self._nome

    def get_telefone(self):
        return self._telefone

    @abstractmethod
    def _aplicar_taxa_juros(self):
        pass

    def __validar_cliente(self, nome, telefone):
        if nome is None or nome == '':
            raise Exception('Não foi possível cadastrar Cliente. Nome é obrigatório! Tente novamente.')

        if telefone is None or telefone == '':
            raise Exception('Não foi possível cadastrar Cliente. Telefone é obrigatório! Tente novamente.')
        
    def __str__(self) -> str:
        return f'Dados Cliente: \n\nId: {self.__id} \nNome: {self._nome} \nTelefone: {self._telefone}'