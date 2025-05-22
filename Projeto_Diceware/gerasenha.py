import os
from random import randint

def gerasenha():
    passphrase = []
    for x in range(5):
        nums = []
        # Criando uma sequência de números
        for i in range(5):
            num = randint(1, 6)
            nums.append(num)

        # Transformando essa sequencia em uma string
        sequencia =  "".join(str(num) for num in nums)

        with open('worldlist.txt', 'r') as arquivo:
            for linha in arquivo:
                # Transforma cada linha do arquivo em uma lista, onde o indice 0 é a sequencia de numeros
                # e o 1, a palavra correspondente a sequencia
                linha = linha.split()
                if linha[0] == sequencia:
                    passphrase.append(linha[1])

            # Transforma a lista passphrase em uma única string
            senha = " ".join(passphrase)

            senha = senha.replace(" ", "_", )

    return senha


# Metodo Adicional para deixar a senha mais forte
def substituicao(senha):
    for i in range(5):
        subs = ["@", "!", "0"]
        letras = ["a", "i", "o"]

        for indice, letra in enumerate(letras):
            senha = senha.replace(letra, subs[indice])

        senha = "".join(senha)

    return senha



