import cine
usuarios = {'joseph': ['joseph', 2, 'zep'],}
filmes = ['vingadores', 'homem aranha', 'deadpool']
opmenu = 99
while (opmenu != 0):
    cine.menu_main()
    opmenu = int(input('digite a opçao que deseja: \033[0;0m'))
    if (opmenu == 1):
        login = input('digite seu loguin')
        senha = input('digite sua senha')
        logado = cine.log_usuario(login, senha, usuarios, 2)
        if(logado):
            opfilme = 99
            while(opfilme != 0):
                cine.menu_adm()
                opfilme = int(input('\033[36mdigite a opçao que deseja: \033[0;0m'))
                if (opfilme == 1):
                    cine.add_cliente(usuarios)
                elif (opfilme == 2):
                    cine.adicionar_film(filmes)
                elif (opfilme == 3):
                    cine.listar_para(filmes)
                    busca_filme = int(input('digite o indice do filme que voce quer atualizar: '))
                    att_mudanca = input('digite a mudança que voce quer fazer no filme: ')
                    filmes[busca_filme] = att_mudanca
                    print('alteraçao feita com sucesso')
                elif (opfilme == 4):
                    cine.listar_para(filmes)
                    ind_rem = int(input('digite o codigo do filme para remover: '))
                    filmes.pop(ind_rem)
                    print('O filme foi excluido com sucesso!!')
                elif (opfilme == 5):
                    cine.listar_para(filmes)
                    busca_mostrar = int(input('digite o indice do filme que voce esta buscando: '))
                    print(f'o nome filme que voce esta procurando é {filmes[busca_mostrar]}')
                elif (opfilme == 6):
                    print(filmes)
                elif (opfilme == 0):
                    print('saindo...')
                    break
                elif(opfilme > 6):
                    print('escolha um numero inteiro valido!!')
        else:
            print('nome de adm ou senha invalidas')
    elif (opmenu == 2):
        cine.cadastrar_cliente(usuarios)
    elif (opmenu == 3):
        login = input('digite seu loguin')
        senha = input('digite sua senha')
        logado_cl = cine.log_usuario(login, senha, usuarios, 1)
        if(logado_cl):
            opcliente = 99
            while (opcliente != 0):
                cine.menu_cliente()
                opcliente = int(input('\033[34mdigite a opcao desejada: \033[0;0m'))
                if (opcliente == 0):
                    print('\033[91mobrigado por nos visitar, tenha um otimo dia!\033[0;0')
                    break
                elif (opcliente == 1):
                    opingresso = 99
                    while (opingresso != 0):
                        cine.menu_salas()
                        opingresso = int(input('qual opcao voce deseja: '))
                        if (opingresso == 1):
                            cine.compra_ingresso1()
                        elif (opingresso == 2):
                            cine.compra_ingresso2()
                        elif (opingresso == 3):
                            cine.compra_ingresso3()
                        elif (opingresso == 0):
                            break

                elif (opcliente == 2):
                    opescolha = 99
                    while (opescolha != 0):
                        cine.filmes_cartaz()
                        opescolha = int(input('digite a opcao: \033[0;0m'))

                        if (opescolha == 0):
                            print('segindo ao menu do cliente..')
                            break
                        elif (opescolha == 1):
                            cine.filme_1()
                        elif (opescolha == 2):
                            cine.filme_2()
                        elif (opescolha == 3):
                            cine.filme_3()
print('chronos gay')