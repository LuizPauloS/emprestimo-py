from src.main.domain.emprestimo import *
from src.main.domain.pessoa_fisica import *
from src.main.domain.pessoa_juridica import *
from uuid import UUID

def main():
    continuar = True
    emprestimo = None
    cliente = None
    lista_clientes = []
    lista_emprestimos = []

    while continuar:

        try:
            print(('-' * 21) + ' MENU ' + ('-' * 21))
            print('[1] Cadastrar Novo Cliente')
            print('[2] Cadastrar Novo Empréstimo')
            print('[3] Imprimir Dados Empréstimos')
            print('[4] Imprimir Dados Clientes')
            print('[5] Realizar Pagamento')
            print('[6] Imprimir Valor Já Pago')
            print('[7] Verificar Empréstimo Quitado')
            print('[8] Imprimir Empréstimo Maior Valor')
            print('[9] Imprimir Empréstimo Menor Valor')
            print('[10] Imprimir Valor Médio Empréstimos')
            print('[11] Imprimir Valor Total Empréstimos')
            print('[12] Imprimir Dados Empréstimo Por ID')
            print('[0] Sair')
            print('-' * 48)
            opcao = str(input('Informe a opção escolhida: '))
            if _validar_opcao_selecionada_inteiro(opcao): 
                raise ValueError('Opção Selecionada Inválida! Tente novamente.')

            match int(opcao):
                case 1: # Cadastrar Novo Cliente
                    print('-' * 48)
                    print('Dados do Cliente')
                    nome = str(input('Informe o Nome: '))
                    telefone = str(input('Informe o Telefone: '))

                    print(('-' * 17) + ' Tipo Pessoa ' + ('-' * 18))
                    print('[1] - Pessoa Física')
                    print('[2] - Pessoa Jurídica')
                    print('-' * 48)
                    tipo_pessoa = int(input('Selecione o Tipo Pessoa do Empréstimo: '))

                    if tipo_pessoa is not None and tipo_pessoa > 0 and tipo_pessoa <= 2:
                        if tipo_pessoa == 1:
                            cpf = str(input('Informe o CPF: '))
                            titulo_eleitor = str(input('Informe o Titulo Eleitor: '))
                            cliente = PessoaFisica(nome, telefone, cpf, titulo_eleitor)
                        elif tipo_pessoa == 2:
                            cnpj = str(input('Informe o CNPJ: '))
                            inscricao_estadual = str(input('Informe a Inscrição Estadual: '))
                            cliente = PessoaJuridica(nome, telefone, cnpj, inscricao_estadual)

                        if cliente._validar_cliente():
                            lista_clientes.append(cliente)
                            print('-' * 48 + f'\nCliente cadastrado com sucesso! Id: {cliente.get_id()}')
                            cliente = None
                    else:
                        print('Cadastro de Cliente não realizado. Tipo pessoa inválido! Tente novamente.')

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
                
                    id_cliente = str(input('Informe o Id do Cliente do Empréstimo: '))
                    cliente = buscar_cliente_por_id(id_cliente, lista_clientes)

                    emprestimo = Emprestimo(valor_emprestimo, numero_parcelas, numero_parcelas_pagas, cliente, tipo_emprestimo)
                    lista_emprestimos.append(emprestimo)
                    print('-' * 48 + f'\nEmpréstimo cadastrado com sucesso! Id: {emprestimo.get_id()}')
                    emprestimo = None

                case 3: #Imprimir Dados Empréstimos
                    if not verificar_lista_vazia(lista_emprestimos, 'Empréstimo'):
                        print('-' * 48)
                        for emprestimo in lista_emprestimos:
                            print(emprestimo.__str__() + '\n')
                            print('-' * 48)
                           
                case 4: # Imprimir Dados Clientes
                    if not verificar_lista_vazia(lista_clientes, 'Cliente'):
                        print('-' * 48) 
                        for cliente in lista_clientes:
                            print(cliente.__str__() + '\n')
                            print('-' * 48)

                case 5: # Realizar Pagamento
                        if not verificar_lista_vazia(lista_emprestimos, 'Empréstimo'):
                            print('-' * 48)
                            id_emprestimo = str(input('Informe o Id do Empréstimo que deseja realizar pagamento: '))
                            quantidade_parcelas_pagamento = int(input('Informe a quantidade de parcelas que deseja realizar pagamento: '))
                            if quantidade_parcelas_pagamento is not None:
                                emp = buscar_emprestimo_por_id(id_emprestimo, lista_emprestimos)
                                if emp is not None: 
                                    emp.realizar_pagamento(quantidade_parcelas_pagamento)

                case 6: # Imprimir Valor Já Pago
                    if not verificar_lista_vazia(lista_emprestimos, 'Empréstimo'):
                        print('-' * 48)
                        id_emprestimo = str(input('Informe o Id do Empréstimo que deseja ver o valor já pago: '))
                        emp = buscar_emprestimo_por_id(id_emprestimo, lista_emprestimos)
                        if emp is not None: 
                            emp.imprimir_valor_pago()
                
                case 7: # Verificar Empréstimo Quitado
                    if not verificar_lista_vazia(lista_emprestimos, 'Empréstimo'):
                        print('-' * 48)
                        id_emprestimo = str(input('Informe o Id do Empréstimo que deseja ver a Situação: '))
                        emp = buscar_emprestimo_por_id(id_emprestimo, lista_emprestimos)
                        if emp is not None:
                            emprestimo_quitado = emp.verificar_emprestimo_quitado()
                            print('Situação do Empréstimo: ' + ('Quitado' if emprestimo_quitado else 'Em Aberto'))
                            if not emprestimo_quitado:
                                emp.imprimir_valor_restante_quitacao()
                
                case 8: # Imprimir Empréstimo Maior Valor
                    if not verificar_lista_vazia(lista_emprestimos, 'Empréstimo'):
                        print('-' * 48)
                        emprestimo_maior_valor = __buscar_emprestimo_maior_valor(lista_emprestimos)
                        print('Empréstimo Maior Valor')
                        print(f'Id: {emprestimo_maior_valor.get_id()}')
                        print(f'Valor: R$ {emprestimo_maior_valor.get_valor_emprestimo():.2f}')
                    
                case 9: # Imprimir Empréstimo Menor Valor
                    if not verificar_lista_vazia(lista_emprestimos, 'Empréstimo'):
                        print('-' * 48)
                        emprestimo_menor_valor = __buscar_emprestimo_menor_valor(lista_emprestimos)
                        print('Empréstimo Menor Valor')
                        print(f'Id: {emprestimo_menor_valor.get_id()}')
                        print(f'Valor: R$ {emprestimo_menor_valor.get_valor_emprestimo():.2f}')

                case 10: # Imprimir Valor Médio Empréstimos
                    if not verificar_lista_vazia(lista_emprestimos, 'Empréstimo'):
                        print('-' * 48)
                        valor_medio = __buscar_valor_medio_emprestimos(lista_emprestimos)
                        print(f'Valor Médio Empréstimos: R$ {valor_medio:.2f}')

                case 11: # Imprimir Valor Total Empréstimos
                    if not verificar_lista_vazia(lista_emprestimos, 'Empréstimo'):
                        print('-' * 48)
                        valor_total = __buscar_valor_total_emprestimos(lista_emprestimos)
                        print(f'Valor Total Empréstimos: R$ {valor_total:.2f}')

                case 12: #Imprimir Dados Empréstimo Por ID
                    if not verificar_lista_vazia(lista_emprestimos, 'Empréstimo'):
                        print('-' * 48)
                        id_emprestimo = str(input('Informe o Id do Empréstimo que deseja ver os dados: '))
                        emp = buscar_emprestimo_por_id(id_emprestimo, lista_emprestimos)
                        if emp is not None:
                            print('-' * 48)
                            print(emp.__str__())
                
                case 0: # Sair
                    continuar = False
                    print('Encerrando Sistema de Empréstimos.')

        except Exception as error:
            print(error)


