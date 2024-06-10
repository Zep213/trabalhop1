from babel.dates import format_date
from datetime import datetime

promocao = {
    'Monday': {
        'nome': 'segunda normalizada', 'detalhes': ['sem desconto.'], 'desconto': 0.0},

    'Tuesday': {
        'nome': 'terça 2x1',
        'detalhes': ['ingressos em dobro: na compra de um ingresso, o segundo é gratuito.'],
        'desconto': 0.50},

    'Wednesday': {
        'nome': 'quarta do cliente fiel',
        'detalhes': [
            'desconto para membros: 50% de desconto no ingresso para clientes cadastrados.', ],
        'desconto': 0.50},

    'Thursday': {
        'nome': 'quinta normalizada', 'detalhes': ['sem desconto.'], 'desconto': 0.0},

    'Friday': {
        'nome': 'sexta da promocao',
        'detalhes': ['desconto em todos os ingressos para filmes lancados de hoje.'],
        'desconto': 0.10},

    'Saturday': {
        'nome': 'sabado familia',
        'detalhes': [
            'desconto para familias: ingressos com preco especial para grupos de quatro ou mais pessoas.'],
        'desconto': 0.20},

    'Sunday': {
        'nome': 'domingo normalizado', 'detalhes': ['sem desconto.'], 'desconto': 0.0}}

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
    for indices_att in list:
        print(f'{list.index(indices_att)} - {indices_att}')


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
    print('0-sair\033[0;0m')


def menu_main():
    print('\033[34m________MENU________\033[0;0m')
    print('\033[96m1-login adm')
    print('2-adicionar cliente')
    print('3-login cliente')
    print('0- sair')


def cadastrar_cliente(dict):
    nome = validar_texto('digite seu nome')
    login = validar_texto('digite seu login')
    senha = validar_texto('digite sua senha')
    dict[login] = [nome, 1, senha]
    print('Cadastro realizado com sucesso!!!\n')


def menu_cliente():
    print('\033[34m________MENU CLIENTE________\033[0;0m')
    print('\033[96m1-compra de ingressos')
    print('\0332-filmes em cartazes/horarios')
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
    for sala_id, sala_info in salas.items():
        poltronas_disponiveis = ocupacao_salas[sala_id]
        print(
            f"{sala_id}: {sala_info['nome']} - Preço do ingresso inteiro: R$ {sala_info['preco_ingresso_inteiros']} - Preço do meio-ingresso: R$ {sala_info['preco_ingresso_meios']} - Poltronas disponíveis: {poltronas_disponiveis}")
        print('opcoes de exibicao:')
        for opcao in sala_info["opcoes"]:
            print(f"- {opcao}")


def escolher_sala():
    global preco_desconto_meio, preco_desconto_inteiro
    mostrar_salas()
    while True:
        sala_escolhida = validar_num('\ndigite o numero da sala escolhida: ')
        if sala_escolhida in salas:
            sala_info = salas[sala_escolhida]
            break
        else:
            print('sala invalida. por favor, escolha uma sala valida.')
    while True:
        opcao_escolhida = input("voce prefere assistir ao filme dublado ou legendado: ").lower()
        print(f"opcao escolhida: {opcao_escolhida}, opcoes disponiveis: {sala_info['opcoes']}")
        if opcao_escolhida in sala_info["opcoes"]:
            break
        else:
            print("opcao invalida, por favor, escolha 'dublado' ou 'legendado'.")

        preco_desconto_inteiro = sala_info['preco_ingresso_inteiros'] * (1 - dia_promocao['desconto'])
        preco_desconto_meio = sala_info['preco_ingresso_meios'] * (1 - dia_promocao['desconto'])
    while True:
        quantidade_inteiros = validar_num('digite a quantidade de ingressos inteiros: ')
        quantidade_meios = validar_num('digite a quantidade de meio-ingressos: ')
        total_ingressos = quantidade_inteiros + quantidade_meios
        if total_ingressos > ocupacao_salas[sala_escolhida]:
            print(f'numero de ingressos excede o numero de poltronas disponíveis'
                  f'({ocupacao_salas[sala_escolhida]} poltronas restantes).')
        else:
            ocupacao_salas[sala_escolhida] -= total_ingressos
            break
    ingresso_comp = quantidade_inteiros + quantidade_meios
    desconto = dia_promocao["desconto"]
    if dia == "terca":
        ingressos_gratis_inteiros = quantidade_inteiros
        ingressos_gratis_meios = quantidade_meios
        quantidade_inteiros_totais = quantidade_inteiros + ingressos_gratis_inteiros
        quantidade_meios_totais = quantidade_meios + ingressos_gratis_meios
        print(
            f"promocao terça 2x1 aplicada: voce recebe {ingressos_gratis_inteiros} ingressos inteiros grátis e {ingressos_gratis_meios} meio-ingressos grátis!")
    else:
        quantidade_inteiros_totais = quantidade_inteiros
        quantidade_meios_totais = quantidade_meios

    desconto = dia_promocao["desconto"]
    if dia == "quarta":
        desconto += 0.10
        print(
            "Bônus especial de quarta-feira aplicado para clientes fieis: Desconto adicional de 10%")

    desconto = dia_promocao["desconto"]

    total_ingressos = preco_desconto_inteiro + preco_desconto_meio
    if total_ingressos > ocupacao_salas[sala_escolhida]:
        print('quantidade de ingressos excede o numero de poltronas disponiveis.')
    else:
        ocupacao_salas[sala_escolhida] -= total_ingressos
