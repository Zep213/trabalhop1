from datetime import datetime

clientes = {}
admins = {'kaka': 'kaka1', 'joseph': 'zep'}
qntdcliente = 0
qntdadm = 0

while True:
    print('\033[34m________MENU________\033[0;0m')
    print('\033[96m1-adicionar cliente')
    print('2-login cliente')
    print('3-login adm')
    print('0- sair')
    opmenu = int(input('digite a opçao que deseja: \033[0;0m'))

    if (opmenu == 0):
        print('saindo...')
        break

    elif (opmenu == 1):
        nome = input('\033[97mdigite o nome de usuario: \033[0;0m').strip()
        if not nome:
            print('\033[31merro: nome de cliente vazio.\033[0;0m')
            continue
        elif nome in clientes:
            print('\033[31mnome de usuario ja existe. tente novamente.\033[0;0m')
        else:
            senha = input('\033[97mdigite a senha: \033[0;0m').strip()
            if not senha:
                print('\033[31merro: senha de cliente vazio.\033[0;0m')
                continue
            else:
                clientes[nome] = senha
                print('\033[92mcliente cadastrado com sucesso!!\033[0;0m')

    elif (opmenu == 2):
        nome = input('\033[97mdigite o nome de usuario: \033[0;0m').strip()
        if not nome:
            print('\033[31merro: nome de cliente vazio.\033[0;0m')
        elif nome not in clientes:
            print('\033[31mnome de usuário nao encontrado.\033[0;0m')
        senha = input('\033[97mdigite a senha: \033[0;0m').strip()
        if not senha:
            print('\033[31merro: senha de cliente vazio.\033[0;0m')
            continue
        elif clientes[nome] == senha:
            print('\033[92mlogin feito com sucesso! bem vindo ao nosso cinema\033[0;0m', nome)
            print('\033[92mpagina exclusiva para clientes\033[0;0m')

            op = 99
            while (op != 0):
                print('\033[34m________MENU CLIENTE________\033[0;0m')
                print('\033[96m1-compra de ingressos')
                print('2-filmes em cartazes/horarios')
                print('0-sair\033[0;0m')
                op = int(input('\033[34mdigite a opcao desejada: \033[0;0m'))

                if (op == 0):
                    print('\033[91mobrigado por nos visitar, tenha um otimo dia!\033[0;0m')
                    break

                elif (op == 1):
                    op = 99
                    while (op != 0):
                        print('\033[34m________MENU DA SALA________\033[0;0m')
                        print('\033[92m1-compra de ingressos/salas\033[0;0m')
                        print('\033[97m0-menu do cliente\033[0;0m')
                        op = int(input('\033[97mqual opcao voce deseja: '))

                        if (op == 1):
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

                            while True:
                                sala_escolhida = int(input('\ndigite o numero da sala escolhida: '))
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
                                quantidade_inteiros = int(input('digite a quantidade de ingressos inteiros: '))
                                quantidade_meios = int(input('digite a quantidade de meio-ingressos: '))
                                total_ingressos = quantidade_inteiros + quantidade_meios
                                if total_ingressos > ocupacao_salas[sala_escolhida]:
                                    print(f'numero de ingressos excede o numero de poltronas disponíveis'
                                          f'({ocupacao_salas[sala_escolhida]} poltronas restantes).')
                                else:
                                    ocupacao_salas[sala_escolhida] -= total_ingressos
                                    break
                            ingresso_comp = quantidade_inteiros + quantidade_meios

                            desconto = dia_promocao["desconto"]
                            if dia == "Monday":
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
                            if dia == "quarta" and clientes:
                                desconto += 0.10
                                print(
                                    "Bônus especial de quarta-feira aplicado para clientes fieis: Desconto adicional de 10%")

                            desconto = dia_promocao["desconto"]
                            if dia == "sexta" and clientes:
                                desconto += 0.10
                                print(
                                    "Bônus especial de quarta-feira aplicado para clientes fieis: Desconto adicional de 10%")

                            total_ingressos = preco_desconto_inteiro + preco_desconto_meio
                            if total_ingressos > ocupacao_salas[sala_escolhida]:
                                print('quantidade de ingressos excede o numero de poltronas disponiveis.')
                            else:
                                ocupacao_salas[sala_escolhida] -= total_ingressos

                        elif (op == 0):
                            op = 99
                            while (op != 0):
                                print('\033[34m________MENU CLIENTE________\033[0;0m')
                                print('\033[96m1-compra de ingressos')
                                print('2-filmes em cartazes/horarios')
                                print('0-sair\033[0;0m')
                                op = int(input('\033[34mdigite a opcao desejada: \033[0;0m'))

                                if (op == 0):
                                    print('\033[91mobrigado por nos visitar tenha um otimo dia\033[0;0m')
                                    break

                                elif (op == 2):
                                    while (op != 0):
                                        print('\033[97mfilmes em cartazes sao:')
                                        print('\033[91m1-homem ranha')
                                        print('2-vingadores')
                                        print('3-deadpool 3')
                                        print('0-menu do cliente\033[0;0m')
                                        opescolha = int(input('digite a opcao: \033[0;0m'))

                                        if (opescolha == 0):
                                            print('voltando ao menu do cliente..')
                                            break

                                        elif (opescolha == 1):
                                            filme = 'homem aranha'
                                            horarios = ['13', '14', '15']
                                            print(f'Os horários disponíveis são: {(horarios)}')
                                            horario = input('que horario voce deseja: ').strip()
                                            if horario in horarios:
                                                print(f'{filme} no horario das {horario} horas')
                                            else:
                                                print('\033[31mdesculpe, nao temos esse horario disponivel.\033[0;0m')
                                                continue

                                            print('\033[34m_______MENU DE COMIDAS________\033[0;0m')
                                            comidas = {'pipoca': 10,'refri': 5}
                                            compras = []
                                            print('bem-vindo', nome)
                                            opcao = input(
                                                'deseja comprar comida (C) ou nao quiser comprar (N): ').strip()

                                            if opcao == 'C' or opcao == 'c':
                                                print('alimentos disponiveis: ')
                                                for comida, valor in comidas.items():
                                                    print(comida, '- R$', valor)
                                                escolhac = input('digite o nome do alimento que deseja comprar: ').strip()
                                                qtde = int(input('quantos: '))
                                                if escolhac in comidas:
                                                    total = qtde * valor
                                                    print(escolhac, '- R$', total)
                                                    for comida in comidas:
                                                        compras.append(comidas)
                                                    for compra in compras:
                                                        total_compra = total
                                                    print('total da compra:', 'R$', total_compra)
                                                    print('\033[93mseguiu ao filme...\033[0;0m')
                                                    break
                                                else:
                                                    print('comida nao disponivel')

                                            if opcao == 'N' or opcao == 'n':
                                                qtde = 0
                                                valor = 0
                                                total = qtde * valor
                                                total_compra = total
                                                escolhac = print('\033[93mseguiu ao filme...\033[0;0m')
                                                break

                                        elif (opescolha == 2):
                                            filme = 'vingadores'
                                            horarios = ['14', '16', '18']
                                            print(f'Os horários disponíveis são: {(horarios)}')
                                            horario = input('que horario voce deseja: ').strip()
                                            if horario in horarios:
                                                print(f'{filme} no horario das {horario} horas')
                                            else:
                                                print('\033[31mdesculpe, nao temos esse horario disponivel.\033[0;0m')
                                                continue

                                            print('\033[34m_______MENU DE COMIDAS________\033[0;0m')
                                            comidas = {'pipoca': 10, 'refri': 5}
                                            compras = []
                                            print('bem-vindo', nome)
                                            opcao = input(
                                                'deseja comprar comida(C) ou nao quiser comprar(N): ').strip()

                                            if opcao == 'C' or opcao == 'c':
                                                print('alimentos disponiveis: ')
                                                for comida, valor in comidas.items():
                                                    print(comida, '- R$', valor)
                                                escolhac = input('digite o nome do alimento que deseja comprar: ').strip()
                                                qtde = int(input('quantos: '))
                                                if escolhac in comidas:
                                                    total = qtde * valor
                                                    print(escolhac, '- R$', total)
                                                    for comida in comidas:
                                                        compras.append(comidas)
                                                    for compra in compras:
                                                        total_compra = total
                                                    print('total da compra:', 'R$', total_compra)
                                                    print('\033[93mseguiu ao filme...\033[0;0m')
                                                    break
                                                else:
                                                    print('comida nao disponivel')

                                            if opcao == 'N' or opcao == 'n':
                                                qtde = 0
                                                valor = 0
                                                total = qtde * valor
                                                total_compra = total
                                                escolhac = print('\033[93mseguiu ao filme...\033[0;0m')
                                                break


                                        elif (opescolha == 3):
                                            filme = 'deadpool'
                                            horarios = ['15', '17', '19']
                                            print(f'Os horários disponíveis são: {(horarios)}')
                                            horario = input('que horario voce deseja: ').strip()
                                            if horario in horarios:
                                                print(f'{filme} no horario das {horario} horas')
                                            else:
                                                print('\033[31mdesculpe, nao temos esse horario disponivel.\033[0;0m')
                                                continue

                                            print('\033[34m_______MENU DE COMIDAS________\033[0;0m')
                                            comidas = {'pipoca': 10, 'refri': 5}
                                            compras = []
                                            print('bem-vindo', nome)
                                            opcao = input(
                                                'deseja comprar comida (C)ou nao quiser comprar(N): ').strip()

                                            if opcao == 'C' or opcao == 'c':
                                                print('alimentos disponiveis: ')
                                                for comida, valor in comidas.items():
                                                    print(comida, '- R$', valor)
                                                escolhac = input('digite o nome do alimento que deseja comprar: ').strip()
                                                qtde = int(input('quantos: '))
                                                if escolhac in comidas:
                                                    total = qtde * valor
                                                    print(escolhac, '- R$', total)
                                                    for comida in comidas:
                                                        compras.append(comidas)
                                                    for compra in compras:
                                                        total_compra = total
                                                    print('total da compra:', 'R$', total_compra)
                                                    print('\033[93mseguiu ao filme...\033[0;0m')
                                                    break
                                                else:
                                                    print('comida nao disponivel')

                                            if opcao == 'N' or opcao == 'n':
                                                qtde = 0
                                                valor = 0
                                                total = qtde * valor
                                                total_compra = total
                                                escolhac = print('\033[93mseguiu ao filme...\033[0;0m')
                                                break

    if (opmenu == 3):
        adm = input('digite seu nome de adm: ').strip()
        if not adm:
            print('\033[31merro: nome de adm vazio.\033[0;0m')
            continue
        adm_senha = input('digite sua senha de adm: ').strip()
        if not adm_senha:
            print('\033[31merro: senha de adm vazio.\033[0;0m')
            continue

        if adm in admins and admins[adm] == adm_senha:
            print(f'bem vindo {adm}!!')
            print('pagina exclusiva para adm')
            filmes = ['vingadores', 'homem aranha', 'deadpool']

            opfilme = 99
            while (opfilme != 0):
                print('\033[34m________MENU ADM________\033[0;0m')
                print('\033[35m1-adicionar adm')
                print('2-adicionar filme')
                print('3-atualizar filme')
                print('4-excluir filme')
                print('5-buscar filme')
                print('6-lista dos filmes adicionados')
                print('7- liberacao ao filme')
                print('8-ofertas da semana')
                print('9-pedidos do clientes')
                print('0-sair\033[0;0m')
                opfilme = int(input('\033[36mdigite a opçao que deseja: \033[0;0m'))

                if (opfilme == 1):

                    while True:
                        adm_novo = input('digite seu nome: ').strip()
                        if not adm_novo:
                            print('\033[31merro: nome de adm vazio.\033[0;0m')
                            continue
                        if adm_novo in admins:
                            print('usuario ja existente, escolha outro nome e senha')
                            continue
                        else:
                            adm_senha_novo = input('digite sua senha: ').strip()
                            if not adm_senha_novo:
                                print('\033[31merro: senha de adm vazio.\033[0;0m')
                                continue
                            admins[adm_novo] = adm_senha_novo
                            print('\033[32m novo administrador cadastrado com sucesso!!\033[0;0m')
                            qntdadm += 1
                        break

                elif (opfilme == 2):
                    qntd_filmes = int(input('quantos filmes voce quer adicionar? '))
                    for qntdf in range(qntd_filmes):
                        nome_filme = input('digite o nome do filme que deseja adicionar: ').strip()
                        if not nome_filme:
                            print('\033[31merro: nome de filme adicionado vazio.\033[0;0m')
                            continue

                        filmes.append(nome_filme)
                        print(f'{len(filmes)} filme(s) foram adicionados!!')

                elif (opfilme == 3):
                    for indices in filmes:
                        print(f'{filmes.index(indices)} - {indices}')
                    busca_filme = int(input('digite o indice do filme que voce quer atualizar: '))
                    att_mudanca = input('digite a mudança que voce quer fazer no filme: ')
                    filmes[busca_filme] = att_mudanca
                    print('alteraçao feita com sucesso')

                elif (opfilme == 4):
                    for indices_exc in filmes:
                        print(f'{filmes.index(indices_exc)} - {indices_exc}')
                    ind_rem = int(input('digite o codigo do filme para remover: '))
                    filmes.pop(ind_rem)
                    if (ind_rem in filmes):
                        filmes.pop(ind_rem)
                    print('O filme foi excluido com sucesso!!')

                elif (opfilme == 5):
                    for indices_busc in filmes:
                        print(f'{filmes.index(indices_busc)} - {indices_busc}')
                    busca_mostrar = int(input('digite o indice do filme que voce esta buscando: '))
                    if busca_mostrar in range(len(filmes)):
                        print(f'o nome filme que voce esta procurando é {filmes[busca_mostrar]}')

                elif (opfilme == 6):
                    print(filmes)

                elif (opfilme == 7):
                    print('pode passar ao filme')
                    ingressos_clientes = print(f'o senhor tem {ingresso_comp}')


                elif (opfilme == 8):
                    promocao = {'Monday': {
                    'nome': 'segunda normalizada',
                    'detalhes': ['sem desconto.'], 'desconto': 0.0},

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

                    dia = datetime.now().strftime("%A")
                    dia_promocao = promocao.get(dia, {"nome": "nenhuma promocao disponivel", "detalhes": [""],
                                                      "desconto": 0.0})

                    print(f"promocao de hoje ({dia}): {dia_promocao['nome']}")
                    for detalhe in dia_promocao['detalhes']:
                        print(f"- {detalhe}")

                elif (opfilme == 9):
                    valor_total_sala = {quantidade_inteiros * preco_desconto_inteiro + quantidade_meios * preco_desconto_meio}
                    valor_total = {quantidade_inteiros * preco_desconto_inteiro + quantidade_meios * preco_desconto_meio + total_compra}

                    print("\nresumo das compras:")
                    print(f'nome: {nome}')
                    print(f"sala: {sala_escolhida}")
                    print(f'ingressos inteiros:{quantidade_inteiros}')
                    print(f'ingressos meios:{quantidade_meios}')
                    print(f"preco original do ingresso: R$ {sala_info['preco_ingresso_inteiros']:}")
                    print(f"preco original do ingresso: R$ {sala_info['preco_ingresso_meios']}:")
                    print(f'preco com desconto: R$ {preco_desconto_inteiro}')
                    print(f'preco com desconto: R$ {preco_desconto_meio}')
                    print(f'valor total: R${valor_total_sala}')
                    print(f'filme: {filme}')
                    print(f'horario da: {horario} horas')
                    print(f'comida escolhida: {escolhac}')
                    print(f'total compra de comidas: R${total_compra}')
                    print(f'valor total: R${valor_total}')

                elif (opfilme == 0):
                    print('saindo...')
                    break
        else:
            print('nome de adm ou senha invalidas')