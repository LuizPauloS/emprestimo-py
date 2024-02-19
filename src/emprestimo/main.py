from domain.emprestimo import *
from domain.pessoa import *
from uuid import UUID

def main():
    continuar = True
    emprestimo = None
    cliente = None
    lista_emprestimos = []

    while continuar:

        print(('-' * 21) + ' MENU ' + ('-' * 21))
        print('[1] Cadastrar Cliente')
        print('[2] Cadastrar Novo Empréstimo')
        print('[3] Imprimir Dados Todos Empréstimos')
        print('[4] Realizar Pagamento')
        print('[5] Imprimir Valor Já Pago')
        print('[6] Verificar Empréstimo Quitado')
        print('[7] Imprimir Empréstimo Maior Valor')
        print('[8] Imprimir Empréstimo Menor Valor')
        print('[9] Imprimir Valor Médio Empréstimos')
        print('[10] Imprimir Valor Total Empréstimos')
        print('[11] Imprimir Dados Empréstimo Por ID')
        print('[0] Sair')
        print('-' * 48)
        opcao = int(input('Informe a opção escolhida: '))

        match opcao:
            case 1: # Cadastrar Cliente
                print('-' * 48)
                print('Dados do Cliente')
                nome = str(input('Informe o Nome: '))
                telefone = str(input('Informe o Telefone: '))
                cpf = str(input('Informe o CPF: '))
                cliente = Pessoa(nome, telefone, cpf)

            case 2: # Cadastrar Novo Empréstimo
                print('-' * 48)
                valor_emprestimo = float(input('Informe o Valor do Empréstimo: R$ '))
                numero_parcelas = int(input('Informe o Prazo do Empréstimo: '))
                numero_parcelas_pagas = int(input('Informe a Quantidade de Parcelas Pagas do Empréstimo: '))

                print(('-' * 9) + ' Tipo de Empréstimo ' + ('-' * 9))
                print('[1] - PESSOAL')
                print('[2] - ROTATIVO')
                print('[3] - CONSIGNADO')
                print('-' * 48)
                tipo_emprestimo = int(input('Selecione o Tipo de Empréstimo: '))

                emprestimo = Emprestimo(valor_emprestimo, numero_parcelas, numero_parcelas_pagas, cliente, tipo_emprestimo)
                if emprestimo._validar_emprestimo():
                    lista_emprestimos.append(emprestimo)
                    print(f'Empréstimo criado com sucesso! Id: {emprestimo.get_id()}')

            case 3: #Imprimir Dados Todos Empréstimos
                if not verificar_lista_vazia(lista_emprestimos):
                    print('-' * 48)
                    for emprestimo in lista_emprestimos:
                        print(emprestimo.__str__() + '\n')
                        print('-' * 48)
                
            case 4: # Realizar Pagamento
                if not verificar_lista_vazia(lista_emprestimos):
                    print('-' * 48)
                    id_emprestimo = str(input('Informe o Id do Empréstimo que deseja realizar pagamento: '))
                    quantidade_parcelas_pagamento = int(input('Informe a quantidade de parcelas que deseja realizar pagamento: '))
                    if quantidade_parcelas_pagamento is not None and quantidade_parcelas_pagamento > 0:
                        emp = buscar_emprestimo_por_id(id_emprestimo, lista_emprestimos)
                        if emp is not None: 
                            emp.realizar_pagamento(quantidade_parcelas_pagamento)

            case 5: # Imprimir Valor Já Pago
                if not verificar_lista_vazia(lista_emprestimos):
                    print('-' * 48)
                    id_emprestimo = str(input('Informe o Id do Empréstimo que deseja ver o valor já pago: '))
                    emp = buscar_emprestimo_por_id(id_emprestimo, lista_emprestimos)
                    if emp is not None: 
                        emp.imprimir_valor_pago()
            
            case 6: # Verificar Empréstimo Quitado
                if not verificar_lista_vazia(lista_emprestimos):
                    print('-' * 48)
                    id_emprestimo = str(input('Informe o Id do Empréstimo que deseja ver a Situação: '))
                    emp = buscar_emprestimo_por_id(id_emprestimo, lista_emprestimos)
                    if emp is not None:
                        emprestimo_quitado = emp.verificar_emprestimo_quitado()
                        print('Situação do Empréstimo: ' + ('Quitado' if emprestimo_quitado else 'Em Aberto'))
                        if not emprestimo_quitado:
                            emp.imprimir_valor_restante_quitacao()
            
            case 7: # Imprimir Empréstimo Maior Valor
                if not verificar_lista_vazia(lista_emprestimos):
                    print('-' * 48)
                    emprestimo_maior_valor = buscar_emprestimo_maior_valor(lista_emprestimos)
                    print('Empréstimo Maior Valor')
                    print(f'Id: {emprestimo_maior_valor.get_id()}')
                    print(f'Valor: R$ {emprestimo_maior_valor.get_valor_emprestimo():.2f}')
                
            case 8: # Imprimir Empréstimo Menor Valor
                if not verificar_lista_vazia(lista_emprestimos):
                    print('-' * 48)
                    emprestimo_menor_valor = buscar_emprestimo_menor_valor(lista_emprestimos)
                    print('Empréstimo Menor Valor')
                    print(f'Id: {emprestimo_menor_valor.get_id()}')
                    print(f'Valor: R$ {emprestimo_menor_valor.get_valor_emprestimo():.2f}')

            case 9: # Imprimir Valor Médio Empréstimos
                if not verificar_lista_vazia(lista_emprestimos):
                    print('-' * 48)
                    valor_medio = buscar_valor_medio_emprestimos(lista_emprestimos)
                    print(f'Valor Médio Empréstimos: R$ {valor_medio:.2f}')

            case 10: # Imprimir Valor Total Empréstimos
                if not verificar_lista_vazia(lista_emprestimos):
                    print('-' * 48)
                    valor_total = buscar_valor_total_emprestimos(lista_emprestimos)
                    print(f'Valor Total Empréstimos: R$ {valor_total:.2f}')

            case 11: #Imprimir Dados Empréstimo Por ID
                if not verificar_lista_vazia(lista_emprestimos):
                    print('-' * 48)
                    id_emprestimo = str(input('Informe o Id do Empréstimo que deseja ver os dados: '))
                    emp = buscar_emprestimo_por_id(id_emprestimo, lista_emprestimos)
                    if emp is not None:
                        print('-' * 48)
                        print(emp.__str__())
            
            case 0: # Sair
                continuar = False
                print('Encerrando Sistema de Empréstimos.')
            
            case _:
                print('Opção Selecionada Inválida! Tente novamente.')


