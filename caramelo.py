
def caramelo():
    km=int(input("ingrese el km final: "))

    for n in range(1, km+1):
        if n%3 == 0:
            print(f'vamos en el km {n}, toma un caramelo')
        else:
            print(f'vamos en el km {n}')

caramelo()

