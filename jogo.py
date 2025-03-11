# Importa o módulo random, que contém funções para gerar números aleatórios
import random

# Gera um número aleatório entre 1 e 10 e o armazena na variável numero_secreto
numero_secreto = random.randint(1, 10)

# Inicializa o contador de tentativas como 0
tentativas = 0

# Define o número máximo de tentativas permitidas
max_tentativas = 5

# Exibe uma mensagem de boas-vindas e explica o objetivo do jogo
print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número que estou pensando, entre 1 e 10.")

# Inicia o loop do jogo; ele continuará enquanto o jogador não atingir o número máximo de tentativas
while tentativas < max_tentativas:
    # Solicita ao jogador que insira um palpite e converte a entrada para um número inteiro
    palpite = int(input("Digite seu palpite: "))

    # Incrementa o contador de tentativas em 1 a cada palpite
    tentativas += 1

    # Compara o palpite do jogador com o número secreto
    if palpite == numero_secreto:
        # Se o jogador acertar, exibe uma mensagem de parabéns com o número de tentativas usadas
        print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
        break  # Encerra o loop, pois o jogador venceu
    elif palpite < numero_secreto:
        # Caso o palpite seja menor que o número secreto, orienta o jogador a tentar um número maior
        print("Quase lá! Tente um número maior.")
    else:
        # Caso o palpite seja maior que o número secreto, orienta o jogador a tentar um número menor
        print("Quase lá! Tente um número menor.")

    # Informa ao jogador quantas tentativas ainda restam, se houver
    if tentativas < max_tentativas:
        print(f"Você tem {max_tentativas - tentativas} tentativas restantes.")

# Caso o jogador exceda o número máximo de tentativas, exibe uma mensagem de fim de jogo
else:
    print("Infelizmente, você não acertou. O número era", numero_secreto)
    print("Fim do jogo!")

