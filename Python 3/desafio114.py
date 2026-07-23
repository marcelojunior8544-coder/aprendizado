# teste se pode acessar o site pudim
import urllib.request

try:
    urllib.request.urlopen('https://python.org/')
except:
    print(f'\033[31mNão consegui acessar o site do Python')
else:
    print('\033[34mConsegui acessar o site do Python')
