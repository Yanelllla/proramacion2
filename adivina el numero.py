#ADIVINA EL NUMERO
import random
sec=random.randint(1,20)
intentosrealizados=0
intentosmaximos=6
x=0
while(intentosrealizados<intentosmaximos):
    intentosrealizados=intentosrealizados+1
    print("ingresa un numero: ")
    x=int(input('-->'))
    if(x>sec):
        print(x,"ingresar un numero mas chico")
    else:
        if(x<sec):
            print(x,"ingresar un numero mas grande")
            if(x==sec):
                print("felicidades!,acerto el numero!")
print("lo siento,no ha adivinado el numero ")
    
