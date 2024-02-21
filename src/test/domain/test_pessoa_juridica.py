from src.main.domain.pessoa_juridica import *
from src.test.domain.conftest import cliente_pj

import pytest

class TestPessoaJuridica:

    def test_deve_criar_cliente_pj_e_deve_gerar_erro_nome_obrigatorio(self):
        nome = None
        cnpj = '00000000/0001-23'
        telefone = '3333-4444'
        inscricao_estadual = '405405405405'

        with pytest.raises(Exception) as excinfo:
            PessoaJuridica(nome, telefone, cnpj, inscricao_estadual)
        assert str(excinfo.value) == 'Não foi possível cadastrar Cliente. Nome é obrigatório! Tente novamente.'

    def test_deve_criar_cliente_pj_e_deve_gerar_erro_telefone_obrigatorio(self):
        nome = 'Empresa XPTO ltda'
        cnpj = '00000000/0001-23'
        telefone = ''
        inscricao_estadual = '405405405405'

        with pytest.raises(Exception) as excinfo:
            PessoaJuridica(nome, telefone, cnpj, inscricao_estadual)
        assert str(excinfo.value) == 'Não foi possível cadastrar Cliente. Telefone é obrigatório! Tente novamente.'

    def test_deve_criar_cliente_pj_e_deve_gerar_erro_cnpj_obrigatorio(self):
        nome = 'Empresa XPTO ltda'
        cnpj = None
        telefone = '3333-4444'
        inscricao_estadual = '405405405405'

        with pytest.raises(Exception) as excinfo:
            PessoaJuridica(nome, telefone, cnpj, inscricao_estadual)
        assert str(excinfo.value) == 'Não foi possível cadastrar Cliente PJ. CNPJ é obrigatório! Tente novamente.'

    def test_deve_criar_cliente_pj_e_deve_gerar_erro_inscricao_estadual_obrigatorio(self):
        nome = 'Empresa XPTO ltda'
        cnpj = '00000000/0001-23'
        telefone = '3333-4444'
        inscricao_estadual = ''

        with pytest.raises(Exception) as excinfo:
            PessoaJuridica(nome, telefone, cnpj, inscricao_estadual)
        assert str(excinfo.value) == 'Não foi possível cadastrar Cliente PJ. Inscrição Estadual é obrigatório! Tente novamente.'

    def test_deve_criar_cliente_pj_e_deve_gerar_erro_comparar_com_outro_cliente_pj(self):
        nome_cliente_1 = 'Empresa XPTO ltda'
        cnpj_cliente_1 = '00000000/0001-23'
        telefone_cliente_1 = '4444-6666'
        inscricao_estadual_cliente_1 = '1234565555555555'
        pessoa_juridica_1 = PessoaJuridica(nome_cliente_1, telefone_cliente_1, cnpj_cliente_1, inscricao_estadual_cliente_1)

        nome_cliente_2 = 'Empresa XPTO 2 ltda'
        cnpj_cliente_2 = '00000000/0001-24'
        telefone_cliente_2 = '4455-6677'
        inscricao_estadual_cliente_2 = '4444444443333456'
        pessoa_juridica_2 = PessoaJuridica(nome_cliente_2, telefone_cliente_2, cnpj_cliente_2, inscricao_estadual_cliente_2)

        assert pessoa_juridica_1.__eq__(pessoa_juridica_2) is False

    def test_deve_criar_cliente_pj_e_deve_comparar_cliente_pj_igual_com_sucesso(self):
        nome_cliente_1 = 'Empresa XPTO ltda'
        cnpj_cliente_1 = '00000000/0001-23'
        telefone_cliente_1 = '4444-6666'
        inscricao_estadual_cliente_1 = '1234565555555555'
        pessoa_juridica_1 = PessoaJuridica(nome_cliente_1, telefone_cliente_1, cnpj_cliente_1, inscricao_estadual_cliente_1)

        pessoa_juridica_2 = pessoa_juridica_1

        assert pessoa_juridica_1.__eq__(pessoa_juridica_2) is True

    def test_deve_imprimir_dados_cliente_pj_com_sucesso(self, emprestimo_pf):
        cliente_pj().__str__()
        
        assert True