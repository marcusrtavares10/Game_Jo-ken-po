from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('-='*15)
print('VAMOS JOGAR JO-KEN-PO COMIGO?')
print('-='*15)
print('''Suas opções:
[0] Pedra 
[1] Papel
[2] Tesoura''')
jogador = int(input('Escolha sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!')
sleep(1)
print('-='*11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*11)
if computador == 0:  #computador jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('PARABÉNS!!! VOCÊ VENCEU')
    elif jogador == 2:
        print('IHH DEU RUIM! VOCÊ PERDEU')
    else:
        print('JOGADA INVÁLIDA')
if computador == 1:  #computador jogou papel
    if jogador == 0:
        print('IHH DEU RUIM! VOCÊ PERDEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('PARABÉNS! VOCÊ VENCEU')
    else:
        print('JOGADA INVÁLIDA')
if computador == 2:  #computador jogou tesoura
    if jogador == 0:
        print('PARABÉNS! VOCÊ VENCEU')
    elif jogador == 1:
        print('IHHH DEU RUIM! VOCÊ PERDEU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
