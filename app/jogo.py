from random import randint
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0,2)
print('''escola sua opção 
[0] Pedra
[1] Papel
[2] Tesoura''')
print("=======================================")
jogador = int(input('diga qual sua opção ?'))
print("o computador escolheu {}".format(itens[computador]))
print('o jogador escolheu {}'.format(itens[jogador]))
print("=======================================")
print('jo')
print('ken')
print('pó')
print("=======================================")
if computador == 0:
    if jogador == 0:
        print('empatou')
    elif jogador ==1:
        print('jogador ganhou')
    elif jogador == 2:
        print('computador ganhou')

elif computador == 1:
    if jogador == 0:
        print('coputador ganhou')
    elif jogador ==1:
        print('empate')
    elif jogador == 2:
        print('jogador ganhou')

elif computador == 2:
    if jogador == 0:
        print('jogador ganhou')
    elif jogador ==1:
        print('computador ganhou')
    elif jogador == 2:
        print('empate')
else:
    print('Opção invalida, tente mais uma vez')
