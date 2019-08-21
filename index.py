import random

from pega_palavra import get_palavra
from pergunta import pergunta_user
from mensagens_falha import get_mensagem
from seleciona_dificuldade import get_dificuldade


dificuldade = get_dificuldade()
palavra = get_palavra(int(dificuldade))

palavra_embaralhada = "".join(random.sample(palavra, len(palavra)))

vezes = 1

while vezes <= 5:
    resposta = pergunta_user(palavra_embaralhada)
    if resposta == palavra:
        print('Parabéns, voce acertou em {} tentativa(s), e a palavra era {}'.format(vezes, palavra))
        exit()
    else:
        vezes += 1
        print('\n' + get_mensagem())
        print('\nVoce ainda tem {} tentativas'.format(5-vezes + 1))

print('\nQue pena, voce nao acertou a palavra, que era: {}, e '
      'todas as suas tentativas ja foram usadas. Quem sabe da próxima vez!'.format(palavra))
exit()
