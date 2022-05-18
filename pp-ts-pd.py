from random import randint

itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogada?  '))
print('-=_' * 15)
print('Computador jogou {}'.format(itens[computador]))
print('jogador jogou {}'.format(itens[jogador]))
print('-=_' * 15)

if computador == 0:
    if jogador == 0:
        print('Isso é um empate')
    elif jogador == 1:
        print('O jogador VENCE!')
    elif jogador == 2:
        print('O jogador VENCE!')
    else:
        print('Jogada inválida! Escolha uma opção válida')

if computador == 1:
    if jogador == 0:
        print('Computador VENCE!')
    elif jogador == 1:
        print('Isso é um Empate!')
    elif jogador == 2:
        print('O jogador VENCE!')
    else:
        print('Jogada inválida! Escolha uma opção válida')

if computador == 2:
    if jogador == 0:
        print('Computador PERDE!')
    elif jogador == 1:
        print('Computador VENCE!')
    elif jogador == 2:
        print('Isso é um EMPATE')
    else:
        print('Jogada inválida! Escolha uma opção válida')

print('-=_' * 15)

