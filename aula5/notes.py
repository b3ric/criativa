# explicar modules/libraries
    # reusability
    # abstraction

# tem modules que ja vem com python
# tem modules que sao privados

"""

eg: random
eh complicado randomness
pra usar um module, tem que importa-lo: import

eg: random.choice(seq) from docs

Programa pra flip coin: 
"""

# generate.py

import random

moeda = random.choice(["cara"], ["coroa"])
print(moeda)

# run


"""
explicar from
import random por ex, importa TUDO
mas eu so quero choice
mas pq isso e bom?
explicar vantagem sobre scope
ou tbm pode ser melhor ser especifico, depende
tudo uma questao de scopt
"""

from random import choice

moeda = choice(["cara"], ["coroa"])
print(moeda)

# run

"""
randint, outro exemplo
"""

import random

numero = random.randint(1,10)
print(numero)

# run

"""
command-line arguments
explicar
terminal, muito popular
create: name.py
"""

# name.py
# programa que usara valores inputados no terminal
# vamos usar o sys module
# sys provem sys.argv (argument vector)
#   eh uma lista dos argumentos, ordenadas
# supor que eh um sistema de name tags

import sys

print("ola, meu nome e", sys.argv[1])

# run: python3 name.py Eric


"""
examinar sys.argv[1]
porque o index comeca no 0?
e se eu rodar: python3 name.py ?
como que eu conserto o index err?
"""

import sys

try:
    print("ola, meu nome e", sys.argv[1])
except IndexError:
    print("Too few arguments")

"""
improvements...
conditional
"""

import sys

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("ola, meu nome e", sys.argv[1])


"""
more about sys module: sys.exit
logically, it's ok, but design is not good
actual code i care about
1. check for errors
2. do the thing

"""

# why is this a bug?

import sys

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")

print("ola, meu nome e", sys.argv[1])

"""
improve code
exit mais CEDO
"""
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("ola, meu nome e", sys.argv[1])

"""
improve code
loop over args
"""

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

# what's wrong here?
for arg in sys.argv:
    print("ola, meu nome e", arg)

"""
introduzir slice
"""

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("ola, meu nome e", arg)

"""
TP packages vs native Python packages
pypi.org
pypi.org/project/cowsay
pip

criar say.py e setup pip
"""

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])

"""
outro pacote...
nos ajuda a interagir com APIs
Muitas APIs vivem na Internet
Podemos interagir com estes servicos via codigo
eg: buscar dados

intro requests
HTTP, me comporto como um browser
pip3 install requests
"""

# itunes.py
# para interagir com a API da Apple
# https://itunes.apple.com/search?entity=song&limit=1&term=metallica
# explicar esta url, api docs
# vcs sabem que estrutura eh esta? 
# lingua nativa de APIs e comunicacoes entre svcs
# quero simular o Chome

# itunes.py

import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(response.json())

# Apple nos esta retornando um json, Python nos converte a um dict

"""
review structure
vamos usar outra biblioteca pra nos ajudar a formatar estes dados, limpar, ta mt baguncado
"""

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(json.dumps(response.json(), indent=2))

# isso nos vai ajudar a entender os dados que estao retornando
# revisar novamente o dado retornado
# results, pq list?

"""
Fetch o que estou interessado desta estrutura
Quero que este programa imprima todas as tracks do artista
"""

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

o = response.json()
for result in o["results"]:
    print(result["trackName"])

# explicar codigo novamente, increase to 1, 10, 50 run. 

"""
e se eu quiser fazer meu proprio module local? 
pq eu faria isto? 
"""

# sayings.py

def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f'hello, {name}')

def goodbye(name):
    print(f'goodbye, {name}')

main()

# run

"""
e se eu quiser estas funcoes como modulo
"""

# say.py

import sys
from sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])

"""
pq aquilo aconteceu
from sayings import hello
python leu o arquivo inteiro
entao como fazer pra modular codigo? 
"""

# sayings.py

def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f'hello, {name}')

def goodbye(name):
    print(f'goodbye, {name}')

if __name__ == '__main__':
    main()

# nos restringe a CLI, eu posso importar sem problema.
# main so seria chamado 
# trocar por goodbye
#fim