def main():
    x = get_int()
    print(f"x e {x}")

def get_int():
    while True:
        try:
            return int(input("Valor do x? "))
        except ValueError:
            pass

main()
