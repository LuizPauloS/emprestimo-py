from src.main.domain.pessoa_fisica import *

import pytest

class TestPessoaFisica:

    def test_deve_criar_cliente_pf_e_deve_gerar_erro_nome_obrigatorio(self):
        nome = ''
        cpf = '123.456.789-10'
        telefone = '3333-4444'
        titulo_eleitor = '55555'

        with pytest.raises(Exception) as excinfo:
            PessoaFisica(nome, telefone, cpf, titulo_eleitor)
        assert str(excinfo.value) == 'Não foi possível cadastrar Cliente. Nome é obrigatório! Tente novamente.'

    def test_deve_criar_cliente_pf_e_deve_gerar_erro_telefone_obrigatorio(self):
        nome = 'Joao'
        cpf = '123.456.789-10'
        telefone = None
        titulo_eleitor = '55555'

        with pytest.raises(Exception) as excinfo:
            PessoaFisica(nome, telefone, cpf, titulo_eleitor)
        assert str(excinfo.value) == 'Não foi possível cadastrar Cliente. Telefone é obrigatório! Tente novamente.'

    def test_deve_criar_cliente_pf_e_deve_gerar_erro_cpf_obrigatorio(self):
        nome = 'Joseph'
        cpf = ''
        telefone = '3333-4444'
        titulo_eleitor = '55555'

        with pytest.raises(Exception) as excinfo:
            PessoaFisica(nome, telefone, cpf, titulo_eleitor)
        assert str(excinfo.value) == 'Não foi possível cadastrar Cliente PF. CPF é obrigatório! Tente novamente.'

    def test_deve_criar_cliente_pf_e_deve_gerar_erro_titulo_eleitor_obrigatorio(self):
        nome = 'Maria'
        cpf = '123.456.789-10'
        telefone = '4444-6666'
        titulo_eleitor = None

        with pytest.raises(Exception) as excinfo:
            PessoaFisica(nome, telefone, cpf, titulo_eleitor)
        assert str(excinfo.value) == 'Não foi possível cadastrar Cliente PF. Título de Eleitor é obrigatório! Tente novamente.'

    def test_deve_criar_cliente_pf_e_deve_gerar_erro_comparar_com_outro_cliente_pf(self):
        nome_cliente_1 = 'Maria'
        cpf_cliente_1 = '123.456.789-10'
        telefone_cliente_1 = '4444-6666'
        titulo_eleitor_cliente_1 = '123456'
        pessoa_fisica_1 = PessoaFisica(nome_cliente_1, telefone_cliente_1, cpf_cliente_1, titulo_eleitor_cliente_1)

        nome_cliente_2 = 'Jose'
        cpf_cliente_2 = '100.456.789-00'
        telefone_cliente_2 = '4455-6677'
        titulo_eleitor_cliente_2 = '3333456'
        pessoa_fisica_2 = PessoaFisica(nome_cliente_2, telefone_cliente_2, cpf_cliente_2, titulo_eleitor_cliente_2)

        assert pessoa_fisica_1.__eq__(pessoa_fisica_2) is False

    def test_deve_criar_cliente_pf_e_deve_comparar_cliente_pf_igual_com_sucesso(self):
        nome_cliente_1 = 'Maria'
        cpf_cliente_1 = '123.456.789-10'
        telefone_cliente_1 = '4444-6666'
        titulo_eleitor_cliente_1 = '123456'
        pessoa_fisica_1 = PessoaFisica(nome_cliente_1, telefone_cliente_1, cpf_cliente_1, titulo_eleitor_cliente_1)

        pessoa_fisica_2 = pessoa_fisica_1

        assert pessoa_fisica_1.__eq__(pessoa_fisica_2) is True