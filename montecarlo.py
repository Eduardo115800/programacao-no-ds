import numpy as np
import matplotlib.pyplot as plt

# Parâmetros da simulação
anos = 10
simulacoes = 10  # Ajuste este valor para melhor visualização
retorno_medio = 0.07
desvio_padrao = 0.20
valor_inicial = 1000

# Simulação Monte Carlo
np.random.seed(42)
trajetorias = np.zeros((anos + 1, simulacoes))
trajetorias[0] = valor_inicial

for i in range(simulacoes):
    for j in range(1, anos + 1):
        retorno_aleatorio = np.random.normal(retorno_medio, desvio_padrao)
        trajetorias[j, i] = trajetorias[j - 1, i] * (1 + retorno_aleatorio)

# Plotando os resultados
plt.figure(figsize=(10, 5))
plt.plot(trajetorias, linewidth=1)
plt.xlabel("Ano")
plt.ylabel("Valor da Carteira")
plt.title("Simulação Monte Carlo para Investimento em Ações")
plt.grid()
plt.show()
