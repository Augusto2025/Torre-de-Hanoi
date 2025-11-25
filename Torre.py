def torre_hanoi(n, inicio, fim, meio):
    if n == 1:
        print(f"O disco 1 foi da torre {inicio} para torre {fim}")
        return
    torre_hanoi(n-1, inicio, meio, fim)
    print(f"O disco {n} foi da torre {inicio} para torre {fim}")
    torre_hanoi(n-1, meio, fim, inicio)

if __name__=='__main__':
    while True:
        n = int(input("Digite o número de discos: "))
        if n < 3:
            print("Informe um número maior ou igual a 3.")
        else:
            break
    torre_hanoi(n, "A", "C", "B")