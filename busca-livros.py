# Lista pré-definida com títulos de livros
livros = [
    "Cem Anos de Solidão",
    "Dom Casmurro",
    "O Senhor dos Anéis",
    "A Menina que Roubava Livros",
    "O Pequeno Príncipe",
    "Orgulho e Preconceito",
    "1984",
    "O Código Da Vinci",
    "A Revolução dos Bichos",
    "Grande Sertão: Veredas"
]

# Solicita ao usuário uma palavra-chave
palavra_chave = input("Digite uma palavra-chave para buscar nos títulos: ")

# Filtra os títulos que contêm a palavra-chave (ignorando maiúsculas/minúsculas)
resultados = [livro for livro in livros if palavra_chave.lower() in livro.lower()]

# Exibe os resultados ou uma mensagem apropriada
if resultados:
    print("\nTítulos encontrados:")
    for titulo in resultados:
        print("-", titulo)
else:
    print("\nNenhum título encontrado com a palavra-chave informada.")

