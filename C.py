numeros = input("Ingresa numeros: ").split()

columna = int(numeros[1]) 
fila= int(numeros[0]) 
matriz = []

def crear_input(): 
    hallar_primero = False
    hallar_segundo = False 
    r  = "Triple Corolla Flower"
    posicion_primero = []
    posicion_segundo = []
    for i in range (fila): 
        n = input("cadena: ")
        k = []
        
        
        for m in range(columna): 
            k.append(n[m])
            if n[m] == "*" and hallar_primero == False: 
                posicion_primero = [i, m]
                hallar_primero = True 
        matriz.append(k)
    for s in range(posicion_primero[0]+2, fila-2): 
            if matriz[s] != matriz[s+1]:
        
                for m in range(columna):
                
                    if matriz[s+2][m] == "*"  and hallar_segundo == False: 
                        posicion_segundo = [s+2, m]
                        hallar_segundo = True
                        if m != columna-1 and matriz[]:
                            r = "Double Petal Flower"
                       
                        break 
    return print(r)

crear_input()
    
            
    
                
                
                
            
            
                
    
        
                
            
            
    
        