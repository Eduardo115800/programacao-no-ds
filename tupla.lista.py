class Biblioteca:
    def __init__(self):
        self.livros = []  # Lista para armazenar os livros

    def adicionar_livro(self, titulo, autor, ano):
        novo_livro = (titulo, autor, ano)  # Criando uma tupla com os dados do livro
        self.livros.append(novo_livro)  # Atualizando automaticamente a lista

    def consultar_livros(self):
        print("\nColeção de livros (tupla):")
        for livro in self.livros:
            print(livro)

        print("\nLista de livros armazenados:")
        print(self.livros)


# Criando uma instância da biblioteca
biblioteca = Biblioteca()

# Adicionando livros
biblioteca.adicionar_livro("Dom Casmurro", "Machado de Assis", 1899)
biblioteca.adicionar_livro("O Alquimista", "Paulo Coelho", 1988)
biblioteca.adicionar_livro("A Revolução dos Bichos", "George Orwell", 1945)

# Consultando os livros armazenados
biblioteca.consultar_livros()
