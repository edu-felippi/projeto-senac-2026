from playlist import Playlist


if __name__ == "__main__":
    playlist = Playlist("Viajei")
    playlist.adicionar_musica("tudo vai dar certo")
    playlist.adicionar_musica("manchild")
    assert len(playlist.musicas) == 2

    assert playlist.remover_musica("Dai Dai") == "Música não encontrada"

    playlist.remover_musica("manchild")

    assert len(playlist.musicas) == 1
    