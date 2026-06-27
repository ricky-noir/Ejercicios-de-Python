def compress():
    n, m = map(int, input().split())
    pixels = []
    for _ in range(n):
        line = input().split()
        for px in line:
            val = int(px, 16)
            pixels.append(val)
    print(len(pixels))
    print(" ".join(str(v) for v in pixels))


def decompress():
    n, m = map(int, input().split())
    k = int(input())
    valores = list(map(int, input().split()))
    idx = 0
    for _ in range(n):
        fila = []
        for _ in range(m):
            val = valores[idx]
            hex_px = f"{val:08X}" 
            fila.append(hex_px)
            idx += 1
        print(" ".join(fila))


def main():
    modo = input().strip()
    if modo == "compress":
        compress()
    elif modo == "decompress":
        decompress()
    else:
        print("Modo desconocido")



main()
