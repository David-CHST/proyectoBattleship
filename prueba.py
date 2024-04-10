#--------------------------------#
# Proyecto de Batalla Naval
# Posicionamiento de flota

#hola dos
#hola tres

"""
Naves crucero = 1 posicion por iteracion
Naves acorazado = 1 poscion por iteracion
Destructor = 1 o 2 posiciones por iteracion de acuerdo al area disponnible
"""

#El avance se realiza de manera automática
#Cuando hay un choque cambia la dirección


# Define las variables para los tipos de nave [TAMAÑO, MAXMOVIMIENTO, DISPONIBLES]
#datosJuego = {"Jugadores":[], "Naves":[[],[]]}

#defaultNaves[tipoNave][2] -= 1 # Restar cantidad de naves disponibles de ese tipo


# Se crean 3 clases distintas, plantillas para crear partidas, jugadores y naves
# Partida guarda los jugadores de la partida, las naves de la partida (según cada jugador) y la matriz del juego en su estado actual
# Jugador guarda los datos de cada jugador dentro de la partida, almacenando las estadísticas pertinentes
# Nave guarda los datos de cada tipo de nave para ser asignados al crearse, las posiciónes

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
        self.navesPorColocar = [6,4,2]

class Nave:
    def __init__(self, tipoNave, dirNave, posNave):
        self.defaultNaves = [[1,2],[2,1],[3,1]]
        self.tipoNave = tipoNave #El usuario otorga el tipo de nave colocada
        self.dirNave = dirNave #El usuario define la dirección en que fue colocada la nave
        self.yPosInicial, self.xPosInicial = posNave[0:] # La posición x y posición y de la nave son dadas en una lista (se toman ambos valores con el [0:])
        self.tamañoNave, self.movimientoMax = self.defaultNaves[tipoNave-1][0], self.defaultNaves[tipoNave-1][1] # Definir el tamaño y el movimiento máximo de la nave
        self.totalPos = []

def colocarNave(numJugador):
    naveActual = partidaActual.listaNaves[numJugador][-1] # Se obtiene la nave más reciente del jugador actual
    #Se revisa si el jugador aún puede colocar este tipo de nave:
    if partidaActual.listaJugadores[numJugador].navesPorColocar[naveActual.tipoNave - 1] <= 0:
        print("Error: Ha llegado a la máxima cantidad de naves de este tipo.")
        return False
    # Se utilizan índices en una lista temporal para obtener factores de dirección que definirán hacia a dónde debe simularse la posición de la nave en el tablero
    direccionesPosibles = [[0,-1],[1, 0],[0, 1],[-1, 0]] #Izquierda
    factorDirX, factorDirY = direccionesPosibles[naveActual.dirNave - 1]
    for i in range(naveActual.tamañoNave):  # Se revisa según el tamaño de la nave, todas las casillas que va a ocupar en el juego
        # A la posición de la nave se le suma i + un factor de dirección que cambia según la dirección del barco para evitar repetición de código
        # Se utiliza un try/except para evitar que el programa se caiga en caso de una posición equivocada
        # La posición yPosInicial va primero porque se define según la fila de la matriz (primer índice)
        try:
            if not 0 <= naveActual.yPosInicial+(i*factorDirY): 
                print("Error: La nave no cabe en el tablero, inténtelo nuevamente.")
                return False  
            if not 0 <= naveActual.xPosInicial+(i*factorDirX):
                print("Error: La nave no cabe en el tablero, inténtelo nuevamente.")
                return False  
            if partidaActual.matrizJuego[naveActual.yPosInicial+(i*factorDirY)][naveActual.xPosInicial+(i*factorDirX)] != 0:
                print("Error: El espacio está obstruido por otra nave, inténtelo de nuevo")
                return False
        except IndexError:
            print("Error: La nave no cabe en el tablero, inténtelo nuevamente.")
            return False
    # Este código coloca la nave en la matriz, si nunca chocó contra nada.
    for i in range(naveActual.tamañoNave):
        # Marca las posiciones de cada espacio tomado por la nave con un 1 o un 2 según el jugador
        partidaActual.matrizJuego[naveActual.yPosInicial+(i*factorDirY)][naveActual.xPosInicial+(i*factorDirX)] = numJugador + 1
    # Se le debe restar al jugador actual una de las naves disponibles del tipo que se acaba de colocar, para tener un máximo de naves
    partidaActual.listaJugadores[numJugador].navesPorColocar[naveActual.tipoNave - 1] -= 1
    return True

