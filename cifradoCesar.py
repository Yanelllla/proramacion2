#CIFRADO CESAR
abecedario="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

print("ingrese el texto a decifrar: ")
texto= input()

print("ingrese el desplazamiento: ")
des= int(input())

cifrado= ""

for letra in texto.upper():
    if letra in abecedario:
        indice = abecedario.find(letra)
        indice += des
        if indice >=26:
            indice -=26
        cifrado += abecedario[indice]
    else:
        cifrado += letra
print("el resultado es: ", cifrado)
