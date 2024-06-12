from datetime import datetime
import random


promocao = {
    'Monday': {
        'nome': 'segunda 2x1',
        'detalhes': ['ingressos em dobro: na compra de um ingresso, o segundo é gratuito.'],
        'desconto': 0.0},

    'Wednesday': {
        'nome': 'quarta do cliente fiel',
        'detalhes': [
            'Bônus especial de quarta-feira do cliente : Desconto adicional de 10%.'],
        'desconto': 0.10}}

salas = {
    1: {'nome': 'sala 1 - 2D',
        'preco_ingresso_inteiros': 15.00,
        'preco_ingresso_meios': 7.50,
        'num_poltronas': 50,
        'opcoes': ['dublado'] + ['legendado']},

    2: {'nome': 'sala 2 - 3D',
        'preco_ingresso_inteiros': 25.00,
        'preco_ingresso_meios': 12.50,
        'num_poltronas': 35,
        'opcoes': ['dublado'] + ['legendado']},

    3: {'nome': 'sala 3 - IMAX',
        'preco_ingresso_inteiros': 35.00,
        'preco_ingresso_meios': 17.50,
        'num_poltronas': 15,
        'opcoes': ['dublado'] + ['legendado']}}
codigo = random.randint(1, 99)
ocupacao_salas = {sala_id: sala_info["num_poltronas"] for sala_id, sala_info in salas.items()}
dia = datetime.now().strftime("%A")
dia_promocao = promocao.get(dia, {"nome": "nenhuma promocao disponivel", "detalhes": [""],
                                  "desconto": 0.0})


def listar_para(list):
    for indices in list:
        print(f'{list.index(indices)} - {indices}')


def adicionar_film(list):
    qntd_filmes = validar_num('quantos filmes voce quer adicionar? ')
    for qntdf in range(qntd_filmes):
        nome_filme = validar_texto('digite o nome do filme que deseja adicionar: ')
        list.append(nome_filme)
    print(f'{qntd_filmes} filme(s) foram adicionados!!')


def log_usuario(login, senha, dicionario, tipo):
    for chave in dicionario:
        if (chave == login and dicionario[login][2] == senha and dicionario[login][1] == tipo):
            return True
    return False


def menu_adm():
    print('\033[34m________MENU ADM________\033[0;0m')
    print('\033[35m1-adicionar adm ou cliente')
    print('2-adicionar filme')
    print('3-atualizar filme')
    print('4-excluir filme')
    print('5-buscar filme')
    print('6-lista dos filmes adicionados')
    print('7-promoçoes da semana')
    print('8-pedidos dos clientes')
    print('9-em breve...')
    print('0-sair\033[0;0m')


def menu_main():
    print('\033[34m________MENU________\033[0;0m')
    print('\033[96m1-login adm')
    print('2-adicionar cliente')
    print('3-login cliente')
    print('0- sair')


def cadastrar_cliente(dict):
    global nome
    nome = validar_texto('digite seu nome: ')
    login = validar_texto('digite seu login: ')
    senha = validar_texto('digite sua senha: ')
    dict[login] = [nome, 1, senha]
    print('Cadastro realizado com sucesso!!!\n')


def menu_cliente():
    print('\033[34m________MENU CLIENTE________\033[0;0m')
    print('\033[96m1-compra de ingressos')
    print('2-filmes em cartazes/horarios')
    print('0-sair\033[0;0m')


def validar_texto(texto):
    campo = input(texto)
    while (len(campo) == 0):
        print('erro!! campo vazio')
        campo = input(texto)
    return campo


def validar_num(num):
    campo = int(input(num))
    while len(num) <= 0:
        print('erro!! preencha o campo corretamente.')
        campo = int(input(num))
    return campo


def mostrar_salas():
    print(f"promocao de hoje ({dia}): {dia_promocao['nome']}")
    for detalhe in dia_promocao['detalhes']:
        print(f"- {detalhe}")

    print("\nSalas disponíveis:")
    for sala_id, sala_info in salas.items():#sala_id e sala_info ta sendo repetido 2 vezes e com 2 valores diferentes
        poltronas_disponiveis = ocupacao_salas[sala_id]
        print(
            f"{sala_id}: {sala_info['nome']} - Preço do ingresso inteiro: R$ {sala_info['preco_ingresso_inteiros']} - Preço do meio-ingresso: R$ {sala_info['preco_ingresso_meios']} - Poltronas disponíveis: {poltronas_disponiveis}")
        print('opcoes de exibicao:')
        for opcao in sala_info["opcoes"]:
            print(f"- {opcao}")


