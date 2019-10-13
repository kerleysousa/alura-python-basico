
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_"]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while not enforcou and not acertou:
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

        enforcou = erros == 6
        acertou = not "_" in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("Você ganhou")
    else:
        print("Você perdeu")

    print("Fim de jogo")

if (__name__ == "__main__ "):
    jogar()