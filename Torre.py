import string


def gerar_nomes_torres(qtd):
    base = list(string.ascii_uppercase)
    nomes = []
    i = 0
    while len(nomes) < qtd:
        if i < len(base):
            nomes.append(base[i])
        else:
            nomes.append(base[i % len(base)] + str(i // len(base)))
        i += 1
    return nomes


def torre_hanoi(n, inicio, fim, meio):
    if n == 1:
        print(f"O disco 1 foi da torre {inicio} para torre {fim}")
        return
    torre_hanoi(n - 1, inicio, meio, fim)
    print(f"O disco {n} foi da torre {inicio} para torre {fim}")
    torre_hanoi(n - 1, meio, fim, inicio)


if __name__ == '__main__':
    # pedir número de torres (mínimo 3)
    while True:
        try:
            qtd_torres = int(input("Digite o número de torres (mínimo 3): "))
        except ValueError:
            print("Valor inválido — informe um número inteiro.")
            continue
        if qtd_torres < 3:
            print("Informe um número maior ou igual a 3.")
        else:
            break

    # pedir número de discos (mínimo 3)
    while True:
        try:
            qtd_discos = int(input("Digite o número de discos: "))
        except ValueError:
            print("Valor inválido — informe um número inteiro.")
            continue
        if qtd_discos < 3:
            print("Informe um número maior ou igual a 3.")
        else:
            break

    torres = gerar_nomes_torres(qtd_torres)
    inicio = torres[0]
    fim = torres[-1]
    meio = torres[1]  # nota: solução simples usa a primeira torre auxiliar

    print(f"Torres: {', '.join(torres)}")
    if qtd_torres == 3:
        torre_hanoi(qtd_discos, inicio, fim, meio)
    else:
        print("Usando algoritmo simples (não-óptimo) que utiliza efetivamente 3 torres.")
        torre_hanoi(qtd_discos, inicio, fim, meio)