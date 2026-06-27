a, b, c, d = map(int, input().split())

def contar(a, b, c, d): 
    semana = 1
    ardillas = c

    while True:
        siguiente = ardillas * a + b
        if siguiente > d:
            break
        ardillas = siguiente
        semana += 1

       
       
    print(semana)
    
    
contar(a, b, c, d)
        