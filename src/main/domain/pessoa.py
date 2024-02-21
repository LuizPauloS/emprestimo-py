from abc import ABC, abstractmethod 
import uuid as id

class Pessoa(ABC):

    def __init__(self, nome, telefone):
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

    @abstractmethod
    def _validar_cliente(self) -> bool:
        pass
        
    def __str__(self) -> str:
        return f'Dados Cliente: \n\nId: {self.__id} \nNome: {self._nome} \nTelefone: {self._telefone}'