
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while not enforcou and not acertou:
        chute = input("Qual a letra? ")
        chute.strip()
        index = 0
        for letra in palavra_secreta:
            if (chute.lower() == letra.lower()):
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1

    print("Fim de jogo")

if (__name__ == "__main__ "):
    jogar()