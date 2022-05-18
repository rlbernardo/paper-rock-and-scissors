from random import randint

itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogada?  '))
print('-=_' * 10)
print('Computador jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogador]))
print('-=_' * 10)

if computador == 0:
    if jogador == 0:
        print('Isso é um empate')
    elif jogador == 2:
        print('O jogador VENCE!')
    elif jogador

elif computador == 1:

elif computador == 2:


