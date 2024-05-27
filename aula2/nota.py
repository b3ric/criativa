# entre 90 e 100: A
# entre 80 e 90 : B
# entre 70 e 80 : C
# entre 60 e 70 : D
# qualquer coisa abaixo: F

nota = int(input("Nota do aluno: "))

# LOGICA
# cima pra baixo

if nota >= 90:
    print("Nota: A")
elif nota >= 80:
    print("Nota: B")
elif nota >= 70:
    print("Nota: C")
elif nota >= 60:
    print("Nota: D")
else:
    print("Nota F")