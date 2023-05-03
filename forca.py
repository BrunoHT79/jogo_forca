import random

def joga():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    print("")
    palavras = []
    with open("palavras.txt", "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange (0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    letras_acertadas = ["_" for letras in palavra_secreta]
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    print("Você poderá errar no máximo cinco vezes.")
    print("Na sexta você perderá o jogo!")

    while (not enforcou and not acertou):
        chute = input("Qual letra você acha que tem na palavra? ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (letra.upper() == chute.upper()):
                    letras_acertadas[index] = chute.upper()
                index += 1
        else:
            erros += 1
            print("Você errou {} vezes.".format(erros))
            if (erros == 5):
                print("Cuidado!!!")
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("Parabéns! Você ganhou!!")
    else:
        print("Infelizmente você não acertou e foi enforcado!!")
    print("Fim do jogo!!!")


if __name__ == "__main__":
    joga()