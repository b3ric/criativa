# git / github
# wsl extension on vs code
# basico linux
# vamos ver a linguagem em si, terminal so, pra depois comecar a criar coisas maiores

##############################################

# hello world
# explicar isso
# basico linux
# executavel python3

print("Ola, Mundo")

##############################################

# funcoes predeterminadas (eg: print)
# print nao imprime qualquer coisa... argumentos da funcao
# bugs, anedota
# cometer um erro de proposito. 

print("Ola, Mundo") # remove parenthesis
      
# rodar e mostrar erro
# perguntas?

##############################################

# Melhorar esse programa, faze-lo mais interativo
# Faze-lo dizer Ola Eric.

print("Qual e seu nome?")
input() # mencionar que essa funcao tambem recebe argumento

input("Qual e seu nome? ")
print("Ola, Mundo")
# isso nao funciona muito bem

input("Qual e seu nome? ")
print("Ola, Eric")
# isso nao funciona muito bem

input("Qual e seu nome? ")
print("Ola, Eric")
# colocar Matheus: isso nao funciona muito bem

##############################################

# VALORES DE RETORNO
# A FUNCAO NOS PODE PASSAR DE VOLTA ALGUM VALOR
# QUERO GUARDAR ISSO EM ALGUM LUGAR
# VARIAVEIS.. MATH.. MESMA COISA, X, Y, Z

nome = input("Qual e seu nome? ")
print("Ola, Eric")

# explicar o = not equality, assignment

# erro proposital, perguntar o grupo...
nome = input("Qual e seu nome? ")
print("Ola, nome")

# ok.... mas not really that good, erro gramatical, feio
nome = input("Qual e seu nome? ")
print("Ola,")
print(nome)

##############################################

# COMMENTS explain
# explicar pra mim mesmo, pro prof
# lembrar no dia seguinte, no futuro
# erro, vc pode ler qual sua intencao, caso ha algum erro
# pra esse programa e simples, mas um grande eh bom


# eg: 

# Pedir usuario o nome
nome = input("Qual e seu nome? ")
# Dizer Ola pro usuario
print("Ola,")
print(nome)

##############################################

# MELHORAR O PROGRAMA, ta feio, esse line break

# Pedir usuario o nome
nome = input("Qual e seu nome? ")
# Dizer Ola pro usuario
print("Ola," + nome) # nao eh adicao, juntando palavras
# rodar e mostrar a falta de espaco. perguntar pra eles como fix
 
# Pedir usuario o nome
nome = input("Qual e seu nome? ")
# Dizer Ola pro usuario
print("Ola, " + nome)

# recapitular

##############################################

# MELHORAR MAIS

# Pedir usuario o nome
nome = input("Qual e seu nome? ")
# Dizer Ola pro usuario
print("Ola, ", nome) # virgula... argumentos multiplos
# primeiro argumento
# uma forma mais elegante
# argumentos multiplos automaticamente agregam espacos
# rodar e mostrar


# Pedir usuario o nome
nome = input("Qual e seu nome? ")
# Dizer Ola pro usuario
print("Ola,", nome) # remover espaco..

# PERGUNTAS? 
# PERGUNTAS? 
# PERGUNTAS?
 
##############################################

# MELHORAR MAIS

# VOLTANDO PRO OUTRO METODO

# Pedir usuario o nome
nome = input("Qual e seu nome? ")
# Dizer Ola pro usuario
print("Ola,")
print(nome)

#mostrar que tava feio e tal..

# a funcao print, automaticamente move o cursor pra prox linha
# mas vc pode modificar este comportamento

##############################################

# PARAMETROS NOMEADOS
# explorar a documentacao do print
# explicar a importancia e riqueza de documentacao

#https://docs.python.org/3/library/functions.html#print

# explicar objects, sep, end.. oq eh \n ? 
# mostrar que eu posso manipular o comportamento de funcoes, nao so essa mas tds
# sep, separator
# focar no sep e no end, esquecer o resto por agora

print(*objects, sep=' ', end='\n', file=None, flush=False)

# Pedir usuario o nome
nome = input("Qual e seu nome? ")
# Dizer Ola pro usuario
print("Ola, ", end="") # manipulando o comportamento
print(nome)
# rodar e mostrar que agora tudo na mesma linha

