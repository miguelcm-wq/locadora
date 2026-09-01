plataformas = ['PC', 'Xbox', 'Playstation', 'Nintendo']
jogos = []

def cadastrar_jogo(titulo, plataformas, genero, valor_locacao):
    jogo = {'titulo': titulo, 'plataforma': plataformas, 'genero': genero, 'valor_locacao': valor_locacao}
    jogos.append(jogo)

def listar_jogo(jogos):
    print('===== Lista de Jogos =====')
    for jogo in jogos:
        print(f'\nTítulo: {jogo['titulo']}\nGênero: {jogo['genero']}\nPlataforma: {jogo['plataforma']}\nValor da locação: {jogo['valor_locacao']}')