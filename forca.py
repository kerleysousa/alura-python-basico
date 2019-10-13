import random

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    print(palavras)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero]
    letras_acertadas = ["_" for letras in palavra_secreta]

    acertou = False
    erros = 0

    print(letras_acertadas)

    while(True):
        chute = input("Qual a letra? ")
        chute.strip().lower()
        index = 0

        if(chute in palavra_secreta):
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = chute
                index += 1
        else:
            erros += 1
            print("Você errou! Restam {} tentativas".format(6-erros))

        if(erros == 6):
            break
        if(not "_" in letras_acertadas):
            acertou = True
            break

        print(letras_acertadas)

    if (acertou == True):
        print("Você ganhou")
    else:
        print("Você perdeu")

    print("A palavras secreta era {}".format(palavra_secreta.upper()))
    print("Fim de jogo")

if (__name__ == "__main__ "):
    jogar()