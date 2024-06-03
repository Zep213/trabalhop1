def listar_para(list):
    for indices_att in list:
        print(f'{list.index(indices_att)} - {indices_att}')
def adicionar_film(list):
    qntd_filmes = int(input('quantos filmes voce quer adicionar? '))
    for qntdf in range(qntd_filmes):
        nome_filme = input('digite o nome do filme que deseja adicionar: ')
        list.append(nome_filme)
    print(f'{qntd_filmes} filme(s) foram adicionados!!')
def log_usuario(login, senha, dicionario, tipo):
    for chave in dicionario:
        if (chave == login and dicionario[login][2] == senha and dicionario[login][1] == tipo):
            return True
    return False
def add_cliente(dict):
    nome = input('digite seu nome')
    login = input('digite seu login')
    senha = input('digite sua senha')
    perfil = 1

    dict[login] = [nome, perfil, senha]
    print('Cadastro realizado com sucesso!!!\n')
#adicionar mais 1 funcionalidade no cliente!!!!
def menu_adm():
    print('\033[34m________MENU ADM________\033[0;0m')
    print('\033[35m1-adicionar adm ou cliente')
    print('2-adicionar filme')
    print('3-atualizar filme')
    print('4-excluir filme')
    print('5-buscar filme')
    print('6-lista dos filmes adicionados')
    print('0-sair\033[0;0m')

def menu_main():
    print('\033[34m________MENU________\033[0;0m')
    print('\033[96m1-login adm')
    print('2-adicionar cliente')
    print('3-login cliente')
    print('0- sair')
def cadastrar_cliente(dict):
    nome = input('digite seu nome')
    login = input('digite seu login')
    senha = input('digite sua senha')
    dict[login] = [nome, 1, senha]
    print('Cadastro realizado com sucesso!!!\n')
def menu_cliente():
    print('\033[34m________MENU CLIENTE________\033[0;0m')
    print('\033[96m1-compra de ingressos')
    print('2-filmes em cartazes/horarios')
    print('0-sair\033[0;0m')

def menu_salas():
    print('\033[34m________MENU DA SALA________\033[0;0m')
    print('\033[92m1-sala 1 50 vagas / ingressos: 35R$ / 17,50R$')
    print('2-sala 2 35 vagas / ingressos: 24R$ / 12R$')
    print('3-sala 3 15 vagas / ingressos: 30R$ / 15R$\033[0;0m')
    print('\033[97m0-menu do cliente\033[0;0m')

def compra_ingresso1():
    capacidade_maxima = 50
    valor_ingresso_inteiro = 35
    valor_ingresso_meio = 17.50
    ingressos_vendidos = []
    total_inteiros = 0
    total_meios = 0

    while True:
        tipo_ingresso = input(
            'voce deseja comprar ingressos i, m ou e para sair da compra: ')

        if tipo_ingresso == 'i':
            ingressos_inteiros = int(
                input('quantos ingressos inteiros você deseja comprar: '))
            if total_inteiros + ingressos_inteiros + total_meios > capacidade_maxima:
                print('desculpe, a sala está lotada.')
            else:
                ingressos_vendidos.append(f'{ingressos_inteiros} ingressos inteiros')
                total_inteiros += ingressos_inteiros
        elif tipo_ingresso == 'm':
            ingressos_meios = int(
                input('quantos ingressos de meia-entrada você deseja comprar: '))
            if total_meios + ingressos_meios + total_inteiros > capacidade_maxima:
                print('desculpe, a sala está lotada.')
            else:
                ingressos_vendidos.append(f'{ingressos_meios} ingressos de meia-entrada')
                total_meios += ingressos_meios
        elif tipo_ingresso == 'e':
            break

        else:
            print(
                "opcao invalida, por favor, escolha entre 'inteiros', 'meia-entrada' ou 'encerrar'.")

    total_ingressos = total_inteiros + total_meios

    if total_ingressos <= capacidade_maxima:
        valor_total = (total_inteiros * valor_ingresso_inteiro) + (
                total_meios * valor_ingresso_meio)
        print(f'\033[32mo valor total a pagar é de R${valor_total}\033[0;0m')

        print('ingressos vendidos:')
        for ingresso in ingressos_vendidos:
            print(ingresso)


