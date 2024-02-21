import pytest

# class EmprestimoTest():

def test_create_emprestimo_success(emprestimo_pessoa_fisica):
    emprestimo = emprestimo_pessoa_fisica

    assert emprestimo is not None
    assert emprestimo.verificar_emprestimo_quitado() is False

def test_create_emprestimo_error(emprestimo_pessoa_juridica):
    emprestimo = emprestimo_pessoa_juridica

    emprestimo_valido = emprestimo._validar_emprestimo()
    assert emprestimo_valido is True
