from src.main.domain.emprestimo import *
from src.main.domain.pessoa_fisica import *

def test_create_emprestimo_success():
    valor_emprestimo = 10000
    numero_parcelas = 10
    numero_parcelas_pagas = 10
    tipo_emprestimo = TipoEmprestimo.PESSOAL

    nome = 'Luiz'
    cpf = '123.456.789-10'
    telefone = '3333-4444'
    titulo_eleitor = '55555'

    cliente = PessoaFisica(nome, telefone, cpf, titulo_eleitor)
    emprestimo = Emprestimo(valor_emprestimo, numero_parcelas, numero_parcelas_pagas, cliente, tipo_emprestimo)

    assert emprestimo is not None
    assert emprestimo.verificar_emprestimo_quitado() is True