# Pedir usuario o nome
nome = input("Qual e seu nome? ")
# Dizer Ola pro usuario
print("Ola, ", end="???") # manipulando o comportamento
print(nome)
# rodar e mostrar que agora tudo na mesma linha


# SEP

# Pedir usuario o nome
nome = input("Qual e seu nome? ")
# Dizer Ola pro usuario
print("Ola,", nome) 

#manipular o sep, vcs lembram o que era? 

# Pedir usuario o nome
nome = input("Qual e seu nome? ")
# Dizer Ola pro usuario
print("Ola,", nome, sep="???")
# rodar, mostrar que eh feio, mas como pode ser manipulado

# PERGUNTAS SOBRE PARAMETROS?  

##############################################

# MELHORAR MAIS AINDA, MAIS ELEGANTE, MANIPULACAO DE STRINGS

# Pedir usuario o nome
nome = input("Qual e seu nome? ")
# Dizer Ola pro usuario
print("Ola, {nome}")
# rodar a mostrar que nao funciona

# Pedir usuario o nome
nome = input("Qual e seu nome? ")
# Dizer Ola pro usuario
print(f"Ola, {nome}") # eu preciso dizer pro python que isso eh uma string de format, f string
# rodar, funciona :)

# TIPO DE DADO STRING... str (Cadeia/corda de caracteres)

##############################################

# MELHORAR
# NAO CONTROLAMOS O INPUT DO USUARIO!! 
# ESPACOS EXTRAS, MOSTRAR
# MINUSCULO AO INVES DE MAIUSCULO
# O TIPO DE DADO STRING VEM COM UM MONTE DE FERRAMENTA 
# MANIPULAR O INPUT DO USUARIO

# Pedir usuario o nome
nome = input("Qual e seu nome? ")
# Dizer Ola pro usuario
print(f"Ola, {nome}")

# RODAR ERRADO:          eric         
# vai imprimir feio...



##############################################

#MELHORAR

# Pedir usuario o nome
nome = input("Qual e seu nome? ")

# Remover espaco vazio
nome = nome.strip() # explicar, strip left right, equal sign AGAIN!

# Dizer Ola pro usuario
print(f"Ola, {nome}")

### rodar de novo com um monte de espaco
# mas com 'eric' minusculo 

##############################################


#MELHORAR

# Pedir usuario o nome
nome = input("Qual e seu nome? ")

# Remover espaco vazio
nome = nome.strip()

# Capitalizar
nome = nome.capitalize()

# Dizer Ola pro usuario
print(f"Ola, {nome}")

# RODAR NOVAMENTE
# Nao importa como o usuario entra o nome... 
# E se o usuario decidir digitar nome e sobrenome? 
# rodar programa e entrar eric baptista
# mostrar que so eric vai capitalizar

##############################################

# TRUQUE LINUX ARROW UP

nome = input("Qual e seu nome? ")

# Remover espaco vazio
nome = nome.strip()

# Capitalizar
nome = nome.title() # agora simmmmmm

# Dizer Ola pro usuario
print(f"Ola, {nome}")

##############################################

# MELHORAR, REDUZIR LINHAS DE CODIGO
# EU CONSIGO CADEAR FUNCOES EM PYTHON

# Pedir nome
nome = input("Qual e seu nome? ")

# Remover espaco vazio
nome = nome.strip().title()

# Dizer Ola pro usuario
print(f"Ola, {nome}")

# da pra diminuir ainda mais:

# Pedir nome
nome = input("Qual e seu nome? ").strip().title()

# Dizer Ola pro usuario
print(f"Ola, {nome}")


# PERGUNTAS??? 
# PERGUNTAS??? 
# PERGUNTAS??? 

# VOCES ACHAM MELHOR CADEADO ASSIM OU MAIS QUEBRADO?
# E UMA QUESTAO DE GOSTO
# CONCEITO DE ELEGANCIA EM CODIGO

##############################################

# MOSTRAR OUTRA FUNCAO POPULAR, SPLIT
# Caso o usuario digite o nome e sobrenome

# Pedir nome
nome = input("Qual e seu nome? ").strip().title()

# Chamar a funcao split
nome, sobrenome = nome.split(" ")

# Dizer Ola pro usuario
print(f"Ola, {nome}")

##############################################

