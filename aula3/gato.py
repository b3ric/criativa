def main():
    n = pegar_numero()
    miau(n)

def pegar_numero():
    while True:
        n = int(input("Numero de vezes? "))
        if n > 1:
            return n

def miau(numero):
    for _ in range(numero):
        print("miau")

main()