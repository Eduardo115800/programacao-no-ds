# Solicita ao usuário que insira uma lista de nomes separados por vírgula
nomes = input("Digite os nomes separados por vírgula: ").split(',')

# Remove espaços extras dos nomes
nomes = [nome.strip() for nome in nomes]

# Itera sobre a lista usando enumerate e exibe o índice e o nome
for indice, nome in enumerate(nomes):
    print(f"{indice}: {nome}")
