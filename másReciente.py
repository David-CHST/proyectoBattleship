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

#-------------------------------------------------------------------------------------------------------------------------------------#

                  #   ----------------------------------  Clases a implementar  -------------------------------------------#

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
        self.numHundimientos = 0
        self.navesPorColocar = [1,1,1]

class Nave:
    def __init__(self, tipoNave, dirNave, posNave):
        self.defaultNaves = [[1,2],[2,1],[3,1]]
        self.tipoNave = tipoNave
        self.dirNave = dirNave
        self.yPosInicial, self.xPosInicial = posNave[0:]
        self.tamañoNave, self.movimientoMax = self.defaultNaves[tipoNave-1][0], self.defaultNaves[tipoNave-1][1]
        self.listaPosTotal = [] # Inicializa totalPos con las posiciones iniciales de la nave
        self.listaPosImpacto = []
        self.impactos = 0
        self.hundida = False
        self.seMueveEsteTurno = True
    
    #cambiar de acuerdo a la función
    def moverArriba(self):
        # Verifica si la nave puede moverse hacia arriba sin salir del borde superior del tablero
        for parOrdenado in self.listaPosTotal: #forloop
            if not parOrdenado[0] -1 in range(len(partidaActual.matrizJuego)): #0=y 1=x 
                print("Error: La nave no puede moverse más hacia arriba.")
                self.seMueveEsteTurno = False
                self.dirNave = 1
                return
            if not parOrdenado[1] in range(len(partidaActual.matrizJuego[0])):
                print("Error: La nave no puede moverse más hacia arriba.")
                self.seMueveEsteTurno = False
                self.dirNave = 1
                return
            
        for parOrdenado in self.listaPosTotal:
            parOrdenado[0] -= 1
        return True  # Devuelve True para indicar que el movimiento fue exitoso
    

    def moverAbajo(self):
        # Verifica si la nave puede moverse hacia abajp sin salir del borde superior del tablero
        for parOrdenado in self.listaPosTotal: #forloop
            if not parOrdenado[0] + 1 in range(len(partidaActual.matrizJuego)): #0=y 1=x 
                print("Error: La nave no puede moverse más hacia arriba.")
                self.seMueveEsteTurno = False
                self.dirNave = 1
                return
            if not parOrdenado[1]  in range(len(partidaActual.matrizJuego[0])):
                print("Error: La nave no puede moverse más hacia arriba.")
                self.seMueveEsteTurno = False
                self.dirNave = 1
                return
            self.seMueveEsteTurno = True   
            
        for parOrdenado in self.listaPosTotal:
            parOrdenado[0] += 1
        return True  # Devuelve True para indicar que el movimiento fue exitoso


    def moverIzquierda(self):
         # Verifica si la nave puede moverse hacia abajp sin salir del borde superior del tablero
        for parOrdenado in self.listaPosTotal: #forloop
            if not parOrdenado[0] in range(len(partidaActual.matrizJuego)): #0=y 1=x 
                print("Error: La nave no puede moverse más hacia arriba.")
                self.seMueveEsteTurno = False
                self.dirNave = 1
                return
            if not parOrdenado[1] - 1 in range(len(partidaActual.matrizJuego[0])):
                print("Error: La nave no puede moverse más hacia arriba.")
                self.seMueveEsteTurno = False
                self.dirNave = 1
                return
            
        for parOrdenado in self.listaPosTotal:
            parOrdenado[1] -= 1
        return True  # Devuelve True para indicar que el movimiento fue exito
    
    def moverDerecha(self):
         # Verifica si la nave puede moverse hacia abajp sin salir del borde superior del tablero
        for parOrdenado in self.listaPosTotal: #forloop
            if not parOrdenado[0] in range(len(partidaActual.matrizJuego)): #0=y 1=x 
                print("Error: La nave no puede moverse más hacia arriba.")
                self.seMueveEsteTurno = False
                self.dirNave = 1
                return
            if not parOrdenado[1] + 1 in range(len(partidaActual.matrizJuego[0])):
                print("Error: La nave no puede moverse más hacia arriba.")
                self.seMueveEsteTurno = False
                self.dirNave = 1
                return
            
        for parOrdenado in self.listaPosTotal:
            parOrdenado[1] += 1
        return True  # Devuelve True para indicar que el movimiento fue exito


#-------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------#

                  #   ----------------------------------  Colocación de la nave  -------------------------------------------#

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
        #Los junta una vez para cada tamaño de la nave
        naveActual.listaPosTotal.append([naveActual.yPosInicial+(i*factorDirY),naveActual.xPosInicial+(i*factorDirX)]) 
    # Se le debe restar al jugador actual una de las naves disponibles del tipo que se acaba de colocar, para tener un máximo de naves
    partidaActual.listaJugadores[numJugador].navesPorColocar[naveActual.tipoNave - 1] -= 1
    print(naveActual.listaPosTotal)
    return True


