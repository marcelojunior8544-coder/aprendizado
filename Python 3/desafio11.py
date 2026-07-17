l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))
area = l*a
t = area/2
print('Uma parede de {}m X {}m tem {:.2f}m² de área'.format(l,a,area))
print('Vai precisar de {}l de tinta para pintar'.format(t))
