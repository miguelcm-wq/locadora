from jogo import jogos

while(True):
    menu = int(input('\n(1) - Jogo\n(2) - Cliente\n(3) - Locações\n(4) - sair\n Digite: '))

    if (menu == 1):
        jogos()

    elif (menu == 2):
        pass

    elif (menu == 3):
        pass

    elif (menu == 4):
        break

    else:
        print('opção inválida, Tente novamente.')