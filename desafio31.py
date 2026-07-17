dist = float(input('Qual a distância da viagem: ')) # Definindo a distância
if dist <= 200:
    print('\033[4;34mEssa viagem vai custar R${:.2f}\033[m'.format(dist*0.5))
else:
    print('\033[4;31mEssa viagem vai custar R${:.2f}\033[m'.format(dist*0.45))
    