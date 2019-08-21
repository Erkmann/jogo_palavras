import random


def get_palavra(dificuldade):

    if dificuldade == 1:
        file = 'palavrasF.txt'
    elif dificuldade == 2:
        file = 'palavrasM.txt'
    elif dificuldade == 3:
        file = 'palavrasD.txt'

    lines = open(file).read().splitlines()

    linha = random.choice(lines)
    return linha
