import random


def get_mensagem():
    file = 'mensagens.txt'
    lines = open(file).read().splitlines()

    linha = random.choice(lines)
    return linha
