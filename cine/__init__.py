from datetime import datetime

promocao = {
    'Monday': {
        'nome': 'terça 2x1',
        'detalhes': ['ingressos em dobro: na compra de um ingresso, o segundo é gratuito.'],
        'desconto': 0.50},

    'Wednesday': {
        'nome': 'quarta do cliente fiel',
        'detalhes': [
            'desconto para membros: 50% de desconto no ingresso para clientes cadastrados.', ],
        'desconto': 0.50},

    }

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

ocupacao_salas = {sala_id: sala_info["num_poltronas"] for sala_id, sala_info in salas.items()}
lista_compras = []
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
    global quantidade_inteiros , quantidade_meios, preco_desconto_inteiro, preco_desconto_meio, sala_escolhida, opcao_escolhida, sala_info
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

        preco_desconto_inteiro = sala_info['preco_ingresso_inteiros'] * (1 - dia_promocao['desconto'])
        preco_desconto_meio = sala_info['preco_ingresso_meios'] * (1 - dia_promocao['desconto'])
    while True:
        quantidade_inteiros = validar_num('digite a quantidade de ingressos inteiros: ')
        quantidade_meios = validar_num('digite a quantidade de meio-ingressos: ')
        ingressos_gratis_inteiros = quantidade_inteiros // 2
        ingressos_gratis_meios = quantidade_meios // 2
        total_ingressos = quantidade_inteiros + quantidade_meios + ingressos_gratis_meios + ingressos_gratis_inteiros
        if total_ingressos > ocupacao_salas[sala_escolhida]:
            print(f'numero de ingressos excede o numero de poltronas disponíveis'
                  f'({ocupacao_salas[sala_escolhida]} poltronas restantes).')
        else:
            ocupacao_salas[sala_escolhida] -= total_ingressos
            break
    ingresso_comp = quantidade_inteiros + quantidade_meios
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
    if dia == "quarta":
        desconto += 0.10
        print(
            "Bônus especial de quarta-feira aplicado para clientes fieis: Desconto adicional de 10%")

    desconto = dia_promocao["desconto"]

    if total_ingressos > ocupacao_salas[sala_escolhida]:
        print('quantidade de ingressos excede o numero de poltronas disponiveis.')
    else:
        ocupacao_salas[sala_escolhida] -= total_ingressos
    desconto = dia_promocao["desconto"]
    if dia == "quarta":
        desconto += 0.10
        print(
            "Bônus especial de quarta-feira aplicado para clientes fieis: Desconto adicional de 10%")
def menu_filmes():
        print('\033[97mfilmes em cartazes sao:')
        print('\033[91m1-homem ranha')
        print('2-vingadores')
        print('3-deadpool 3')
        print('0-menu do cliente\033[0;0m')


def menu_comidas():
    print('\033[34m_______MENU DE COMIDAS________\033[0;0m')
    comidas = {'pipoca': 10, 'refri': 5}
    compras = []
    total = 0
    opcao = validar_texto(
        'deseja comprar comida (C) ou nao quiser comprar (N): ')

    if opcao == 'C' or opcao == 'c':
        global escolhac, total_compra
        print('alimentos disponiveis: ')
        for comida, valor in comidas.items():
            print(comida, '- R$', valor)
        pergunta = validar_texto('deseja comprar mais de uma comida (sim) ou (nao)')
        if pergunta == 'sim':
            repete = validar_num('quantas comidas vc deseja comprar? ')
            for i in range(repete):
                escolhac = validar_texto('digite o nome do alimento que deseja comprar: ')
                qtde = validar_num('quantos(as): ')
                if escolhac in comidas:
                    total = qtde * valor
                else:
                    print('comida nao disponivel')
            for comida in comidas:
                compras.append(comidas)
            for compra in compras:
                total_compra = total
            print('total da compra:', 'R$', total_compra)
            print('\033[93mseguiu ao filme...\033[0;0m')
        elif pergunta == 'nao':
            print('alimentos disponiveis: ')
            for comida, valor in comidas.items():
                print(comida, '- R$', valor)
                escolhac = validar_texto('digite o nome do alimento que deseja comprar: ')
                qtde = validar_num('quantos(as): ')
                if escolhac in comidas:
                    total = qtde * valor
                else:
                    print('comida nao disponivel')
            for comida in comidas:
                compras.append(comidas)
            for compra in compras:
                total_compra = total
            print('total da compra:', 'R$', total_compra)
            print('\033[93mseguiu ao filme...\033[0;0m')

    if opcao == 'N' or opcao == 'n':
        qtde = 0
        valor = 0
        total = qtde * valor
        total_compra = total
        escolhac = print('\033[93mseguiu ao filme...\033[0;0m')



def menu1():
    global filme1
    filme1 = 'homem aranha'
    horarios = ['13', '14', '15']
    print(f'Os horários disponíveis são: {(horarios)}')
    horario = validar_texto('que horario voce deseja: ')
    if horario in horarios:
        print(f'{filme1} no horario das {horario} horas')
        return menu_comidas()
    else:
        print('\033[31mdesculpe, nao temos esse horario disponivel.\033[0;0m')

def menu2():
    global filme2
    filme2 = 'vingadores'
    horarios = ['14', '16', '18']
    print(f'Os horários disponíveis são: {(horarios)}')
    horario = validar_texto('que horario voce deseja: ')
    if horario in horarios:
        print(f'{filme2} no horario das {horario} horas')
        return menu_comidas()
    else:
        print('\033[31mdesculpe, nao temos esse horario disponivel.\033[0;0m')


def menu3():
    global filme3
    filme3 = 'deadpool'
    horarios = ['15', '17', '19']
    print(f'Os horários disponíveis são: {(horarios)}')
    horario = validar_texto('que horario voce deseja: ')
    if horario in horarios:
        print(f'{filme3} no horario das {horario} horas')
        return menu_comidas()
    else:
        print('\033[31mdesculpe, nao temos esse horario disponivel.\033[0;0m')



def pedidos_clientes(dict, dict2):
    valor_total_sala = quantidade_inteiros * preco_desconto_inteiro + quantidade_meios * preco_desconto_meio
    valor_total = quantidade_inteiros * preco_desconto_inteiro + quantidade_meios * preco_desconto_meio + total_compra

    nota_fiscal = open("resumo das compras", "w")
    nota_fiscal.write(f"nome: {nome}\n")  # nome do cliente que esta comprando
    nota_fiscal.write(f"sala: {sala_escolhida}\n")  # numero da sala
    nota_fiscal.write(f"tipo de filme: {opcao_escolhida}\n")  # dublado ou legendado
    nota_fiscal.write(f"quantidade de inteiros: {quantidade_inteiros}\n")
    nota_fiscal.write(f"quantidade de meios: {quantidade_meios}\n")
    nota_fiscal.write(f"valor total da compra: {valor_total}\n")
    nota_fiscal.close()
