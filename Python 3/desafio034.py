# Calculo de aumento salárial
salario = float(input('Qual é o salário? R$'))
# Reajuste para salários maiores
if salario > 1250:
    reajuste = salario + (salario * 0.10)
# Reajuste para salário menores
else:
    reajuste = salario +(salario * 0.15)
print('Quem ganhava \033[33mR${:.2f}\033[m agora ganha \033[32mR${:.2f}\033[m.'
      .format(salario,reajuste))
