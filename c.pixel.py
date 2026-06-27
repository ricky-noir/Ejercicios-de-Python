import sys

entrada = sys.stdin.buffer.readline


def leer_imagen(n):
    pixeles = []

    for _ in range(n):
        fila = entrada().split()
        for pixel in fila:
            pixeles.append(int(pixel, 16))

    return pixeles


def directo(pixeles):
    datos = [0]
    datos.extend(pixeles)
    return datos


def paleta(pixeles):
    color_a_indice = {}
    colores = []
    indices = []

    for color in pixeles:

        if color not in color_a_indice:
            color_a_indice[color] = len(colores)
            colores.append(color)

        indices.append(color_a_indice[color])

    cantidad = len(colores)

    if cantidad == 0:
        return None

    bits = max(1, (cantidad - 1).bit_length())
    por_entero = max(1, 32 // bits)

    empaquetados = []

    i = 0

    while i < len(indices):

        valor = 0

        for j in range(por_entero):

            if i + j >= len(indices):
                break

            valor |= indices[i + j] << (j * bits)

        empaquetados.append(valor)

        i += por_entero

    datos = [1, cantidad, bits]
    datos.extend(colores)
    datos.extend(empaquetados)

    return datos


def rle(pixeles):

    if len(pixeles) == 0:
        return [2]

    datos = [2]

    actual = pixeles[0]
    cantidad = 1

    for i in range(1, len(pixeles)):

        if pixeles[i] == actual and cantidad < 4294967295:
            cantidad += 1

        else:
            datos.append(cantidad)
            datos.append(actual)

            actual = pixeles[i]
            cantidad = 1

    datos.append(cantidad)
    datos.append(actual)

    return datos


def mejor_compresion(pixeles):

    opcion1 = directo(pixeles)

    opcion2 = paleta(pixeles)

    opcion3 = rle(pixeles)

    mejor = opcion1

    if len(opcion2) < len(mejor):
        mejor = opcion2

    if len(opcion3) < len(mejor):
        mejor = opcion3

    return mejor

def compress():

    n, m = map(int, entrada().split())

    pixeles = leer_imagen(n)

    datos = mejor_compresion(pixeles)

    print(len(datos))
    print(*datos)
    
def decompress():

    n, m = map(int, entrada().split())

    k = int(entrada())

    datos = list(map(int, entrada().split()))

    modo = datos[0]

    if modo == 0:

        pixeles = datos[1:]

    elif modo == 1:

        pos = 1

        cantidad = datos[pos]
        pos += 1

        bits = datos[pos]
        pos += 1

        colores = datos[pos:pos + cantidad]
        pos += cantidad

        empaquetados = datos[pos:]

        por_entero = max(1, 32 // bits)

        mascara = (1 << bits) - 1

        pixeles = []

        total = n * m

        for valor in empaquetados:

            for i in range(por_entero):

                if len(pixeles) >= total:
                    break

                indice = (valor >> (i * bits)) & mascara

                pixeles.append(colores[indice])

    else:

        pixeles = []

        pos = 1

        while pos < len(datos):

            cantidad = datos[pos]
            color = datos[pos + 1]

            for _ in range(cantidad):
                pixeles.append(color)

            pos += 2

    pos = 0

    for _ in range(n):

        fila = []

        for _ in range(m):

            fila.append("{:08X}".format(pixeles[pos]))
            pos += 1

        print(*fila)


def main():

    modo = entrada().decode().strip()

    if modo == "compress":
        compress()
    else:
        decompress()


main()