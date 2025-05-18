print('Bem vindos(a) a empresa da Wanessa Brito Ramalho')

#Lista de funcionários e id_global
lista_funcionario = []
id_global = 4916022  # RU 

# Função para cadastrar funcionário
def cadastrar_funcionario(id):
    print('-'*70)
    print('-'*20, 'MENU CADASTRAR FUNCIONÁRIO', '-'*22)
    nome = input('Digite seu nome: ')
    setor = input('Digite seu setor: ')
    salario = float(input('Digite seu salário: '))

    dados_funcionario = {
        'id': id,
        'nome': nome,
        'setor': setor,
        'salario': salario,
    }

    lista_funcionario.append(dados_funcionario.copy())
    print(f"Funcionário cadastrado com sucesso! ID: {id}")

# Função para consultar funcionários
def consultar_funcionarios():
    while True:
        try:
            print('-'*70)
            print('-'*20, 'MENU CONSULTAR FUNCIONÁRIO', '-'*22)
            texto = '''
Escolha a opção desejada:
1 - Consultar Todos os Funcionários
2 - Consultar Funcionário por ID
3 - Consultar Funcionário(s) por Setor
4 - Retornar
'''
            print(texto)
            opcao = int(input('Escolha a opção desejada: '))

            if opcao == 1:
                for i in lista_funcionario:
                    print(f"ID: {i['id']}\nNome: {i['nome']}\nSetor: {i['setor']}\nSalário: R${i['salario']:.2f}\n")

            elif opcao == 2:
                id_consulta = int(input('Digite o ID do funcionário: '))
                encontrado = False
                for i in lista_funcionario:
                    if i['id'] == id_consulta:
                        print(f"ID: {i['id']}\nNome: {i['nome']}\nSetor: {i['setor']}\nSalário: {i['salario']}\n")
                        encontrado = True
                        break
                if not encontrado:
                    print('ID não encontrado')

            elif opcao == 3:
                setor_consulta = input('Digite o setor do funcionário: ')
                encontrados = False
                for i in lista_funcionario:
                    if i['setor'] == setor_consulta:
                        print(f"ID: {i['id']}\nNome: {i['nome']}\nSetor: {i['setor']}\nSalário: {i['salario']}\n")
                        encontrados = True
                if not encontrados:
                    print('Setor não encontrado')

            elif opcao == 4:
                return

            else:
                print('Opção inválida')

        except ValueError:
            print('Opção inválida')

# Função para remover funcionário
def remover_funcionario():
    while True:
        try:
            print('-'*70)
            print('-'*20, 'MENU REMOVER FUNCIONÁRIO', '-'*24)

            id_remover = int(input('Digite o ID do funcionário a ser removido: '))
            encontrado = False
            for i in lista_funcionario:
                if i['id'] == id_remover:
                    lista_funcionario.remove(i)
                    encontrado = True
                    print(f'Funcionário com ID {id_remover} removido com sucesso.')
                    return 

            if not encontrado:
                print('ID de funcionário não encontrado.')

        except ValueError:
            print('ID inválido')

# Estrutura de menu no código principal
while True:
    print('-'*76)
    print('-'*27, 'MENU PRINCIPAL', '-'*33)
    print('Escolha a opção desejada: \n1 - Cadastrar Funcionário(s)\n2 - Consultar Funcionário(s)\n3 - Remover Funcionário(s)\n4 - Encerrar Programa ')
    escolha = input('Digite a opção desejada: ')

    if escolha == '1':
        id_global += 1
        cadastrar_funcionario(id_global)

    elif escolha == '2':
        consultar_funcionarios()

    elif escolha == '3':
        remover_funcionario()

    elif escolha == '4':
        print('Encerrando o programa...')
        break

    else:
        print('Opção inválida. Por favor, escolha uma opção entre 1 e 4.')