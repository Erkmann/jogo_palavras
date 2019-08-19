import random


def get_palavra():
    file = 'palavras.txt'
    lines = open(file).read().splitlines()

    linha = random.choice(lines)
    return linha
