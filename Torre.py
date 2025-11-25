def torre_hanoi(n, inicio, fim, meio):
    if n == 1:
        print(f"Mova o disco 1 de {inicio} para {fim}")
        return
    torre_hanoi(n-1, inicio, meio, fim)
    print(f"Mova o disco {n} de {inicio} para {fim}")
    torre_hanoi(n-1, meio, fim, inicio)

if __name__=='__main__':
    # Exemplo de uso
    n = int(input("Digite o número de discos: "))
    torre_hanoi(n, "A", "C", "B")