def escolher_sala():
    global valor, quantidade_inteiros, quantidade_meios, nota_fiscal
    mostrar_salas()
    while True:
        sala_escolhida = validar_num('\ndigite o numero da sala escolhida: ')
        if sala_escolhida in salas:
            sala_info = salas[sala_escolhida]
            break
        else:
            print('sala invalida. por favor, escolha uma sala valida.')
    while True:
        opcao_escolhida = validar_texto("voce prefere assistir ao filme dublado ou legendado: ").lower()
        print(f"opcao escolhida: {opcao_escolhida}")
        if opcao_escolhida in sala_info["opcoes"]:
            break
        else:
            print("opcao invalida, por favor, escolha 'dublado' ou 'legendado'.")
    while True:
        quantidade_inteiros = validar_num('digite a quantidade de ingressos inteiros: ')
        quantidade_meios = validar_num('digite a quantidade de meio-ingressos: ')
        valor_total_ingressos = quantidade_inteiros  + quantidade_meios
        valor_total = valor_total_ingressos
        print(f'esse é seu codigo: {codigo}')
        ingressos_gratis_inteiros = quantidade_inteiros // 2
        ingressos_gratis_meios = quantidade_meios // 2
        total_ingressos = quantidade_inteiros + quantidade_meios + ingressos_gratis_meios + ingressos_gratis_inteiros
        if total_ingressos > ocupacao_salas[sala_escolhida]:
            print(f'numero de ingressos excede o numero de poltronas disponíveis'
                  f'({ocupacao_salas[sala_escolhida]} poltronas restantes).')
        else:
            ocupacao_salas[sala_escolhida] -= total_ingressos
            break
    desconto = dia_promocao["desconto"]
    if dia == "Monday":
        quantidade_inteiros_totais = quantidade_inteiros + ingressos_gratis_inteiros
        quantidade_meios_totais = quantidade_meios + ingressos_gratis_meios
        print(
            f"promocao segunda 2x1 aplicada: voce recebe {ingressos_gratis_inteiros} ingressos inteiros grátis e "
            f"{ingressos_gratis_meios} meio-ingressos grátis!")
    else:
        quantidade_inteiros_totais = quantidade_inteiros
        quantidade_meios_totais = quantidade_meios

    desconto = dia_promocao["desconto"]
    if dia == "Wednesday":
        desconto += 0.10
        print(
            "Bônus especial de quarta-feira do cliente : Desconto adicional de 10%")
    desconto = dia_promocao["desconto"]
    if total_ingressos > ocupacao_salas[sala_escolhida]:
        print('quantidade de ingressos excede o numero de poltronas disponiveis.')
    else:
        ocupacao_salas[sala_escolhida] -= total_ingressos
    desconto = dia_promocao["desconto"]
    nota_fiscal = open("\nresumo das compras", "w")
    nota_fiscal.write(f'nome: {nome}')
    nota_fiscal.write(f"sala: {sala_escolhida}")
    nota_fiscal.write(f'ingressos inteiros:{quantidade_inteiros}')
    nota_fiscal.write(f'ingressos meios:{quantidade_meios}')
    nota_fiscal.write(f"preco original do ingresso: R$ {sala_info['preco_ingresso_inteiros']:}")
    nota_fiscal.write(f"preco original do ingresso: R$ {sala_info['preco_ingresso_meios']}:")
    nota_fiscal.write(f'valor total: R${valor_total_ingressos}')
    nota_fiscal.close()



def menu_filmes():
        verificar = verificacao()
        if verificar:
            print('\033[97mfilmes em cartazes sao:')
            print('\033[91m1-homem ranha')
            print('2-vingadores')
            print('3-deadpool 3')
            print('0-menu do cliente\033[0;0m')
        else:
            print('erro!! codigo que voce digitou esta incorreto, tente novamente'
                  ', esta compra nao sera debitada')
            return menu_cliente()

def menu_comidas():
    print('\033[34m_______MENU DE COMIDAS________\033[0;0m')
    comidas = {'pipoca': 10, 'refri': 5}
    compras = []
    escolha_comida = []
    while True:
        opcao = validar_texto(
            'deseja comprar comida (C) ou se nao quiser comprar (N): ')
        if opcao.lower() == 'c':
            print('alimentos disponiveis: ')
            for comida, valor in comidas.items():
                print(comida, '- R$', valor)
            escolhac = validar_texto(
                'digite o nome do alimento que deseja comprar: ')
            escolha_comida.append(escolhac)
            if escolhac in comidas:
                qtde = validar_num('quantos: ')
                total = qtde * comidas[escolhac]
                print(escolhac, '- R$', total)
                compras.append(total)
                total_compra = 0
                for compra in compras:
                    total_compra += compra
                print('total da compra: R$', total_compra)
            else:
                print('comida nao disponivel')
        elif opcao.lower() == 'n':
            print('\033[93mseguindo para o filme...\033[0;0m')
            with open('../nota comida.txt', 'a') as nota_fiscal:
                nota_fiscal.write(f'comida escolhida: {escolhac}')
                nota_fiscal.write(f'total compra de comidas: R${total_compra}')
            break
        else:
            print('opcao invalida. por favor, escolha C ou N.')
            return menu_comidas()


def menu1():
    global filme, horario
    filme = 'homem aranha'
    horarios = ['13', '14', '15']
    print(f'Os horários disponíveis são: {(horarios)}')
    horario = validar_texto('que horario voce deseja: ')
    if horario in horarios:
        print(f'{filme} no horario das {horario} horas')
        menu_comidas()
    else:
        print('\033[31mdesculpe, nao temos esse horario disponivel.\033[0;0m')

def menu2():
    global filme, horario
    filme = 'vingadores'
    horarios = ['14', '16', '18']
    print(f'Os horários disponíveis são: {(horarios)}')
    horario = validar_texto('que horario voce deseja: ')
    if horario in horarios:
        print(f'{filme} no horario das {horario} horas')
        menu_comidas()
    else:
        print('\033[31mdesculpe, nao temos esse horario disponivel.\033[0;0m')



def menu3():
    global filme, horario
    filme = 'deadpool'
    horarios = ['15', '17', '19']
    print(f'Os horários disponíveis são: {(horarios)}')
    horario = validar_texto('que horario voce deseja: ')
    if horario in horarios:
        print(f'{filme} no horario das {horario} horas')
        menu_comidas()
    else:
        print('\033[31mdesculpe, nao temos esse horario disponivel.\033[0;0m')

def verificacao():
    campo = validar_num('digite seu codigo: ')
    if campo == codigo:
        return True
    return False
