class Pessoa:

    def __init__(self, nome, telefone, cpf):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf

    def imprimir_dados_pessoa(self):
        print(f'Nome: {self.nome}\n'
              f'CPF: {self.cpf}\n'
              f'Telefone: {self.telefone}')