# PASSAR PRA INTEGROS, O QUE E UM INTEGRO
# NAO TEM DECIMOS
# SIMBOLOS EM PYTHON: + - * / %

##############################################

# MODULO INTERATIVO DO PYTHON, O INTERPRETADOR
1 + 1
print("ola, mundo")
# nao usamos tanto assim, so p vcs saberem

##############################################

# salvar arquivo antigo
# novo arquivo calculator.py

# TRABALHANDO COM NUMEROS

x = 1
y = 2
z = x + y

print(z)

#nao muito util, so vai calcular sempre 1 + 2

##############################################

# MELHORAR

# qual uma forma da gente pegar esse nuumero do usuario? 
x = input("Digite valor de x: ")
y = input("Digite valor de y: ")
z = x + y

print(z)

# qual o problema? qual o bug? 
# vem do teclado como string, texto
##############################################

# MELHORAR


# eh possivel converter um tipo de dado pra outro tipo de dado
x = input("Digite valor de x: ")
y = input("Digite valor de y: ")
z = int(x) + int(y) # int alem de ser um tipo de dado, eh uma funcao tb, o que essa funcao faz?

print(z)

# SHOW LINUX AUTO COMPLETE WHEN EXECUTING

##############################################

# MELHORAR - CONVERSAO DE TIPOS

# PRECISAMOS REALMENTE DA VARIAVEL Z? 
# eu posso cadear funcoes, a funcao de dentro vai executar, dps a de fora
# mostrar um exemplo com matematica PRIMEIRO


x = int(input("Digite valor de x: "))
y = int(input("Digite valor de y: "))
print(x + y)

# vcs preferem essa versao? questao de estilo 

##############################################


# TA OK? MAS NAO TA LEGAL, FOI MUITO LONGE... NAO EH ELEGANTE, LEGIVEL
print(int(input("Digite valor de x: ")) + int(input("Digite valor de y: ")))


##############################################

x = int(input("Digite valor de x: "))
y = int(input("Digite valor de y: "))
print(x + y)

##############################################

# MELHORAR
# FLOAT !! Decimais
# nossa calculadora ta presumindo q o usuario vai coloar int

x = float(input("Digite valor de x: "))
y = float(input("Digite valor de y: "))
print(x + y)

# 1.2
# 3.4

# show... nao funcionaria antes

# MAS E SE EU QUISER ARREDONDAR?

x = float(input("Digite valor de x: "))
y = float(input("Digite valor de y: "))

z = round(x + y)

print(z)

# NUMEROS GRANDES?

x = float(input("Digite valor de x: "))
y = float(input("Digite valor de y: "))

z = round(x + y)

print(z)


##############################################

# DIVISAO

x = float(input("Digite valor de x: "))
y = float(input("Digite valor de y: "))

z = (x / y) # sem formatar
z = round(x / y, 2)

print(z)



#######################################

# DEFINIR FUNCOES
# VOLTAR PRO hello.py

name = input("Qual e seu nome? ")
ola()
print(name)

#mostrar que isso nao funciona pq hello nao def


def ola():
    print("Ola")

name = input("Qual e seu nome? ")
ola()
print(name)

# parametrizar a funcao ola pra fazer tudo de uma vez

def ola(nome):
    print("Ola", nome)

name = input("Qual e seu nome? ")
ola(nome)

# default mundo, caso um nome nao entre

def ola(nome="mundo"):
    print("Ola", nome)

ola()
name = input("Qual e seu nome? ")
ola(nome)

# mostrar se a funcao estiver abaixo ele nao vai saber,
# precisa estar em ordem 
# mas isso pode ser uma merda pq tem que ester sempre em cima


# CONCEITO MAIN

def main():
    nome = input("Qual e seu nome? ")
    ola(nome)

def ola(nome="mundo"):
    print("ola,",nome)

main()

# SCOPE!

def main():
    nome = input("Qual e seu nome? ")
    ola()

def ola():
    print("ola,",nome)

main()

# variaveis somente existem onde elas foram definidas


# RETURN!!!!

# EX: float, int, etc
# voltar pro calculator.py

def main():
    x = int(input("Qual valor do x? "))
    print("x ao quadrado e", square(x))

def square(n):
    return n * n

# construir em cima disso

# lembrar do exercicio
    # PONTO em numeros grandes!
    # calc com funcoes