cadena = input()

def contar_letras(cadena): 
    r = "NO"
    t = 0
    s = 0
    c = 0
    for i in range(len(cadena)): 
        if cadena[i] == "T": 
            t += 1
        elif cadena[i] == "S": 
            s += 1
        elif cadena[i] == "C": 
            c += 1
    
    if t == s and s== c: 
        r = "YES"
    print(r)
    
contar_letras(cadena)

    
            