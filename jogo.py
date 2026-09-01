plataformas = ['PC', 'Xbox', 'Playstation', 'Nintendo']
jogos = []

def cadastrar_jogo(titulo, plataformas, genero, valor_locacao):
    jogo = {'titulo': titulo, 'plataforma': plataformas, 'genero': genero, 'valor_locacao': valor_locacao}
    jogos.append(jogo)