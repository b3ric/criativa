def main():
    nome = input("Qual e o seu nome? ")
    ola(nome)

def ola(nome):
    print("Ola,", nome.strip().title())

main()
