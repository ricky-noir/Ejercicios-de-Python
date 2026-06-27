import sys

def main():
    datos = sys.stdin.buffer.read().split()
    n = int(datos[0])

    numeros = map(int, datos[1:1 + 2 * n])

    min_x = max_x = None
    min_y = max_y = None

    for x in numeros:
        y = next(numeros)
        if min_x is None:
            min_x = max_x = x
            min_y = max_y = y
        else:
            if x < min_x:
                min_x = x
            elif x > max_x:
                max_x = x
            if y < min_y:
                min_y = y
            elif y > max_y:
                max_y = y

    a = max_x - min_x
    b = max_y - min_y
    area = a * b

    print(area, a, b)

main()


