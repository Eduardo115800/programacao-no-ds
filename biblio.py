class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}\nNúmero de páginas: {self.paginas}"

# Solicita ao usuário os dados do livro
titulo = input("Informe o título do livro: ")
autor = input("Informe o autor do livro: ")
paginas = input("Informe a quantidade de páginas: ")
