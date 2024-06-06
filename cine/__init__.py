from babel.dates import format_date
from datetime import datetime


salas = {
    1: {
        "nome": "Sala 1 - 2D",
        "preco_ingresso_inteiro": 15.00,
        "preco_ingresso_meio": 7.50,
        "num_poltronas": 100,
        "opcoes": ["dublado", "legendado"]
    },
    2: {
        "nome": "Sala 2 - 3D",
        "preco_ingresso_inteiro": 20.00,
        "preco_ingresso_meio": 10.00,
        "num_poltronas": 80,
        "opcoes": ["dublado", "legendado"]
    },
    3: {
        "nome": "Sala 3 - IMAX",
        "preco_ingresso_inteiro": 25.00,
        "preco_ingresso_meio": 12.50,
        "num_poltronas": 60,
        "opcoes": ["dublado", "legendado"]
    }
}
promotions = {
    "terça-feira": {
        "nome": "Terça 2x1",
        "detalhes": ["Ingressos em dobro: Na compra de um ingresso, o segundo é gratuito."],
        "desconto": 0.0  # Sem desconto adicional
    },
    "quarta-feira": {
        "nome": "Quarta do Cliente Fiel",
        "detalhes": ["Desconto para membros: 50% de desconto no ingresso para clientes cadastrados.",
                     "Acumule pontos: Dobre os pontos de fidelidade para cada ingresso comprado."],
        "desconto": 0.50  # 50% de desconto para membros
    }
}
today = format_date(datetime.now(), 'EEEE', locale='pt_BR').lower()
today_promotion = promotions.get(today, {"nome": "Nenhuma promoção disponível", "detalhes": [""], "desconto": 0.0})
ocupacao_salas = {sala_id: sala_info["num_poltronas"] for sala_id, sala_info in salas.items()}
lista_compras = []
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
    print('0-sair\033[0;0m')

def exibir_salas(dict,nome):
    global sala_info, opcao_escolhida
    print(f"Promoção de hoje {today} : {today_promotion['nome']}")
    for detalhe in today_promotion['detalhes']:
        print(f"{detalhe}")
    print(f'\nSalas disponiveis:')
    for sala_id, sala_info in salas.items():
        poltronas_disponiveis = ocupacao_salas[sala_id]
        print(f'{sala_id} : {sala_info['nome']} - Preço do ingresso inteiro: R$ {sala_info['preco_ingresso_inteiro']}'
              f' - Preço do meio-ingresso: R$ {sala_info['preco_ingresso_meio']} '
              f'- Poltronas disponíveis: {poltronas_disponiveis}')
        for opcao in sala_info['opcoes']:
            print(f' - {opcao}')
    sala_escolhida = int(input("\nDigite o número da sala escolhida: "))
    if sala_escolhida in salas:
        sala_info = salas[sala_escolhida]
    else:
        print("Sala inválida. Por favor, escolha uma sala válida.")
        while True:
            opcao_escolhida = input("Você prefere assistir ao filme dublado ou legendado? ").lower()
            if opcao_escolhida in sala_info["opcoes"]:
                break
            else:
                print("Opção inválida. Por favor, escolha 'dublado' ou 'legendado'.")

    # Calcular o preço final do ingresso com desconto
    desconto = today_promotion["desconto"]
    if today == "quarta-feira" and dict:
        desconto += 0.10  # Bônus de 10% para clientes cadastrados nas quartas-feiras
        print("Bônus especial de quarta-feira aplicado para clientes cadastrados: Desconto adicional de 10%")

    preco_final_inteiro = sala_info["preco_ingresso_inteiro"] * (1 - desconto)
    preco_final_meio = sala_info["preco_ingresso_meio"] * (1 - desconto)

    # Solicitar a quantidade de ingressos inteiros e meio
    ingressos_gratis_inteiros = 0
    ingressos_gratis_meios = 0
    quantidade_inteiros = int(input("Digite a quantidade de ingressos inteiros: "))
    quantidade_meios = int(input("Digite a quantidade de meio-ingressos: "))
    for i in range(quantidade_inteiros):
        if quantidade_inteiros > 0 and quantidade_inteiros % 2 == 0:
            ingressos_gratis_inteiros += 1
    for i in range(quantidade_meios):
        if quantidade_meios > 0 and quantidade_meios % 2:
            ingressos_gratis_meios += 1
    # Aplicar a promoção "Terça 2x1" se hoje for terça-feira
    if today == "terça-feira":
        ingressos_gratis_inteiros = ingressos_gratis_inteiros # Para cada ingresso inteiro comprado, o cliente ganha um grátis
        ingressos_gratis_meios = ingressos_gratis_meios  # Para cada meio-ingresso comprado, o cliente ganha um grátis
        quantidade_inteiros_totais = quantidade_inteiros + ingressos_gratis_inteiros
        quantidade_meios_totais = quantidade_meios + ingressos_gratis_meios
        print(
            f"Promoção Terça 2x1 aplicada: Você recebe {ingressos_gratis_inteiros} "
            f"ingressos inteiros grátis e {ingressos_gratis_meios} meio-ingressos grátis!")
    else:
        quantidade_inteiros_totais = quantidade_inteiros
        quantidade_meios_totais = quantidade_meios

    # Verificar disponibilidade de poltronas
    total_ingressos = quantidade_inteiros_totais + quantidade_meios_totais
    if total_ingressos > ocupacao_salas[sala_escolhida]:
        print("Quantidade de ingressos excede o número de poltronas disponíveis.")
    else:
        # Atualizar a ocupação das poltronas
        ocupacao_salas[sala_escolhida] -= total_ingressos
    compra = {
        "cliente": nome,
        "sala": sala_escolhida,
        "opcao": opcao_escolhida,
        "quantidade_inteiros": quantidade_inteiros,
        "quantidade_meios": quantidade_meios,
        "preco_total": (quantidade_inteiros * preco_final_inteiro) + (quantidade_meios * preco_final_meio)
    }
    lista_compras.append(compra)

    # Calcular o valor total
    valor_total_inteiros = quantidade_inteiros * preco_final_inteiro
    valor_total_meios = quantidade_meios * preco_final_meio
    valor_total = valor_total_inteiros + valor_total_meios

    # Cria o arquivo .TXT
    nota_fiscal = open("resumo das compras", "w")
    nota_fiscal.write(f"nome: {nome}\n")
    nota_fiscal.write(f"sala: {sala_escolhida}\n")
    nota_fiscal.write(f"tipo de filme: {opcao_escolhida}\n")
    nota_fiscal.write(f"quantidade de inteiros: {quantidade_inteiros}\n")
    nota_fiscal.write(f"quantidade de meios: {quantidade_meios}\n")
    nota_fiscal.write(f"valor total da compra: {valor_total}\n")
    nota_fiscal.close()
    print('Nota fiscal gerada com sucesso!!')