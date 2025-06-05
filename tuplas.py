# Solicita ao usuário que insira as coordenadas geográficas (latitude e longitude)
coordenadas = input("Digite as coordenadas (latitude, longitude) separadas por vírgula: ")

# Converte a entrada em uma tupla de números de ponto flutuante
latitude, longitude = map(float, coordenadas.split(','))

# Exibe as coordenadas desempacotadas
print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")
