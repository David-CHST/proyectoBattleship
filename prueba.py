#--------------------------------#
#-------------------------------#
# Pruebas de Batalla Naval

# Posicionamiento de flota



"""
Naves crucero = 1 posicion por iteracion
Naves acorazado = 1 poscion por iteracion
Destructor = 1 o 2 posiciones por iteracion de acuerdo al area disponnible
"""

#El avance se realiza de manera automática
#Cuando hay un choque cambia la dirección


# Define las variables para los tipos de nave [TAMAÑO, MAXMOVIMIENTO, DISPONIBLES]
#datosJuego = {"Jugadores":[], "Naves":[[],[]]}




#datosNaves[tipoNave][2] -= 1 # Restar cantidad de naves disponibles de ese tipo

# La siguiente clase se encarga de la creación de cada nave, idealmente se pondrá en otro archivo para mayor orden
class Partida:
    def __init__(self, listaJugadores, listaNaves, matrizJuego):
        self.listaJugadores = listaJugadores
        self.listaNaves = listaNaves
        self.matrizJuego = matrizJuego

class Jugador:
    def __init__(self, realName, nickName):
        self.realName = realName
        self.nickName = nickName
        self.tirosAcertados = 0
        self.tirosFallidos = 0
        self.tamañoFlota = 0
        self.numHundimientos = 0

class Nave:
    def __init__(self, tipoNave, dirNave, posNave):
        self.tipoNave = tipoNave #El usuario otorga el tipo de nave colocada
        self.dirNave = dirNave #El usuario define la dirección en que fue colocada la nave
        self.xPos, self.yPos = posNave[0:] # La posición x y posición y de la nave son dadas en una lista (se toman ambos valores con el [0:])
        self.tamañoNave, self.movimientoMax = datosNaves[tipoNave-1][0], datosNaves[tipoNave-1][1] # Definir el tamaño y el movimiento máximo de la nave
        self.totalPos = []

def validarNave(numJugador):
    naveActual = partidaActual.listaNaves[numJugador][partidaActual.listaJugadores[numJugador].tamañoFlota] # son muchos índices, pero llevan a la más reciente nave
    # Se utilizan índices en una lista temporal para obtener factores de dirección que definirán hacia a dónde debe simularse la posición de la nave en el tablero
    direccionesPosibles = [[0, 1],[1, 0],[0, -1],[-1, 0]]
    factorDirX, factorDirY = direccionesPosibles[naveActual.dirNave - 1]
    for i in range(naveActual.tamañoNave):  # Se revisa según el tamaño de la nave, todas las casillas que va a ocupar en el juego
            # A la posición de la nave se le suma i + un factor de dirección que cambia según la dirección del barco para evitar repetición de código
            ################ A esto le falta una revisión if para asegurar que no suceda un error de índice, porque si no existe la casilla se cae.
            if partidaActual.matrizJuego[naveActual.xPos+(i*factorDirX)][naveActual.yPos+(i*factorDirY)] != 0:
                return False
    # Este código coloca la nave en la matriz, si nunca chocó contra nada.
    for i in range(naveActual.tamañoNave):
        partidaActual.matrizJuego[naveActual.xPos+(i*factorDirX)][naveActual.yPos+(i*factorDirY)] = "X"



def nuevoBarco(numJugador):
    # Solicita al usuario el número de la nave a agregar y las coordenadas
    print("""
        [1] Destructor
        [2] Crucero
        [3] Acorazado
            """)
    tipoNave = int(input("¿Qué tipo de nave desea agregar? "))

    # Verifica si el número de la nave es válido
    if tipoNave in [1,2,3]:
        nFila = int(input("Ingrese el número de fila en el que desea posicionar el frente de la nave: "))-1
        nColumna = int(input("Ingrese el número de columna desea posicionar el frente de la nave: "))-1
        print("""
        [1] Arriba
        [2] Derecha
        [3] Abajo
        [4] Izquierda
            """)
        dirNave = int(input("¿En cuál dirección desea colocar la cola de la nave?"))
        print("Coordenadas dadas:", nFila+1, ",", nColumna+1, "| Dirección: ", dirNave)

        # Inserta el número de la nave en la posición dada
        #Función que revisa si la nave es válida

        partidaActual.listaNaves[numJugador].append(Nave(tipoNave, dirNave, [nFila,nColumna])) # Añade un objeto de nave a la lista de naves en el diccionario de partidaActual
        validarNave(numJugador) # Revisa si es válido el posicionamiento de la nave utilizando datos del mismo diccionario
        print(partidaActual.listaNaves)
        print(partidaActual.listaNaves[numJugador][-1].tipoNave)
        print(partidaActual.listaNaves[numJugador][-1].dirNave)
        print(partidaActual.listaNaves[numJugador][-1].tamañoNave)
        print(partidaActual.listaNaves[numJugador][-1].movimientoMax)
        print(partidaActual.listaNaves[numJugador][-1].xPos)
        print(partidaActual.listaNaves[numJugador][-1].yPos)
        
    # Imprime la matriz actualizada
    
    print("------------------------------------")
    print("La matriz actualizada es la siguiente:")
    for fila in partidaActual.matrizJuego:
        print(fila)
    

# Inicializa la matriz vacía con valores numéricos
matrizJuego = [[0] * 10 for _ in range(5)]

# Inicializa la partida vacía
partidaActual = Partida([],[[],[]], matrizJuego)

# Guarda las características de los 3 tipos de naves, para ser utilizada en la colocación de naves
datosNaves = [[1,2,6],[2,1,2],[3,1,4]]

# Imprime la matriz vacía del juego
for fila in partidaActual.matrizJuego:
    print(fila)

# Llama a cada jugador a colocar un barco y luego finaliza el programa
for i in range(2):
    partidaActual.listaJugadores.append(Jugador("Hola","Sisoy"))
    nuevoBarco(i)

#---------------------------------------------------------#

#SELECCIONAR EL TIPO DE MOVIMIENTO QUE SE LE QUIERA AGREGAR
#Comparar si es vertical u horizontal 
#de acuedrdo a la eleccion recorrer el bucle y agregar el movimiento
