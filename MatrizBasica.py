#MATRIZ BASICA
suma=0
multiplicacion=1
suma2=1
multiplicacion2=1
#suma y multiplicacion de la matriz diagonal
M=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
fil=len(M)
for i in range(4):
    for j in range(4):
        if(i==j):
            suma=suma+M[i][j]
            multiplicacion=multiplicacion*M[i][j]
#suma y multiplicacion de la contradiagonal
for i in range(4):
    for j in range(4):
        if(j==fil-1-i):
            suma2=suma2+M[i][j]
            multiplicacion2=multiplicacion2*M[i][j]

print("la suma de la diagonal es: " , str(suma))
print("la multiplicacion de la diagonal es: ",str(multiplicacion) )
print("La suma de la contradiagonal es: ", str(suma2))
print("la multiplicacion de la contradiagonal es: ", str(multiplicacion2))
