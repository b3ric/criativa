x = int(input("Valor de x? "))
print(f"x is {x}")

####

try:
    x = int(input("Valor de x? "))
    print(f"x is {x}")
except ValueError:
    print("x nao e um inteiro")

####

try:
    x = int(input("Valor de x? "))
except ValueError:
    print("x nao e um inteiro")
else:
    print(f"x is {x}")

###


# explicar linha e linha

while True:
    try:
        x = int(input("Valor de x? "))
    except ValueError:
        print("x nao e um inteiro")
    else:
        break

print(f"x is {x}")


### hack

while True:
    try:
        x = int(input("Valor de x? "))
        break
    except ValueError:
        print("x nao e um inteiro")

print(f"x is {x}")

# get_int

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("Valor de x? "))
        except ValueError:
            print("x nao e um inteiro")
        else:
            break
    return x

# melhorar implementacao de get int

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("Valor de x? "))
        except ValueError:
            print("x nao e um inteiro")
        else:
            return x # here, return is stronger than break

# melhorar mais

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("Valor de x? "))
            return x
        except ValueError:
            print("x nao e um inteiro")

# melhorar mais

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("Valor de x? "))
        except ValueError:
            print("x nao e um inteiro")

# melhor? ta muito criptico... 


# usando pass

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("Valor de x? "))
        except ValueError:
            pass # eu ainda to catching a excp

# making elegant

def main():
    x = get_int("Valor de x? ")
    print(f"x is {x}")

def get_int(prompt): # making it reusable
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass