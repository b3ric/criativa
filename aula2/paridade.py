def main():
    x = int(input("Valor do x: "))
    if e_par(x):
        print("x e Par")
    else:
        print("x e Impar")

def e_par(n):
    return n % 2 == 0

main()
