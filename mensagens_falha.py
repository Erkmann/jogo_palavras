import random


def get_mensagem():
    mensagens = [
        'Não foi dessa vez', 'Errou!', 'Não é essa a palavra!', 'A palavra não é essa, que pena!'
    ]

    mensagem = random.choice(mensagens)

    return mensagem
