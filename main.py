import matplotlib.pyplot as plt
from PIL import Image as img
import random

user1 = {}
user2 = {}

for i in range(2):
    num = random.randint(1,151)
    while(num in user1):
        num = random.randint(1, 151)

    arquivo = f'pokemon_jpg/{num}.jpg'
    print(f'voce escolheu o pokemon {num}')
    im = img.open(arquivo)
    im.show()

    nome = input('digite o nome deste pokemon')
    tipo = input('digite o tipo deste pokemon (fogo, planta,agua,terra)')


    user1[num] = [nome, tipo]

for i in range(2):
    num = random.randint(1, 151)
    while(num in user2):
        num = random.randint(1, 151)

    arquivo = f'pokemon_jpg/{num}.jpg'
    print(f'voce escolheu o pokemon {num}')
    im = img.open(arquivo)
    im.show()

    nome = input('digite o nome deste pokemon')
    tipo = input('digite o tipo deste pokemon (fogo, planta,agua,terra)')

    user2[num] = [nome, tipo]

for i in range(2):
    print(user1)
    escolha1 = int(input('qual numero do pokemon vc quer escolher'))

    print('\n---------------------XX-------------------\n')
    print(user2)
    escolha2 = int(input('qual numero do pokemon vc quer escolher'))

    if(user1[escolha1][1] == 'fogo' and user2[escolha2][1] == 'agua'):
        vencedor = user2[escolha2][0]
        print(f'o segundo user ganhou a disputa com o {vencedor}')
    elif(user1[escolha1][1] == 'agua' and user2[escolha2][1] == 'fogo'):
        vencedor = user1[escolha1][0]
        print(f'o primeiro user ganhou a disputa com o {vencedor}')