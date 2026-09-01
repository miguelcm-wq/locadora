from jogo import cadastrar_jogo, plataformas

while(True):
    menu = int(input('\n(1) - Jogo\n(2) - Cliente\n(3) - Locações\n(4) - sair\n Digite: '))

    if (menu == 1):
        while(True):
                menu_jogo = int(input('\n(1) - cadastrar\n(2) - listar\n(3) - sair\n Digite: '))
        
                if (menu_jogo == 1):
                    titulo = input('\nDigite o ttulo do jogo: ')
                    genero = input('Digite o gênero do jogo: ')
                    print('===== plataformas =====')
                    for indice, plataformas in enumerate(plataformas, start=1):
                        print(f"{indice} - {plataformas}")
                    escolha_plataforma = int(input('Digite plataforma do jogo: '))-1
                    valor_locacao = float(input('Digite o valor da locação do jogo: '))
                    cadastrar_jogo(titulo, plataformas, genero, valor_locacao)
                    break
                
                elif (menu_jogo == 2):
                    pass
                    break
        
                elif (menu_jogo == 3):
                    break

                else:
                 print('opção inválida, Tente novamente.')   

    elif (menu == 2):
        pass

    elif (menu == 3):
        pass

    elif (menu == 4):
        break

    else:
        print('opção inválida, Tente novamente.')