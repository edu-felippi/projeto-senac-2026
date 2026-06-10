from pdf import PDF
from imagem import Imagem


if __name__ == "__main__":
    pdf = PDF()
    imagem = Imagem()
    documentos = [pdf, imagem]

    for documento in documentos:
        print(documento.exibir())