# 1. Lista de nomes de estudantes
estudantes = ["Carlos", "Ana", "Pedro", "Beatriz", "Mariana"]

# Use sort() para ordenar diretamente a lista original
estudantes.sort()
print("Estudantes ordenados:", estudantes)  # A lista original é modificada

# 2. Lista de notas dos estudantes
notas = [88, 92, 78, 90, 85]

# Use sorted() para retornar uma nova lista ordenada
notas_ordenadas = sorted(notas)
print("Notas ordenadas:", notas_ordenadas)  # Retorna uma nova lista ordenada

# Verifica lista original de notas
print("Lista original de notas:", notas)  # A lista original permanece inalterada
