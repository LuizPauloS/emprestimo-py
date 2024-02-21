from src.main.domain.emprestimo import *
from src.test.domain.conftest import cliente_pj

import pytest

class TestEmprestimo:

    def test_deve_criar_emprestimo_pf_com_sucesso_dados_validos(self, emprestimo_pf):
        valor_original = 10000
        taxa_parcela_maior_5 = 2.5
        taxa_pessoa_fisica = 10

        valor_com_juros = valor_original + (valor_original * (taxa_parcela_maior_5 /100))
        valor_com_juros = valor_com_juros + (valor_com_juros * (taxa_pessoa_fisica /100))

        assert emprestimo_pf.get_id() is not None
        assert emprestimo_pf.get_numero_parcelas() > 5
        assert emprestimo_pf.get_valor_emprestimo() == valor_com_juros

    def test_deve_criar_emprestimo_pj_com_sucesso_dados_validos(self, emprestimo_pj):
        valor_original = 150000000
        taxa_parcela_maior_5 = 2.5
        taxa_pessoa_juridica = 5

        valor_com_juros = valor_original + (valor_original * (taxa_parcela_maior_5 /100))
        valor_com_juros = valor_com_juros + (valor_com_juros * (taxa_pessoa_juridica /100))

        assert emprestimo_pj.get_id() is not None
        assert emprestimo_pj.get_numero_parcelas() > 5
        assert emprestimo_pj.get_valor_emprestimo() == valor_com_juros

    def test_deve_realizar_pagamento_emprestimo_pf_com_sucesso(self, emprestimo_pf):
        numero_parcelas_para_pagamento = 10
        numero_parcelas_pagas_original = emprestimo_pf.get_numero_parcelas_pagas()
        emprestimo_pf.realizar_pagamento(numero_parcelas_para_pagamento)
        
        assert numero_parcelas_pagas_original == 0
        assert emprestimo_pf.get_numero_parcelas_pagas() == 10
        assert emprestimo_pf.get_numero_parcelas_pagas() == numero_parcelas_para_pagamento

    def test_deve_realizar_pagamento_emprestimo_pf_e_deve_gerar_erro_numero_parcelas_invalido(self, emprestimo_pf):
        numero_parcelas_para_pagamento = '1abc'

        with pytest.raises(Exception) as excinfo:
            emprestimo_pf.realizar_pagamento(numero_parcelas_para_pagamento)
        assert str(excinfo.value) == f'Número de Parcelas para Pagamento inválido! Informe um número inteiro.'

    def test_deve_realizar_pagamento_emprestimo_pf_e_deve_gerar_erro_emprestimo_quitado(self, emprestimo_pf):
        numero_parcelas_para_pagamento = 10

        emprestimo_pf.realizar_pagamento(numero_parcelas_para_pagamento)
        assert emprestimo_pf.verificar_emprestimo_quitado() is True

        with pytest.raises(Exception) as excinfo:
            emprestimo_pf.realizar_pagamento(numero_parcelas_para_pagamento)
        assert str(excinfo.value) == f'Não foi possível realizar o pagamento de {numero_parcelas_para_pagamento} parcelas. Empréstimo encontra-se Quitado!'

    def test_realiza_pagamento_emprestimo_pf_e_deve_gerar_erro_numero_parcelas_igual_a_zero(self, emprestimo_pf):
        numero_parcelas_para_pagamento = 0

        with pytest.raises(Exception) as excinfo:
            emprestimo_pf.realizar_pagamento(numero_parcelas_para_pagamento)
        assert str(excinfo.value) == f'Não foi possível realizar o pagamento de {numero_parcelas_para_pagamento} parcelas. Valor deve ser maior que zero!'

    def test_realiza_pagamento_emprestimo_pf_e_deve_gerar_erro_numero_parcelas_restantes_menor_que_numero_parcelas_pagamento(self, emprestimo_pf):
        numero_parcelas_para_pagamento = 11
        numero_parcelas_restantes = emprestimo_pf.get_numero_parcelas() - emprestimo_pf.get_numero_parcelas_pagas() 

        with pytest.raises(Exception) as excinfo:
            emprestimo_pf.realizar_pagamento(numero_parcelas_para_pagamento)
        assert str(excinfo.value) == f'Não foi possível realizar o pagamento de {numero_parcelas_para_pagamento} parcelas, pois faltam {numero_parcelas_restantes} parcelas para quitação do Empréstimo.'

    def test_deve_validar_emprestimo_e_deve_gerar_erro_cliente_invalido(self):
        valor_emprestimo = 10000
        numero_parcelas = 10
        numero_parcelas_pagas = 0
        tipo_emprestimo = 1

        cliente = None
        with pytest.raises(Exception) as excinfo:
            Emprestimo(valor_emprestimo, numero_parcelas, numero_parcelas_pagas, cliente, tipo_emprestimo)
        assert str(excinfo.value) == 'Não foi possível cadastrar o Empréstimo. Cliente é obrigatório! Tente novamente.'

    def test_deve_validar_emprestimo_e_deve_gerar_erro_valor_emprestimo_invalido(self):
        valor_emprestimo = -10000
        numero_parcelas = 10
        numero_parcelas_pagas = 2
        tipo_emprestimo = 3

        cliente = cliente_pj()
        with pytest.raises(Exception) as excinfo:
            Emprestimo(valor_emprestimo, numero_parcelas, numero_parcelas_pagas, cliente, tipo_emprestimo)
        assert str(excinfo.value) == 'Não foi possível cadastrar o Empréstimo. Valor deve ser maior que zero! Tente novamente.'

    def test_deve_validar_emprestimo_e_deve_gerar_erro_numero_parcelas_invalido(self):
        valor_emprestimo = 10000
        numero_parcelas = -110
        numero_parcelas_pagas = 10
        tipo_emprestimo = 1

        cliente = cliente_pj()
        with pytest.raises(Exception) as excinfo:
            Emprestimo(valor_emprestimo, numero_parcelas, numero_parcelas_pagas, cliente, tipo_emprestimo)
        assert str(excinfo.value) == 'Não foi possível cadastrar o Empréstimo. Prazo deve ser maior que zero! Tente novamente.'

    def test_deve_validar_emprestimo_e_deve_gerar_erro_tipo_emprestimo_invalido(self):
        valor_emprestimo = 10000
        numero_parcelas = 10
        numero_parcelas_pagas = 0
        tipo_emprestimo = "aaa"

        cliente = cliente_pj()
        with pytest.raises(Exception) as excinfo:
            Emprestimo(valor_emprestimo, numero_parcelas, numero_parcelas_pagas, cliente, tipo_emprestimo)
        assert str(excinfo.value) == 'Não foi possível cadastrar o Empréstimo. Tipo de Empréstimo inválido! Tente novamente.'

    def test_deve_validar_emprestimo_e_deve_gerar_erro_numero_parcelas_pagas_invalido(self):
        valor_emprestimo = 10000
        numero_parcelas = 10
        numero_parcelas_pagas = -11
        tipo_emprestimo = 2

        cliente = cliente_pj()
        with pytest.raises(Exception) as excinfo:
            Emprestimo(valor_emprestimo, numero_parcelas, numero_parcelas_pagas, cliente, tipo_emprestimo)
        assert str(excinfo.value) == 'Não foi possível cadastrar o Empréstimo. Número de Parcelas Pagas deve ser igual ou maior que zero! Tente novamente.'

    def test_deve_validar_emprestimo_e_deve_gerar_erro_numero_parcelas_pagas_maior_que_numero_parcelas(self):
        valor_emprestimo = 10000
        numero_parcelas = 10
        numero_parcelas_pagas = 11
        tipo_emprestimo = 2

        cliente = cliente_pj()
        with pytest.raises(Exception) as excinfo:
            Emprestimo(valor_emprestimo, numero_parcelas, numero_parcelas_pagas, cliente, tipo_emprestimo)
        assert str(excinfo.value) == 'Não foi possível cadastrar o Empréstimo. Número de Parcelas Pagas não pode ser superior ao Número de Parcelas do Empréstimo! Tente novamente.'

    def test_deve_imprimir_valor_parcela_com_sucesso(self, emprestimo_pf):
        emprestimo_pf.imprimir_valor_parcela()
        
        assert True

    def test_deve_imprimir_valor_pago_com_sucesso(self, emprestimo_pf):
        emprestimo_pf.imprimir_valor_pago()
        
        assert True

    def test_deve_imprimir_valor_restante_quitacao_com_sucesso(self, emprestimo_pf):
        emprestimo_pf.imprimir_valor_restante_quitacao()
        
        assert True

    def test_deve_validar_se_emprestimo_pf_e_diferente_de_emprestimo_pj_com_sucesso(self, emprestimo_pf, emprestimo_pj):
        
        assert emprestimo_pf.__eq__(emprestimo_pj) is False

    def test_deve_imprimir_dados_emprestimo_com_sucesso(self, emprestimo_pf):
        emprestimo_pf.__str__()
        
        assert True
        
