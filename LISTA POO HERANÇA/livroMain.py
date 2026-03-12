from Livros import Livro

titulo = input("Escreva o nome do livro: ")
Autor = input("Escreva o nome do Autor: ")
Editora = input("Escreva o nome da Editora: ")
paginas = int(input("Quantidade de paginas: "))
largura = int(input('Digite a largura: '))
profundidade = int(input('Digite a profundidade: '))
cumprimento = int(input('Digite a cumprimento: '))
descricao = input("digite: ")
idioma = input("digte o idioma: ")
livro = Livro(titulo,Autor,Editora,paginas,descricao,(largura,profundidade,cumprimento), idioma)

x = livro.get_todasInformacao()
