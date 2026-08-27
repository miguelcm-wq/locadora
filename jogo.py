plataformas = ['PC', 'Xbox', 'Playstation', 'Nintendo']

def jogos():
    while(True):
        menu_jogo = int(input('\n(1) - cadastrar\t(2) - listar\t(3) - sair\n Digite: '))

        if (menu_jogo == 1):
            cadastrar_jogo(plataformas)

        elif (menu_jogo == 2):
            pass

        elif (menu_jogo == 3):
            break

def cadastrar_jogo(plataformas):
    titulo = input('\nDigite o ttulo do jogo: ')
    genero = input('Digite o gênero do jogo: ')
    for indice, plataformas in enumerate(plataformas, start=1):
        print(f"{indice} - {plataformas}")