def compra_ingresso2():
    capacidade_maxima = 35
    valor_ingresso_inteiro = 24
    valor_ingresso_meio = 12
    ingressos_vendidos = []
    total_inteiros = 0
    total_meios = 0

    while True:
        tipo_ingresso = input(
            'voce deseja comprar ingressos i, m ou e para sair da compra: ')

        if tipo_ingresso == 'i':
            ingressos_inteiros = int(
                input('quantos ingressos inteiros você deseja comprar: '))
            if total_inteiros + ingressos_inteiros + total_meios > capacidade_maxima:
                print('desculpe, a sala está lotada.')
            else:
                ingressos_vendidos.append(f'{ingressos_inteiros} ingressos inteiros')
                total_inteiros += ingressos_inteiros
        elif tipo_ingresso == 'm':
            ingressos_meios = int(
                input('quantos ingressos de meia-entrada você deseja comprar: '))
            if total_meios + ingressos_meios + total_inteiros > capacidade_maxima:
                print('desculpe, a sala está lotada.')
            else:
                ingressos_vendidos.append(f'{ingressos_meios} ingressos de meia-entrada')
                total_meios += ingressos_meios
        elif tipo_ingresso == 'e':
            break

        else:
            print("opcao invalida, por favor, escolha entre 'inteiros', 'meia-entrada'"
                  " ou 'encerrar'.")

    total_ingressos = total_inteiros + total_meios

    if total_ingressos <= capacidade_maxima:
        valor_total = (total_inteiros * valor_ingresso_inteiro) + (
                total_meios * valor_ingresso_meio)
        print(f'o valor total a pagar é de R${valor_total}.')

        print('ingressos vendidos:')
        for ingresso in ingressos_vendidos:
            print(ingresso)

def compra_ingresso3():
    capacidade_maxima = 15
    valor_ingresso_inteiro = 30
    valor_ingresso_meio = 15
    ingressos_vendidos = []
    total_inteiros = 0
    total_meios = 0

    while True:
        tipo_ingresso = input(
            'voce deseja comprar ingressos i, m ou e para sair da compra: ')

        if tipo_ingresso == 'i':
            ingressos_inteiros = int(
                input('quantos ingressos inteiros você deseja comprar: '))
            if total_inteiros + ingressos_inteiros + total_meios > capacidade_maxima:
                print('desculpe, a sala está lotada.')
            else:
                ingressos_vendidos.append(f'{ingressos_inteiros} ingressos inteiros')
                total_inteiros += ingressos_inteiros
        elif tipo_ingresso == 'm':
            ingressos_meios = int(
                input('quantos ingressos de meia-entrada você deseja comprar: '))
            if total_meios + ingressos_meios + total_inteiros > capacidade_maxima:
                print('desculpe, a sala está lotada.')
            else:
                ingressos_vendidos.append(f'{ingressos_meios} ingressos de meia-entrada')
                total_meios += ingressos_meios
        elif tipo_ingresso == 'e':
            break

        else:
            print("opcao invalida, por favor, escolha entre 'inteiros', 'meia-entrada'"
                  " ou 'encerrar'.")

    total_ingressos = total_inteiros + total_meios

    if total_ingressos <= capacidade_maxima:
        valor_total = (total_inteiros * valor_ingresso_inteiro) + (
                total_meios * valor_ingresso_meio)
        print(f'o valor total a pagar é de R${valor_total}.')

        print('Ingressos vendidos:')
        for ingresso in ingressos_vendidos:
            print(ingresso)
def filmes_cartaz():
    print('\033[97mfilmes em cartazes sao:')
    print('\033[91m1-homem ranha')
    print('2-vingadores')
    print('3-deadpool 3')
    print('0-menu do cliente\033[0;0m')
def filme_1():
    filmeh = 'homem aranha'
    horarios = '13', '14', '15'
    print(f'os horarios disponiveis sao:{horarios}')
    horario = int(input('que horario vc deseja: '))
    print(f'{filmeh} no horario das {horario} horas')

    op = 99
    while (op != 0):
        menu_comidas()
        break
def filme_2():
    filmev = 'vingadores'
    horarios = '14', '16', '18'
    print(f'os horarios disponiveis sao:{horarios}')
    horario = int(input('que horario vc deseja: '))
    print(f'{filmev} no horario das {horario} horas')

    op = 99
    while (op != 0):
        menu_comidas()
        break
def filme_3():
    filmed = 'deadpool'
    horarios = '15', '17', '19'
    print(f'os horarios disponiveis sao:{horarios}')
    horario = int(input('que horario vc deseja: '))
    print(f'{filmed} no horario das {horario} horas')

    op = 99
    while (op != 0):
        menu_comidas()
        break
def menu_comidas():
    print('\033[34m_______MENU DE COMIDAS________\033[0;0m')
    print('\033[96m1-comidas')
    print('2-combos')
    print('0-seguir ao filme\033[0;0m')
    op = int(input('\033[34moque voce deseja: \033[0;0m'))

    if (op == 1):
        comidas = print('essas sao as comidas:''pipoca', 'chocolates', 'salgadinho', 'refrigerantes')
        comida = input('quais comidas o senhor(a) deseja: ')
        print(f'obrigado pela compra da(s) {comida}')

    elif (op == 2):
        combos = print('esses sao os combos:''pipoca tamanho gigante', 'refil de 1 litro de refrigerante',
                       'barras de chocolate')
        combo = input('quais combos o senhor(a) deseja: ')
        print(f'obrigado por ter escolhido nosso(s) combo(s) de {combo}')

    elif (op == 0):
        print('\033[93mseguindo ao filme... \033[0;0m')