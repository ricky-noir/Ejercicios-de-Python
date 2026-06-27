import sys

def main():

    n = int(input())
    arreglo = list(map(int, input().split()))
    usados = [False] * (n + 1)

    for x in arreglo:
        if x != -1:
            usados[x] = True

    siguiente = 0

    for i in range(n):

        if arreglo[i] == -1:

            while siguiente <= n and usados[siguiente]:
                siguiente += 1

            if siguiente <= n:
                arreglo[i] = siguiente
                usados[siguiente] = True
            else:
                arreglo[i] = 0

    print(*arreglo)

main()