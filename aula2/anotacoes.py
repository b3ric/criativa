# AULA DE HOJE VAI SER MAIS RAPIDO, PQ ELES SAO RAPIDOS 
# SEGUNDA FEIRA, VOU PASSAR EXERCICIO QUE JUNTA AS AULAS DE PASSADA E HJ

# INTRO CONDITIONALS

"""
>
>=
<
<=
==
!=

"""

# ONE EQ SIGN

# IF

# comparar.py

# comparar inteiros, valor do user, nao sabemos

x = int(input("Valor do x: "))
y = int(input("Valor do y: "))

# Queremos fazer decisoes sobre estes valores

if x < y: 
    print("x e menor que y.")
# Bool, sim ou nao, true or false, only two possible answers
# relembrar dos dois pontos e a indentacao. 
if x > y:
    print("x e maior que y")
if x == y: 
    print("x e igual a y")

# run program
# show diagram, logic, flow, top to bottom
# explicar do start, pro diamante, left, right 
# nao importa a resposta, ambas flechas vao pro proximo
# mais uma vez
# stop


# O QUE TA FEIO/NAO ELEGANTE NESSE CODIGO?
x = int(input("Valor do x: "))
y = int(input("Valor do y: "))

if x < y: 
    print("x e menor que y.")
if x > y:
    print("x e maior que y")
if x == y: 
    print("x e igual a y")

# eu nao preciso estar perguntando as 3 perguntas SEMPRE...

##########################################

# ELIF
x = int(input("Valor do x: "))
y = int(input("Valor do y: "))

if x < y: 
    print("x e menor que y.")
elif x > y:
    print("x e maior que y")
elif x == y: 
    print("x e igual a y")

# MUTUALMENTE EXCLUSIVAS.
# NAO CONTINUA PERGUNTANDO SE EU JA SEI A PERGUNTA

# SENAO SE
# isso nao afeta tanto a performance, programa pequeno 
# mas programas grandes, sim..

# diagrama 2
# mostrar como o programa morre logo depois de um true -> stop

# rodar o codigo de uma forma que ele caia no segundo diamante

# mostrar no diagrama que nao precisamos do ultimo diamante


###########################################

# LOGICA. 
# Porque o ultimo elif e inutil? 
x = int(input("Valor do x: "))
y = int(input("Valor do y: "))

if x < y: 
    print("x e menor que y.")
elif x > y:
    print("x e maior que y")
else:
    print("x e igual a y")

# rodar programa com os tres diamantes.

# mostrar diagrama ideal.
# programa menos complexo
# mais elegante

###########################################

# OR

# x e igual a y ou nao? 

x = int(input("Valor do x: "))
y = int(input("Valor do y: "))

if x < y or x > y:
    print("x nao e igual a y")
else: 
    print("x e igual a y")

# da pra melhorar? 
# perguntar menos vezes? 
# melhorar a logica? 

x = int(input("Valor do x: "))
y = int(input("Valor do y: "))

if x != y:
    print("x nao e igual a y")
else:
    print("x e igual a y")

# mostrar novo diagrama e comparar ambos

# se vc prefere o oposto, sem problema...

x = int(input("Valor do x: "))
y = int(input("Valor do y: "))

if x == y:
    print("x e igual a y")
else:
    print("x nao e igual a y")

#########################################

# NOVO PROGRAMA nota.py

nota = int(input("Nota: "))

if nota >= 90 and nota <= 100:
    print("Nota: A")
elif nota >= 80 and nota < 90:
    print("Nota: B")
elif nota >= 70 and nota < 80:
    print("Nota: C")
elif nota >= 60 and nota < 70:
    print("Nota: D")
else:
    print("Nota: F")

# rodar e mostrar que funciona

# MELHORAR, reduzir possibilidade de bugs, etc. 

# menos codigo, encadear

nota = int(input("Nota: "))

if 90 <= nota <= 100:
    print("Nota: A")
elif 80 <= nota < 90:
    print("Nota: B")
elif 70 <= nota < 80:
    print("Nota: C")
elif 60 <= nota < 70:
    print("Nota: D")
else:
    print("Nota: F")


# PERGUNTAR MENOS VEZES (LOGICA)


if nota >= 90:
    print("Nota: A")
elif nota >= 80:
    print("Nota: B")
elif nota >= 70:
    print("Nota: C")
elif nota >= 60:
    print("Nota: D")
else:
    print("Nota: F")

# PORQUE ISSO FUNCIONA? if elif, top down

#############################################

# NOVO PROGRAMA, paridade.py

# lembram? 

"""
+
-
*
/
%
"""

x = int(input("Valor do x: "))

# o que significa um numero ser PAR?

if x % 2 == 0:
    print("Par")
else:
    print("Impar")

# rodar programa

# o que mais pode ser feito aqui? 

# vamos voltar ao habito do main... organizacao

def main():
    x = int(input("Valor do x: "))
    if e_par(x):
        print("Par")
    else:
        print("Impar")

# relembrar... qual o problema aqui? Chamar alguem. 

def e_par(n):
    if n % 2 == 0:
        # INTRODUZIR BOOLEAN VALUES, another data type 
        # can only be True or False
        return True
    else:
        return False

main()

# rodar programa... mostrar que funciona
# math and conditionals... :)

# FORMA "PYTHONICA" 

def main():
    x = int(input("Valor do x: "))
    if e_par(x):
        print("Par")
    else:
        print("Impar")

# relembrar... qual o problema aqui? Chamar alguem. 

def e_par(n):
    return (n % 2 == 0) # dps remove o parentesis

main()

# FIM 
# LEMBRAR DO EXERCICIO NA SEGUNDA