def buscar_emprestimo_por_id(id_emprestimo, lista_emprestimos) -> Emprestimo:
    emprestimo_encontrado = None
    if __validar_id(id_emprestimo):
        for emprestimo in lista_emprestimos:
            if id_emprestimo is not None and str(id_emprestimo).strip() == str(emprestimo.get_id()).strip():
                emprestimo_encontrado = emprestimo
    if emprestimo_encontrado is None:
        print(f'Empréstimo não encontrado. Id: {id_emprestimo} informado é Inválido! Tente novamente.')
    return emprestimo_encontrado

def buscar_cliente_por_id(id_cliente, lista_clientes) -> Pessoa:
    cliente_encontrato = None
    if __validar_id(id_cliente):
        for cliente in lista_clientes:
            if id_cliente is not None and str(id_cliente).strip() == str(cliente.get_id()).strip():
                cliente_encontrato = cliente
    if cliente_encontrato is None:
        print(f'Cliente não encontrado. Id: {id_cliente} informado é Inválido! Tente novamente.')
    return cliente_encontrato

def verificar_lista_vazia(lista, nome_lista) -> bool:
    if lista is None or len(lista) == 0:
        print(f'Nenhum {nome_lista} cadastrado até o momento! Tente novamente.')
        return True
    else:
        return False

def __buscar_emprestimo_maior_valor(lista_emprestimos):
    emprestimo_maior_valor = None
    for emprestimo in lista_emprestimos:
        if emprestimo_maior_valor is None or emprestimo.get_valor_emprestimo() > emprestimo_maior_valor.get_valor_emprestimo():
            emprestimo_maior_valor = emprestimo
    return emprestimo_maior_valor

def __buscar_emprestimo_menor_valor(lista_emprestimos):
    emprestimo_menor_valor = None
    for emprestimo in lista_emprestimos:
        if emprestimo_menor_valor is None or emprestimo.get_valor_emprestimo() < emprestimo_menor_valor.get_valor_emprestimo():
            emprestimo_menor_valor = emprestimo
    return emprestimo_menor_valor

def __buscar_valor_medio_emprestimos(lista_emprestimos):
    valor_total= 0.0
    valor_medio = 0.0
    for emprestimo in lista_emprestimos:
        valor_total += emprestimo.get_valor_emprestimo()
    valor_medio = valor_total / len(lista_emprestimos)
    return valor_medio

def __buscar_valor_total_emprestimos(lista_emprestimos):
    valor_total= 0.0
    for emprestimo in lista_emprestimos:
        valor_total += emprestimo.get_valor_emprestimo()
    return valor_total

def __validar_id(id):
    try:
        uuid = UUID(id)
    except ValueError:
        return False
    return str(uuid) == id

def _validar_opcao_selecionada_inteiro(opcao: str) -> bool:
    return isinstance(opcao, int)

if __name__ == '__main__':
    main()
