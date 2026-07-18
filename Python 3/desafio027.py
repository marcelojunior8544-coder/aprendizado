#Dizer o primeiro e último nome
nome = str(input('Informe seu nome: ')).strip()
pn = nome.split()[0]
un = nome.split()[-1]
print('É um prazer te conhecer {} {}\n'
      'Seu primeiro nome é {}.\n'
      'Seu ultimo nome é {}.'
      .format(pn,un,pn,un)
      )
