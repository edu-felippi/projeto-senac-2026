class Playlist:

    nome: str

    def __init__(self, nome: str):
        self.nome = nome
        self.musicas = []

    def adicionar_musica(self, nome_musica: str):
        self.musicas.append(nome_musica)

    def remover_musica(self, nome_musica: str):
        for nome_musica in self.musicas:
            self.musicas.remove(nome_musica)
        return "Música não encontrada"
    
    def mostrar_playlist(self):
        print(self.nome)
        for nome_musica in self.musicas:
            print(nome_musica)