#-------------------------------------------------------------------------------------------------------------------------------------#

                  #   ----------------------------------  Nuevo Barco  -------------------------------------------#

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

#-------------------------------------------------------------------------------------------------------------------------------------#
                  #   ----------------------------------  Actualizar Matriz  -------------------------------------------#

def actualizarMatrizJuego():
    # Iterar sobre todas las filas de la matriz del juego
    for fila in range(len(partidaActual.matrizJuego)):
        # Iterar sobre todas las columnas de la matriz del juego
        for columna in range(len(partidaActual.matrizJuego[fila])):
            partidaActual.matrizJuego[fila][columna] = 0  # Reinicia la casilla a 0 (vacía)
    
    # Iterar sobre la lista de naves de cada jugador en el juego
    for numJugador, jugador in enumerate(partidaActual.listaNaves):
        
        jugador_num = numJugador + 1

        for nave in jugador:
        
            for parOrdenado in nave.listaPosTotal:
        
                jugador_marca = jugador_num if jugador_num != 2 else 2
                print(parOrdenado)
                partidaActual.matrizJuego[parOrdenado[0]][parOrdenado[1]] = jugador_marca

    # Iterar sobre la lista de naves de cada jugador en el juego para marcar las posiciones hundidas
    for numJugador, jugador in enumerate(partidaActual.listaNaves):

        for nave in jugador:
        
            for parOrdenado in nave.listaPosImpacto:
        
                partidaActual.matrizJuego[parOrdenado[0]][parOrdenado[1]] = "x"

    
#-------------------------------------------------------------------------------------------------------------------------------------#

                  #   ----------------------------------  Mover Barco  -------------------------------------------#

# Función para mover las naves del jugador
def moverNave():    
    # Iterar sobre las naves de cada jugador
    for naveAMover in partidaActual.listaNaves[0]: #Itera sobre cada nave en la lista de naves del jugador actual.
        direccion = naveAMover.dirNave  # Utilizar la dirección de la nave
        if direccion in [1, 2, 3, 4] and naveAMover.seMueveEsteTurno == True and naveAMover.impactos == 0:  # Comprobar si la dirección es válida        
            naveMoved = False # Se asigna la variable un valor booleano con el fin de que cuando este cambie de estado el bucle finalice
            while not naveMoved: #El bucle continuará ejecutandose siempre que "naveMoved" sea falsa               
                if direccion == 3:  # Arriba #Se compara la dirección con la selección de dirNave               
                    if naveAMover.moverArriba(): #se llaman los metodos anteriormente definidos               
                        print("Nave movida arriba.")#se imprime un mensaje indicando la dirección en la que se movió la nave                            
                        naveMoved = True #Si el movimiento es exitoso, lo iguala a True para no inicializar con las otras comparaciones y finalizar el ciclo 
                    else:
                        naveMoved = True
               #----------------------- La logica se repite con la abarcar los posibles casos   --------------------------#
                elif direccion == 1:  # Abajo           
                    if naveAMover.moverAbajo():                    
                        print("Nave movida abajo.")                                  
                        naveMoved = True      
                    else:
                        naveMoved = True      
                elif direccion == 2:  # Izquierda
                    if naveAMover.moverIzquierda():
                        print("Nave movida izquierda.")
                        naveMoved = True
                    else:
                        naveMoved = True
                elif direccion == 4:  # Derecha
                    if naveAMover.moverDerecha():
                        print("Nave movida derecha.")
                        naveMoved = True
                    else:
                        naveMoved = True
        else:
            print("Dirección de movimiento inválida para la nave. Moviendo a la siguiente nave.")
        naveAMover.seMueveEsteTurno == True
    # Lo mismo para el jugador 2
    for naveAMover in partidaActual.listaNaves[1]: #Itera sobre cada nave en la lista de naves del jugador actual.
        direccion = naveAMover.dirNave  # Utilizar la dirección de la nave
        if direccion in [1, 2, 3, 4] and naveAMover.seMueveEsteTurno == True and naveAMover.impactos == 0:  # Comprobar si la dirección es válida        
            naveMoved = False # Se asigna la variable un valor booleano con el fin de que cuando este cambie de estado el bucle finalice
            while not naveMoved: #El bucle continuará ejecutandose siempre que "naveMoved" sea falsa               
                if direccion == 3:  # Arriba #Se compara la dirección con la selección de dirNave               
                    if naveAMover.moverArriba(): #se llaman los metodos anteriormente definidos               
                        print("Nave movida arriba.")#se imprime un mensaje indicando la dirección en la que se movió la nave                            
                        naveMoved = True #Si el movimiento es exitoso, lo iguala a True para no inicializar con las otras comparaciones y finalizar el ciclo 
                    else:
                        naveMoved = True
               #----------------------- La logica se repite con la abarcar los posibles casos   --------------------------#
                elif direccion == 1:  # Abajo           
                    if naveAMover.moverAbajo():                    
                        print("Nave movida abajo.")                                  
                        naveMoved = True      
                    else:
                        naveMoved = True      
                elif direccion == 2:  # Izquierda
                    if naveAMover.moverIzquierda():
                        print("Nave movida izquierda.")
                        naveMoved = True
                    else:
                        naveMoved = True
                elif direccion == 4:  # Derecha
                    if naveAMover.moverDerecha():
                        print("Nave movida derecha.")
                        naveMoved = True
                    else:
                        naveMoved = True
        else:
            print("Dirección de movimiento inválida para la nave. Moviendo a la siguiente nave.")
        naveAMover.seMueveEsteTurno == True
    
    print("Se han movido todas las naves del jugador.")

