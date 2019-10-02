import random

numero_secreto = random.randrange(1,100);
contador = 1
pontos = 1000

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

dificuldade = int(input("Escolha o nível de dificuldade: "))

if (dificuldade==1):
    total_de_tentativas = 10
elif (dificuldade==2):
    total_de_tentativas = 5
elif (dificuldade==3):
    total_de_tentativas = 2

for contador in range(1, total_de_tentativas+1):

    print(numero_secreto)
    print("Tentativa {} de {}".format(contador, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou e fez {} pontos!".format(pontos))
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
            pontos_perdidos = abs(pontos-chute)
            pontos = pontos - pontos_perdidos
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto-chute)
            pontos = pontos - pontos_perdidos

print("Fim do jogo")
print("### {} pontos!".format(pontos))
