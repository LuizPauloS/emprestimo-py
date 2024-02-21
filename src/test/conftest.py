import pytest

from src.main.domain.emprestimo import *
from src.main.domain.pessoa_fisica import *
from src.main.domain.pessoa_juridica import *

@pytest.fixture()
def emprestimo_pessoa_fisica() -> Emprestimo:
    valor_emprestimo = 10000
    numero_parcelas = 10
    numero_parcelas_pagas = 0
    tipo_emprestimo = TipoEmprestimo.PESSOAL

    nome = 'Luiz'
    cpf = '123.456.789-10'
    telefone = '3333-4444'
    titulo_eleitor = '55555'

    cliente = PessoaFisica(nome, telefone, cpf, titulo_eleitor)
    emprestimo = Emprestimo(valor_emprestimo, numero_parcelas, numero_parcelas_pagas, cliente, tipo_emprestimo)
    return emprestimo

@pytest.fixture()
def emprestimo_pessoa_juridica() -> Emprestimo:
    valor_emprestimo = 150000000
    numero_parcelas = 24
    numero_parcelas_pagas = 0
    tipo_emprestimo = TipoEmprestimo.ROTATIVO

    nome = 'Empresa XPTO ltda'
    cnpj = '00000000/0001-23'
    telefone = '3333-4444'
    inscricao_estadual = '405405405405'

    cliente = PessoaJuridica(nome, telefone, cnpj, inscricao_estadual)
    emprestimo = Emprestimo(valor_emprestimo, numero_parcelas, numero_parcelas_pagas, cliente, tipo_emprestimo)
    return emprestimo