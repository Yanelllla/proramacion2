import random		
IMAGENES_AHORCADO = ['''		
  +---+		
  |   |		
      |		
      |		
      |		
      |		
  =========''', '''		
  +---+		
  |   |		
  O   |		
      |		
      |		
      |		
  =========''', '''		
  +---+		
  |   |		
  O   |		
  |   |		
      |		
      |		
  =========''', '''		
  +---+		
  |   |		
  O   |		
 /|   |		
      |		
      |		
  =========''', '''		
  +---+		
  |   |		
  O   |		
 /|\  |		
      |		
      |		
  =========''', '''		
  +---+		
  |   |		
  O   |		
 /|\  |		
 /    |		
      |		
  =========''', '''		
  +---+		
  |   |		
  O   |		
 /|\  |		
 / \  |		
      |		
  =========''']
 
ListaDePalabras = 'hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja mofeta perezoso serpiente araña cigüeña cisne tigre sapo trucha pavo tortuga comadreja ballena lobo cebra'.split()
def ObtenerPalabraAlAzar(ListaDePalabras):
 def MostrarTablero(IMAGENES_AHORCADO,letrasCorrectas,letrasIncorrectas,PalabraSecreta,VidasRestantes,Ejecutar):
        IndiceDePalabras=random.randint(0,len(claveDePalabras)-1)
PalabraSecreta=ListaDePalabras[IndiceDePalabras]
PalMinus=PalabraSecreta.lower()
SubGuion=IndiceDePalabras*" _ "
Print(IMAGENES_AHORCADO[0],SubGuion)
WHERE(Ejecutar)
Ejecutar=True
input("ingrese su respuesta: ").lower()
PalUser=input("Adivine la palabra: ").lower()
