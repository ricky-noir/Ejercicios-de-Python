import random
adivinado = True 

def main():
    
    print("elige una dificultad ")
    print("1. hasta el 10  ")
    print("2. hasta el 50 ")
    print("3. hasta el 100  ")
    
    
    dificultad = int(input("ingrese el número de la dificultar: ")) 
    if dificultad  == 1: 
        numero_aleatorio = random.randint(1, 10)
        adivina(numero_aleatorio)
    elif dificultad ==2: 
        numero_aleatorio = random.randint(1, 50)
        adivina(numero_aleatorio)
    elif dificultad ==3: 
        numero_aleatorio = random.randint(1, 100)
        adivina(numero_aleatorio)
    else: 
        print("el num ingresado no es valido ")
        

        
def adivina (num_aleatorio): 
    contador = 1 
    num = int(input("ingrese que numero cree que es: "))

    while adivinado:
        if  num < num_aleatorio:
            print("Pista: el número ingresado es menor del número secreto")
            num = int(input("Ingresa otro número: "))
            contador += 1 
        
        elif num> num_aleatorio: 
            print("Pista: el número ingresado es mayor del número secreto")
            num= int(input("Ingresa otro número: "))
            contador += 1 
        else: 
            break 
    return print("Felicidades número adivinado en: " + str(contador) + " intentos")

main() 