from src.main.domain.emprestimo import *
from src.main.domain.pessoa import *
from src.main.domain.pessoa_fisica import *
from src.main.domain.pessoa_juridica import *

import pytest

def cliente_pf() -> Pessoa:
    nome = 'Luiz'
    cpf = '123.456.789-10'
    telefone = '3333-4444'
    titulo_eleitor = '55555'

    return PessoaFisica(nome, telefone, cpf, titulo_eleitor)

def cliente_pj() -> Pessoa:
    nome = 'Empresa XPTO ltda'
    cnpj = '00000000/0001-23'
    telefone = '3333-4444'
    inscricao_estadual = '405405405405'

    return PessoaJuridica(nome, telefone, cnpj, inscricao_estadual)

@pytest.fixture()
def emprestimo_pf() -> Emprestimo:
    valor_emprestimo = 10000
    numero_parcelas = 10
    numero_parcelas_pagas = 0
    tipo_emprestimo = 1

    cliente = cliente_pf()
    emprestimo = Emprestimo(valor_emprestimo, numero_parcelas, numero_parcelas_pagas, cliente, tipo_emprestimo)
    return emprestimo

@pytest.fixture()
def emprestimo_pj() -> Emprestimo:
    valor_emprestimo = 150000000
    numero_parcelas = 24
    numero_parcelas_pagas = 0
    tipo_emprestimo = 2

    cliente = cliente_pj()
    return Emprestimo(valor_emprestimo, numero_parcelas, numero_parcelas_pagas, cliente, tipo_emprestimo)

# @pytest.fixture()
# def emprestimo_cliente_invalido() -> Emprestimo:
#     valor_emprestimo = 10000
#     numero_parcelas = 10
#     numero_parcelas_pagas = 0
#     tipo_emprestimo = TipoEmprestimo.PESSOAL

#     cliente = None
#     return Emprestimo(valor_emprestimo, numero_parcelas, numero_parcelas_pagas, cliente, tipo_emprestimo)