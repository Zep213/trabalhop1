import cine
from datetime import datetime
promocao = {
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
dia = datetime.now().strftime("%A")#arrumar essa parte
dia_promocao = promocao.get(dia, {"nome": "nenhuma promocao disponivel", "detalhes": [""],
"desconto": 0.0})
ocupacao_salas = {sala_id: sala_info["num_poltronas"] for sala_id, sala_info in salas.items()}
lista_compras = []
usuarios = {'joseph': ['joseph', 2, 'zep'],'kaue': ['kaka', 2, 'kaka1']}
filmes = ['vingadores', 'homem aranha', 'deadpool']
opmenu = 99
while opmenu != 0:
    cine.menu_main()
    opmenu = cine.validar_num('digite a opçao que deseja: \033[0;0m')
    if opmenu == 1:
        login = cine.validar_texto('digite seu loguin: ')
        senha = cine.validar_texto('digite sua senha: ')
        logado = cine.log_usuario(login, senha, usuarios, 2)
        if logado:
            opadm = 99
            while opadm != 0:
                cine.menu_adm()
                opadm = cine.validar_num('\033[36mdigite a opçao que deseja: \033[0;0m')
                if opadm == 1:
                    cine.cadastrar_cliente(usuarios)
                elif opadm == 2:
                    cine.adicionar_film(filmes)
                elif opadm == 3:
                    cine.listar_para(filmes)
                    busca_filme = cine.validar_num('digite o indice do filme que voce quer atualizar: ')
                    att_mudanca = cine.validar_texto('digite a mudança que voce quer fazer no filme: ')
                    filmes[busca_filme] = att_mudanca
                    print('alteraçao feita com sucesso')
                elif opadm == 4:
                    cine.listar_para(filmes)
                    ind_rem = cine.validar_num('digite o codigo do filme para remover: ')
                    filmes.pop(ind_rem)
                    print('O filme foi excluido com sucesso!!')
                elif opadm == 5:
                    cine.listar_para(filmes)
                    busca_mostrar = cine.validar_num('digite o indice do filme que voce esta buscando: ')
                    print(f'o nome filme que voce esta procurando é {filmes[busca_mostrar]}')
                elif opadm == 6:
                    print(filmes)
                elif opadm == 7:
                    print(promocao)
                elif opadm == 8:
                    cine.pedidos_clientes()
                elif opadm == 9:
                    filmes_breve = ['veloses furiosos', 'tarzan', 'umanji', 'toy story' ,'era do gelo']
                    print('filmes que vao ser adicionados em breve no nosso catalago:')
                    print(filmes_breve)
                elif opadm == 0:
                    print('saindo...')
                    break
                elif opadm > 10:
                    print('escolha um numero inteiro valido!!')
        else:
            print('nome de adm ou senha invalidas')
    elif opmenu == 2:
        cine.cadastrar_cliente(usuarios)
    elif opmenu == 3:
        login = cine.validar_texto('digite seu loguin: ')
        senha = cine.validar_texto('digite sua senha: ')
        logado_cl = cine.log_usuario(login, senha, usuarios, 1)
        if logado_cl:
            opcliente = 99
            while opcliente != 0:
                cine.menu_cliente()
                opcliente = cine.validar_num('\033[34mdigite a opcao desejada: \033[0;0m')
                if opcliente == 0:
                    print('\033[91mobrigado por nos visitar, tenha um otimo dia! \033[0;0')
                    break
                elif opcliente == 1:
                    cine.escolher_sala()
                elif opcliente == 2:
                    opfilme = 99
                    while opfilme != 0:
                        cine.menu_filmes()
                        opfilme = cine.validar_num('digite o numero do filme que voce deseja assistir: ')
                        if opfilme == 0:
                            print('voltando ao menu do cliente...')
                        elif opfilme == 1:
                            cine.menu1()

                        elif opfilme == 2:
                            cine.menu2()

                        elif opfilme == 3:
                            cine.menu3()

        else:
            print('erro!!nome ou senha invalidos')
    elif opmenu == 0:
        print('tenha um bom dia...')
        break