#-----------------------------------------------        Registro jugadores    ----------------------------------------------------#

def registroJugadores(): #Se solicita el respectivo ingreso de datos (el nick, la futura clave para el diccionario y el nombre)
    realName = input("Ingrese el nombre real del jugador: ")
    nickName = input("Ingrese el apodo del jugador: ")
    return Jugador(realName, nickName) #El mae llama a la clase y sus respectivas propiedades

                #   ------------------------------------  Datos jugadores  ---------------------------------------  #


# Se recomienda dejar de utilizar esta función de esta manera, para no crear un nuevo diccionario sin necesidad.
def datosJugadores(): 
    global partidaActual
    
    datos_por_partida = {}
    
    for jugador in partidaActual.listaJugadores:
        datos_jugador = {
            "Real Name": jugador.realName,
            "Nick Name": jugador.nickName,
            "Tiros Acertados": jugador.tirosAcertados,
            "Tiros Fallidos": jugador.tirosFallidos,
            "Num Hundimientos": jugador.numHundimientos,
            "Flota": jugador.navesPorColocar
        }
        
        datos_por_partida[jugador.nickName] = datos_jugador
    
    return datos_por_partida

#-------------------------------------------------------------------------------------------------------------------------------------#

# Inicialización de la partida
partidaActual = Partida([], [[], []], [[0] * 20 for _ in range(10)])

#-------------------------------------------------------------------------------------------------------------------------------------#
                  #   ----------------------------------  Ataque de flota  -------------------------------------------#

def AtaqueFlota(numJugador):

    # Obtener la lista de naves del jugador actual
    numOponente = 0 if (numJugador+1) == 2 else 1 #Hacer chequeo para ver si las naven se calleron

    listaNavesOponente = partidaActual.listaNaves[numOponente] #Obtiene la lista de naves del oponente, haciendo que el indice cambie del jugador opuesto 
                                                                                            #Evita que exista "jugador 3"

    # Obtener coordenadas del jugador
    fila = int(input("Digite la fila de la coordenada en la que desea iterar: "))  # Solicita al jugador la fila
    columna = int(input("Digite la columna de la coordenada sobre la que desea iterar: "))  # Solicita al jugador la columna
    coordenada = [fila - 1, columna - 1]  # Se resta 1 para ajustar a la indexación de Python (empezando desde 0)

    # Iterar sobre las naves del jugador
    for nave in listaNavesOponente:
        print("prueba",nave.listaPosTotal)
        print("Coordenada",coordenada)
        if coordenada in nave.listaPosTotal:  # Comprobar si las coordenadas están en las posiciones de la nave
            nave.listaPosImpacto.append([fila -1, columna -1]) #Agrega las casillas impactadas a la nave impactada y posteriormente detectan los hundimientos
            nave.impactos += 1 #Si no lo ha sido, cambia el valor a true
            partidaActual.listaJugadores[numJugador].tirosAcertados += 1 # Incrementar el contador de tiros acertados del jugador
            print("¡Acertaste un disparo! La nave ha sido impactada.")
            #-----------------------------------------------------------------#
            #como le digo a bro que si el numero de impactos es igual al numero de casillas de la nave
            if nave.impactos == (nave.tipoNave):  # Si la nave ha sido impactada, detectan los hundimientos
                nave.hundida = True
                partidaActual.listaJugadores[numJugador].numHundimientos += 1 
        else:
            print("Tiro fallido, no impactaste en ninguna nave.")
            partidaActual.listaJugadores[numJugador].tirosFallidos += 1
        return
    

    if numJugador.numHundimientos == len(listaNavesOponente):
        print("¡Todas las naves del oponente han sido hundidas!")

    