def nuevoBarco(numJugador):
    # Solicita al usuario el número de la nave a agregar y las coordenadas
    while True:
        print("""
            [1] Destructor
            [2] Crucero
            [3] Acorazado
                """)
        tipoNave = int(input("¿Qué tipo de nave desea agregar? "))

        # Verifica si el número de la nave es válido
        if tipoNave in [1,2,3]:
            nColumna = int(input("Ingrese el número de fila en el que desea posicionar el frente de la nave: "))-1
            nFila = int(input("Ingrese el número de columna desea posicionar el frente de la nave: "))-1
            print("""
            [1] Arriba
            [2] Derecha
            [3] Abajo
            [4] Izquierda
                """)
            dirNave = int(input("¿En cuál dirección desea colocar la cola de la nave?"))
            print("Coordenadas dadas:", nColumna+1, ",", nFila+1, "| Dirección: ", dirNave)

            # Inserta el número de la nave en la posición dada
            

            partidaActual.listaNaves[numJugador].append(Nave(tipoNave, dirNave, [nColumna,nFila])) # Añade un objeto de nave a la lista de naves del jugador
            
            # La siguiente condicional utiliza una función que revisa si es válido el posicionamiento de la nave.
            # En caso de serlo la misma función coloca la nave en la matriz y retorna un valor booleano.
            if colocarNave(numJugador): # Retorna verdadero en caso de colocar con éxito al jugador.
                break # En caso de ser válida se rompe el ciclo y el programa sigue al siguiente jugador.
            else:
                del partidaActual.listaNaves[numJugador][-1] # Borra la nave más reciente en caso de que la revisión sea inválida (retornado falso)
        else:
            print("Error: Debe seleccionar una nave válida")
        
    # Imprime la matriz actualizada
    
    print("------------------------------------")
    print("La matriz actualizada es la siguiente:")
    for fila in partidaActual.matrizJuego:
        print(fila)

# Inicializa la partida vacía
# Primera lista para almacenamiento de jugadores
# Segunda lista para almacenamiento de naves (1 sub-lista por jugador)
# Tercera lista corresponde a la matriz, que es creada de 20 columnas y 10 filas con un ciclo for de una línea
partidaActual = Partida([],[[],[]], [[0] * 20 for _ in range(10)])

# Guarda las características de los 3 tipos de naves, para ser utilizada en la colocación de naves


# Imprime la matriz vacía del juego
for fila in partidaActual.matrizJuego:
    print(fila)

# Llama a cada jugador a colocar un barco y luego finaliza el programa
#Creación de Jugador 1
partidaActual.listaJugadores.append(Jugador("aqui va el nombre","aquí va el nickname")) # se debe cambiar para que pida la información de los jugadores
#Creación de Jugador 2
partidaActual.listaJugadores.append(Jugador("aqui va el nombre","aquí va el nickname")) # se debe cambiar para que pida la información de los jugadores
for _ in range(12):
    for i in range(2):
        print(f"Es el turno del jugador {i+1}.")
        nuevoBarco(i)

#---------------------------------------------------------#

#SELECCIONAR EL TIPO DE MOVIMIENTO QUE SE LE QUIERA AGREGAR
#Comparar si es vertical u horizontal 
#de acuedrdo a la eleccion recorrer el bucle y agregar el movimiento