def buscar_emprestimo_por_id(id_emprestimo, lista_emprestimos) -> Emprestimo:
    emprestimo_encontrado = None
    if validar_id_emprestimo(id_emprestimo):
        for emprestimo in lista_emprestimos:
            if id_emprestimo is not None and str(id_emprestimo).strip() == str(emprestimo.get_id()).strip():
                emprestimo_encontrado = emprestimo
    if emprestimo_encontrado is None:
        print(f'Empréstimo não encontrado. Id: {id_emprestimo} de empréstimo informado é Inválido! Tente novamente.')
    return emprestimo_encontrado


def verificar_lista_vazia(lista_emprestimos):
    if lista_emprestimos is None or len(lista_emprestimos) == 0:
        print('Nenhum Empréstimo cadastrado até o momento! Tente novamente.')
        return True
    else:
        return False

def buscar_emprestimo_maior_valor(lista_emprestimos):
    emprestimo_maior_valor = None
    for emprestimo in lista_emprestimos:
        if emprestimo_maior_valor is None or emprestimo.get_valor_emprestimo() > emprestimo_maior_valor.get_valor_emprestimo():
            emprestimo_maior_valor = emprestimo
    return emprestimo_maior_valor

def buscar_emprestimo_menor_valor(lista_emprestimos):
    emprestimo_menor_valor = None
    for emprestimo in lista_emprestimos:
        if emprestimo_menor_valor is None or emprestimo.get_valor_emprestimo() < emprestimo_menor_valor.get_valor_emprestimo():
            emprestimo_menor_valor = emprestimo
    return emprestimo_menor_valor

def buscar_valor_medio_emprestimos(lista_emprestimos):
    valor_total= 0.0
    valor_medio = 0.0
    for emprestimo in lista_emprestimos:
        valor_total += emprestimo.get_valor_emprestimo()
    valor_medio = valor_total / len(lista_emprestimos)
    return valor_medio

def buscar_valor_total_emprestimos(lista_emprestimos):
    valor_total= 0.0
    for emprestimo in lista_emprestimos:
        valor_total += emprestimo.get_valor_emprestimo()
    return valor_total

def validar_id_emprestimo(id_emprestimo):
    try:
        uuid = UUID(id_emprestimo)
    except ValueError:
        return False
    return str(uuid) == id_emprestimo

main()
