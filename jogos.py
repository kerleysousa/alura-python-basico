import forca
import adivinhacao

print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")

print("(1) Adivinhacao (2) Forca")

jogo = int(input("Qual jogo?"))

if (jogo==1):
    adivinhacao.jogar()
elif (jogo==2):
    forca.jogar()