#-------------------------------------------------------------------------------------------------------------------------------------#
                  #   ----------------------------------  Ingreso Jugadores  -------------------------------------------#

for i in range(2):  #Se registran dos jugadores por partida
    nuevo_jugador = registroJugadores() #En cada iteración del bucle se solicita agregar los datos anterirmente establecidos en la función invocada
    print(f"Registro del jugador {i+1}:") #Indica un registro del jugador actual

    #   --------------------------------    Info del jugador registrado     ------------------------------- #

    #   Es para que se vea boonito en terminal pero en algún momento gg :(
    print("Jugador registrado:")
    print("Nombre real:", nuevo_jugador.realName)
    print("Apodo:", nuevo_jugador.nickName)

    #   ---------------------------------------------------------------------------------------------------- #

    partidaActual.listaJugadores.append(nuevo_jugador)# jugador creado se agrega a la lista listaJugadores del objeto partidaActual.


#-------------------------------------------------------------------------------------------------------------------------------------#

                  #   ----------------------------------  Acceso a Jugadores  -------------------------------------------#

# Acceso a los datos de los jugadores registrados
print("-------------------------------------------------")
print("Cuidado, estos prints no han sido actualizados, sólo los que están después de este inicial!")
print("¿Desea acceder a los datos de los jugadores registrados?")

accion = input("S/N: ") #Se hace una variable que almacene la respuesta del usuario

if accion.upper() == "S":  #De a cuerdo a la respuesta del mismo accede o no a la información mediante una comparación

    datos_por_partida = datosJugadores() #lama a la función con el objetivo de acceder al diccionario con los datos de los jugadores por partida. 

    for nick_name, datos in datos_por_partida.items(): #Se genera el for para de acuerdo al nick, acceder al diccionario de datos por partida

        print("-------------------------------------------------")
        print(f"Datos del jugador '{nick_name}':") #Imprime el nick para mayor legibilidad

        for clave, valor in datos.items(): #se imprimen los datos guardados del jugador de acuerdo al nick registrado

            print(f"{clave}: {valor}")

else: #Si el jugador decide no ingresar, simplemente no se accede a la información

    print("No se accedió a los datos de los jugadores registrados")


#-------------------------------------------------------------------------------------------------------------------------------------#

                  #   ----------------------------------  Turno de jugadores  -------------------------------------------#


# Asignación del turno de jugadores y colocación de barcos

# i = numJugador

for _ in range(1): #También modifiqué eso para hacer el agregado más simple
    for i in range(2):
        #Es invocada aquí porque es más legible en la terminal xd
        actualizarMatrizJuego()
        print("------------------------------------")
        print("La matriz actualizada es la siguiente:")
        for fila in partidaActual.matrizJuego:
            print(fila) 
        print("------------------------------------")
        nuevoBarco(i)
    
    
while True:
    for i in range(2):
        print("####################################")
        actualizarMatrizJuego()
        print("------------------------------------")
        print("La matriz actualizada es la siguiente:")
        for fila in partidaActual.matrizJuego:
            print(fila)
        print("------------------------------------")
        AtaqueFlota(i)
        print("¿Desea acceder a los datos de los jugadores registrados?")
        accion = input("S/N: ") 
        if accion.upper() == "S":
            print("-------------------------------------------------")
            jugAccedido = partidaActual.listaJugadores[i] # Recuerde que i es el índice del jugador actual
            print(f"Datos del jugador: '{jugAccedido.realName}'") 
            print("Real Name:", jugAccedido.realName) 
            print("Nick Name:", jugAccedido.nickName)
            print("Tiros Acertados:", jugAccedido.tirosAcertados)
            print("Tiros Fallidos:", jugAccedido.tirosFallidos)
            print("Num Hundimientos:", jugAccedido.numHundimientos)
            print("Tipos de Naves que le faltan por colocar:", jugAccedido.navesPorColocar)
            print("-------------------------------------------------")
    if  partidaActual.listaJugadores[1].numHundimientos == 12 and partidaActual.listaJugadores[0].numHundimientos == 12:
        print("Buenas noticias! La partida es un empate")
    elif partidaActual.listaJugadores[1].numHundimientos == 12:
        print("¡Felicidades jugador",0,",has ganado la partida!")
    elif partidaActual.listaJugadores[0].numHundimientos == 12:
        print("¡Felicidades jugador",1,",has ganado la partida!")
    moverNave()
    


