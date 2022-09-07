import os, time

print("Bienvenido a Adivina Palabra!")
cantPalabras = 0
maxIntentos = 0
palabra = ""
adivinaPalabra = [] #Lista auxiliar, contiene una copia de la palabra a adivinar
jugadores = [["", 0], ["", 0]] #Almacena nombre de jugadores y puntaje

jugadores[0][0] = input("Ingrese el nombre del jugador 1: ")
jugadores[1][0] = input("Ingrese el nombre del jugador 2: ")
cantPalabras = int(input("Ingrese la cantidad de palabras para esa ronda: "))*2
maxIntentos = int(input("Ingrese la cantidad de intentos para adivinar la palabra: "))
turno = [0,1]
os.system('cls')

#Función para proponer la palabra a adivinar
def faseProponedor():
    global palabra
    print("Ahora juega proponedor: " + jugadores[turno[0]][0])
    print("Estas son las reglas para ingresar la palabra: ")
    print("-Debe tener caracteres que pertenezcan al alfabeto español.")
    print("-Debe estar en minúsculas.")
    print("-El tamaño no puede ser mayor a 20 caracteres.")
    print("Tiene 3 intentos para indicar una palabra valida")
    palabra = input("Ingrese la palabra: ")
    i = 2 #cantidad de intentos fijada por ejercicio
    while palabra != palabra.lower() or len(palabra) > 20 or not palabra.isalpha():
        print(f"Palabra no valida. Le quedan {str(i)} intentos")
        print("Si falla los 3 intentos, perdera automaticamente.")
        palabra = input("Ingrese una palabra valida: ")
        i = i - 1
        if i == 0:
            os.system('cls')
            perdedor()
    os.system('cls')

#Si el proponedor falla al elegir una palabra, pierde automáticamente
def perdedor():
    print(f"El jugador {jugadores[turno[0]][0]} ha perdido.")
    print(f"Gana el jugador {jugadores[turno[1]][0]} con {jugadores[turno[1]][1]} puntos!")
    quit()

#Convierte la palabra a adivinar en una lista rellena con "_"
def guion_bajo(unapalabra):
    adivinaPalabra.clear()
    for i in range(0, len(unapalabra)):
        adivinaPalabra.append("_")

#Función para adivinar la palabra, letra a letra
def faseAdivinador():
    intentos = 0
    while intentos < maxIntentos:
        print("Ahora juega el adivinador: " + jugadores[turno[1]][0])
        print(f"La palabra tiene {len(palabra)} letras.")
        print(f"Tiene {maxIntentos-intentos} intentos para adivinar la palabra.")
        print("Adivine que letra tiene la palabra: ")
        print(" ".join(adivinaPalabra)) #Imprime la lista auxiliar usando como separador un espacio
        letra = input()
        while not letra.isalpha() or len(letra) != 1:
            letra = input("Error. Ingrese una letra: ")
        letra = letra.lower()
        for x, y in enumerate(palabra):
            if letra == y:
                adivinaPalabra[x] = y
        if adivinaPalabra == list(palabra):
            print(f"Correcto! La palabra es: {palabra}")
            jugadores[turno[1]][1] += calcula_puntaje(intentos)
            time.sleep(5)
            break
        if letra not in adivinaPalabra:
            intentos += 1
        os.system('cls')
    if maxIntentos == intentos:
        print(f"No acertaste, {jugadores[turno[1]][0]}. La palabra era: {palabra}")
        time.sleep(5)

#Calcula el puntaje de jugador adivinador
def calcula_puntaje(intentos):
    puntaje = (1-intentos/maxIntentos)*len(palabra)
    return puntaje

#Invierte el turno entre proponedor/adivinador
def cambia_de_turno():
    if turno[0] == 0:
        turno[0] = 1
        turno[1] = 0
    else:
        turno[0] = 0
        turno[1] = 1

#Una vez terminado el juego imprime el jugador ganador, el perdedor y sus puntajes
def puntaje_final():
    jugadores[0][1] = round(jugadores[0][1], 1)
    jugadores[1][1] = round(jugadores[1][1], 1)
    if jugadores[0][1] > jugadores[1][1]:
        print(f"El ganador es el jugador {jugadores[0][0]} con {jugadores[0][1]} puntos!")
        print(f"El jugador {jugadores[1][0]} obtuvo un puntaje de {jugadores[1][1]}")
    elif jugadores[0][1] == jugadores[1][1]:
        print(f"Hubo un empate! Ambos jugadores obtuvieron {jugadores[1][1]} puntos!")
    else:
        print(f"El ganador es el jugador {jugadores[1][0]} con {jugadores[1][1]} puntos!")
        print(f"El jugador {jugadores[0][0]} obtuvo un puntaje de {jugadores[0][1]}")

#Bucle que se repite según el número de palabras, que contiene todas las funciones a utilizar
for i in range(cantPalabras):
    faseProponedor()
    guion_bajo(palabra)
    faseAdivinador()
    cambia_de_turno()
    os.system('cls')
puntaje_final()
