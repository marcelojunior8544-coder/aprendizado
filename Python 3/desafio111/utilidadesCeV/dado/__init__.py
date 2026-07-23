# validação de valor

def leiadinheiro(txt):
   valido = False
   while not valido:
       num = str(input(txt).replace(',' , '.').strip())
       if num.isalpha() or num == '':
           print(f'O valor {num} é inválido')

       else:
           return float(num)
   return None

