################################################  SEGUNDO PROYECTO PROGRAMADO SEMESTRE I #################################################################
################################################              ELABORADO POR:             #################################################################
################################################          David Molina Guerrero          #################################################################
################################################        Britanny Alvarado Ramírez        #################################################################
##########################################################################################################################################################
#############################################################  Requisitos!! ##############################################################################
#############################################################      PIL      ##############################################################################
############################################################# Customtkinter ##############################################################################
##########################################################################################################################################################
###########################################################  Instalar Fuente:  ###########################################################################
########################################################  Graphics/Basillion.ttf  ########################################################################

# Lamento la carencia de una formal documentación interna, se nos acabó el tiempo...

# Imports
import customtkinter as CTk
from PIL import Image, ImageTk

################################################  Comienzo del código || Clases Globales #################################################################
################################################  Comienzo del código || Clases Globales #################################################################
################################################  Comienzo del código || Clases Globales #################################################################

naveImágenes=[["Naves/b1 (Custom).png"], ["Naves/b22 (Custom).png", "Naves/b21 (Custom).png", ], ["Naves/b33 (Custom).png", "Naves/b32 (Custom).png", "Naves/b31 (Custom).png"], "Naves/b0.png"]

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
        self.numHundimientos = [0,0,0]
        self.navesPorColocar = [6,4,2]
        self.disparoReciente = "x"

class Nave:
    def __init__(self, tipoNave, dirNave, posNave):
        self.defaultNaves = [[1,2],[2,1],[3,1]]
        self.tipoNave = tipoNave
        self.dirNave = dirNave
        self.yPosInicial, self.xPosInicial = posNave[0:]
        self.tamañoNave = self.defaultNaves[tipoNave-1][0]
        self.movimientoMax = self.defaultNaves[tipoNave-1][1]
        self.listaPosTotal = [] # Inicializa totalPos con las posiciones iniciales de la nave
        self.listaPosImpacto = []
        self.numImpactos = 0
        self.hundida = False
        self.puedeMoverMínimo = False

    
    #cambiar de acuerdo a la función
    def moverArriba(self):
        # Se requieren las posiciones de todos los Naves en la matriz.
        # Esto se hace afuera del ciclo principal para solamente armar una vez este gran repositorio de posiciones.
        listaDeTodasLasPosDeTodosLasNaves = []
        for tempJugadores in partidaActual.listaNaves:
            for tempNaves in tempJugadores:
                for tempParOrdenado in tempNaves.listaPosTotal:
                    listaDeTodasLasPosDeTodosLasNaves.append(tempParOrdenado) # Se ingresan todas en esta lista.
        
        #Sin embargo, se deben eliminar las posiciones de la nave actual para que no choque con sí misma.
        for posPropia in self.listaPosTotal:
            listaDeTodasLasPosDeTodosLasNaves.remove(posPropia)
        self.puedeMoverMínimo = False # Esto se utiliza para destructores (cuando solo se mueven 1 celda)
        
        # Ahora estamos listos para comenzar a ciclar y verificar si el movimiento es válido.
        for parOrdenado in self.listaPosTotal:
            for distanciaMax in range(1,self.movimientoMax+1):
                # Revisa que la nave se mueva dentro de la matriz
                if not parOrdenado[0]-(distanciaMax) in range(len(partidaActual.matrizJuego)):
                    #print("Error: La nave no puede moverse más hacia abajo. FUERAMATRIZ")
                    if not self.puedeMoverMínimo:
                        self.dirNave = 1
                        self.yPosInicial -= self.tipoNave-1
                    #self.navesDebug()
                    return
                # Revisa que la nave no choque contra otra
                if [parOrdenado[0]-(distanciaMax),parOrdenado[1]] in listaDeTodasLasPosDeTodosLasNaves:
                    #print("Error: La nave no puede moverse más hacia abajo. CHOQUE")
                    if not self.puedeMoverMínimo:
                        self.dirNave = 1
                        self.yPosInicial -= self.tipoNave-1
                    #self.navesDebug()
                    return
                if self.tipoNave == 1:
                    self.puedeMoverMínimo = True
        
        # Correctamente mueve la nave si se llega hasta esta parte del código sin retornar la función
        for parOrdenado in self.listaPosTotal:
            parOrdenado[0] -= self.movimientoMax
        self.yPosInicial -= self.movimientoMax
        self.puedeMoverMínimo = False
        return True  # Devuelve True para indicar que el movimiento fue exitoso
    

    def moverAbajo(self):
        # Se requieren las posiciones de todas las naves en la matriz.
        # Esto se hace afuera del ciclo principal para solamente armar una vez este gran repositorio de posiciones.
        listaDeTodasLasPosDeTodosLasNaves = []
        for tempJugadores in partidaActual.listaNaves:
            for tempNaves in tempJugadores:
                for tempParOrdenado in tempNaves.listaPosTotal:
                    listaDeTodasLasPosDeTodosLasNaves.append(tempParOrdenado) # Se ingresan todas en esta lista.
        
        #Sin embargo, se deben eliminar las posiciones de la nave actual para que no choque con sí misma.
        for posPropia in self.listaPosTotal:
            listaDeTodasLasPosDeTodosLasNaves.remove(posPropia)
        self.puedeMoverMínimo = False # Esto se utiliza para destructores (cuando solo se mueven 1 celda)
        
        # Ahora estamos listos para comenzar a ciclar y verificar si el movimiento es válido.
        for parOrdenado in self.listaPosTotal:
            for distanciaMax in range(1,self.movimientoMax+1):
                # Revisa que la nave se mueva dentro de la matriz
                if not parOrdenado[0]+(distanciaMax) in range(len(partidaActual.matrizJuego)):
                    #print("Error: La nave no puede moverse más hacia abajo. FUERAMATRIZ")
                    if not self.puedeMoverMínimo:
                        self.dirNave = 3
                        self.yPosInicial += self.tipoNave-1
                    #self.navesDebug()
                    return
                # Revisa que la nave no choque contra otra
                if [parOrdenado[0]+(distanciaMax),parOrdenado[1]] in listaDeTodasLasPosDeTodosLasNaves:
                    #print("Error: La nave no puede moverse más hacia abajo. CHOQUE")
                    if not self.puedeMoverMínimo:
                        self.dirNave = 3
                        self.yPosInicial += self.tipoNave-1
                    #self.navesDebug()
                    return
                if self.tipoNave == 1:
                    self.puedeMoverMínimo = True
                
        for parOrdenado in self.listaPosTotal:
            parOrdenado[0] += self.movimientoMax
        self.yPosInicial += self.movimientoMax
        self.puedeMoverMínimo = False
        return True  # Devuelve True para indicar que el movimiento fue exitoso


    def moverIzquierda(self):
        # Se requieren las posiciones de todos los Naves en la matriz.
        # Esto se hace afuera del ciclo principal para solamente armar una vez este gran repositorio de posiciones.
        listaDeTodasLasPosDeTodosLasNaves = []
        for tempJugadores in partidaActual.listaNaves:
            for tempNaves in tempJugadores:
                for tempParOrdenado in tempNaves.listaPosTotal:
                    listaDeTodasLasPosDeTodosLasNaves.append(tempParOrdenado) # Se ingresan todas en esta lista.
        
        #Sin embargo, se deben eliminar las posiciones de la nave actual para que no choque con sí misma.
        for posPropia in self.listaPosTotal:
            listaDeTodasLasPosDeTodosLasNaves.remove(posPropia)
        self.puedeMoverMínimo = False # Esto se utiliza para destructores (cuando solo se mueven 1 celda)
        
        # Ahora estamos listos para comenzar a ciclar y verificar si el movimiento es válido.
        for parOrdenado in self.listaPosTotal:
            for distanciaMax in range(1,self.movimientoMax+1):
                # Revisa que la nave se mueva dentro de la matriz
                if not parOrdenado[1]-(distanciaMax) in range(len(partidaActual.matrizJuego[0])):
                    #print("Error: La nave no puede moverse más hacia la izquierda. FUERAMATRIZ")
                    if not self.puedeMoverMínimo:
                        self.dirNave = 4
                        self.xPosInicial -= self.tipoNave-1
                    #self.navesDebug()
                    return
                # Revisa que la nave no choque contra otra
                if [parOrdenado[0],parOrdenado[1]-(distanciaMax)] in listaDeTodasLasPosDeTodosLasNaves:
                    #print("Error: La nave no puede moverse más hacia la izquierda. CHOQUE")
                    if not self.puedeMoverMínimo:
                        self.dirNave = 4
                        self.xPosInicial -= self.tipoNave-1
                    #self.navesDebug()
                    return
                # Revisa que las naves no se excedan de sus campos, una nave de jugador 0 no puede cruzar al lado de jugador 1
                if ventanaBatalla.numJugador == 0:
                    if ventanaBatalla.matrizIzquierda.numColumnas <= parOrdenado[1]-(distanciaMax):
                        #print("Error: La nave no puede moverse más hacia la izquierda. CRUZAR CAMPOS JUG1")
                        if not self.puedeMoverMínimo:
                            self.dirNave = 4
                            self.xPosInicial -= self.tipoNave-1
                        #self.navesDebug()
                        return
                # Lo anterior, pero para el jugador 2
                elif ventanaBatalla.matrizIzquierda.numColumnas > parOrdenado[1]-(distanciaMax):
                    #print("Error: La nave no puede moverse más hacia la izquierda. CRUZAR CAMPOS JUG2")
                    if not self.puedeMoverMínimo:
                        self.dirNave = 4
                        self.xPosInicial -= self.tipoNave-1
                    #self.navesDebug()
                    return
                if self.tipoNave == 1:
                    self.puedeMoverMínimo = True # En caso de que se haya podido mover aunque sea 1 cuadro, se guarda esto en la clase
                
        for parOrdenado in self.listaPosTotal:
            parOrdenado[1] -= self.movimientoMax
        self.xPosInicial -= self.movimientoMax
        self.puedeMoverMínimo = False
        return True  # Devuelve True para indicar que el movimiento fue exitoso
    
    def moverDerecha(self):
        # Se requieren las posiciones de todos los Naves en la matriz.
        # Esto se hace afuera del ciclo principal para solamente armar una vez este gran repositorio de posiciones.
        listaDeTodasLasPosDeTodosLasNaves = []
        for tempJugadores in partidaActual.listaNaves:
            for tempNaves in tempJugadores:
                for tempParOrdenado in tempNaves.listaPosTotal:
                    listaDeTodasLasPosDeTodosLasNaves.append(tempParOrdenado) # Se ingresan todas en esta lista.
        
        #Sin embargo, se deben eliminar las posiciones de la nave actual para que no choque con sí misma.
        for posPropia in self.listaPosTotal:
            listaDeTodasLasPosDeTodosLasNaves.remove(posPropia)
        self.puedeMoverMínimo = False # Esto se utiliza para destructores (cuando solo se mueven 1 celda)
        
        # Ahora estamos listos para comenzar a ciclar y verificar si el movimiento es válido.
        for parOrdenado in self.listaPosTotal:
            for distanciaMax in range(1,self.movimientoMax+1):
                # Revisa que la nave se mueva dentro de la matriz
                if not parOrdenado[1]+(distanciaMax) in range(len(partidaActual.matrizJuego[0])):
                    #print("Error: La nave no puede moverse más hacia la derecha. FUERA MATRIZ")
                    if not self.puedeMoverMínimo: # esto le da vuelta a la nave
                        self.dirNave = 2
                        self.xPosInicial += self.tipoNave-1
                    #self.navesDebug()
                    return
                # Revisa que la nave no choque contra otra
                if [parOrdenado[0],parOrdenado[1]+(distanciaMax)] in listaDeTodasLasPosDeTodosLasNaves:
                    #print("Error: La nave no puede moverse más hacia la derecha. CHOQUE!")
                    if not self.puedeMoverMínimo:
                        self.dirNave = 2
                        self.xPosInicial += self.tipoNave-1
                    #self.navesDebug()
                    return
                # Revisa que las naves no se excedan de sus campos, una nave de jugador 0 no puede cruzar al lado de jugador 1
                if ventanaBatalla.numJugador == 0:
                    if ventanaBatalla.matrizIzquierda.numColumnas <= parOrdenado[1]+(distanciaMax):
                        #print("Error: La nave no puede moverse más hacia la derecha. CRUZAR CAMPOS JUG1")
                        if not self.puedeMoverMínimo:
                            self.dirNave = 2
                            self.xPosInicial += self.tipoNave-1
                        #self.navesDebug()
                        return
                # Lo anterior, pero para el jugador 2
                elif ventanaBatalla.matrizIzquierda.numColumnas > parOrdenado[1]+(distanciaMax):
                    #print("Error: La nave no puede moverse más hacia la derecha. CRUZAR CAMPOS JUG2")
                    if not self.puedeMoverMínimo:
                        self.dirNave = 2
                        self.xPosInicial += self.tipoNave-1
                    #self.navesDebug()
                    return
                if self.tipoNave == 1:
                    self.puedeMoverMínimo = True # En caso de que se haya podido mover aunque sea 1 cuadro, se guarda esto en la clase
                
        for parOrdenado in self.listaPosTotal:
            parOrdenado[1] += self.movimientoMax
        self.xPosInicial += self.movimientoMax
        self.puedeMoverMínimo = False
        return True  # Devuelve True para indicar que el movimiento fue exitoso

################################################  Comienzo del código de selección de partida #################################################################
################################################  Comienzo del código de selección de partida #################################################################
################################################  Comienzo del código de selección de partida #################################################################

# Esta es la clase de la app principal, para más información de clases vea los comentarios anteriores o pregúnteme jeje
class selecciónApp(CTk.CTk):
    def __init__(self):
        #######################################################
        ##    Código que crea la ventana principal con CTk   ##
        #######################################################
        super().__init__()
        self.title("Selección de Partida")
        self.configure(fg_color="#CDE8F4")
        self.geometry("1650x950+125+25")
        self.estadoMensaje = "Escoger Tablero" # Este string se usa como mensaje de error variable para varios botones
        #######################################################
        ##   Código dedicado a interfaz, realizada con CTk   ##
        #######################################################
        self.grid_columnconfigure((0,1,2), weight=0)
        self.grid_rowconfigure((0,1,2,3,4), weight=0)
        self.grid_columnconfigure((0,1,2), weight=1)
        self.grid_rowconfigure((0,1,2), weight=1)
        self.imagenTítulo = CTk.CTkLabel(self, text=None, image=CTk.CTkImage(Image.open("Graphics/Title.png"), size=(1291, 342)))
        self.imagenTítulo.grid(row=0, column=0, columnspan=3, sticky="ew")
        self.fuenteTexto = CTk.CTkFont(family="Basillion",size=35)
        self.btnPartidaNueva = CTk.CTkButton(self,fg_color="#023047",hover_color="#FF961F", text="Nueva Partida", width=350, height=150, font=self.fuenteTexto, corner_radius=8, command=self.abrirNuevaPartida)
        self.btnPartidaNueva.grid(row=1, column=0,sticky="ew")
        self.btnCargarPartida = CTk.CTkButton(self,fg_color="#023047",hover_color="#FF961F", text="Cargar Partida", width=350, height=150, font=self.fuenteTexto, corner_radius=8, command=self.preCargarPartida)
        self.btnCargarPartida.grid(row=1, column=2,sticky="ew") 
        
    def abrirNuevaPartida(self):
        ########################################################
        # Se ha determinado que vamos a hacer una nueva partida
        # Se globaliza para transmitirla a la ventana batalla
        global partidaActual 
        partidaActual = Partida([],[[],[]],[])
        ########################################################
        ##  Código para ELIMINAR menu viejo y mostrar nuevo  ###
        ########################################################
        self.btnCargarPartida.destroy()
        self.imagenTítulo.destroy()
        self.btnPartidaNueva.destroy()
        self.grid_columnconfigure((2), weight=0)
        ########################################################
        ##   Código dedicado a interfaz, realizada con CTk   ###
        ########################################################
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure((0,1,2,3,4), weight=1)
        self.fuenteTextoGrande = CTk.CTkFont(family="Basillion",size=95)
        self.fuenteTextoPequeño = CTk.CTkFont(family="Basillion",size=15)
        self.jugadorTexto1 = CTk.CTkLabel(self, text="Jugador 1", font=self.fuenteTextoGrande, text_color="#023047")
        self.jugadorTexto1.grid(column=0, row=0, padx=150, pady=(65,10), sticky="w")
        self.jugadorTexto2 = CTk.CTkLabel(self, text="Jugador 2", font=self.fuenteTextoGrande, text_color="#023047")
        self.jugadorTexto2.grid(column=1, row=0, padx=150, pady=(65,10), sticky="e")
        self.entradaJugador1A = CTk.CTkEntry(self, font=self.fuenteTextoPequeño,placeholder_text="Nombre del Jugador 1", width=350, height=50)
        self.entradaJugador1A.grid(column=0, row=1, padx=190, pady=0, sticky="w")
        self.entradaJugador1B = CTk.CTkEntry(self, font=self.fuenteTextoPequeño,placeholder_text="Nickname del Jugador 1", width=350, height=50)
        self.entradaJugador1B.grid(column=0, row=2, padx=190, pady=0, sticky="w")
        self.entradaJugador2A = CTk.CTkEntry(self, font=self.fuenteTextoPequeño,placeholder_text="Nombre del Jugador 2", width=350, height=50)
        self.entradaJugador2A.grid(column=1, row=1, padx=190, pady=0, sticky="e")
        self.entradaJugador2B = CTk.CTkEntry(self, font=self.fuenteTextoPequeño,placeholder_text="Nickname del Jugador 2", width=350, height=50)
        self.entradaJugador2B.grid(column=1, row=2, padx=190, pady=0, sticky="e")
        self.btnEscogerTablero = CTk.CTkButton(self,fg_color="#023047",
                                               hover_color="#FF961F",
                                               text=self.estadoMensaje,
                                               width=350,
                                               height=150,
                                               font=self.fuenteTexto,
                                               corner_radius=0,
                                               command=self.preEscogerTablero)
        self.btnEscogerTablero.grid(row=4, column=0, columnspan=2, sticky="ew")

    def preEscogerTablero(self):
        self.estadoMensaje = "Escoger Tablero" if self.estadoMensaje == "Nombres Incompletos!" else "Escoger Tablero"
        self.btnEscogerTablero.configure(text=self.estadoMensaje)
        # Lista Nombres es la lista del nombre y nickname de cada jugador en el siguiente orden: [nom1,nick1,nom2,nick2]
        listaNombres = self.getNombres()
        for entrada in listaNombres:
            if entrada[0] in ["", " ", "  "] or entrada[1] in ["", " ", "  "]:
                self.estadoMensaje = "Nombres Incompletos!" if self.estadoMensaje == "Escoger Tablero" else "Escoger Tablero"
                self.btnEscogerTablero.configure(text=self.estadoMensaje)
                return
        partidaActual.listaJugadores = listaNombres
        self.mostrarEscogerTablero()


    def mostrarEscogerTablero(self):
        #######################################################
        ##  Código para ELIMINAR menu viejo y mostrar nuevo  ##
        #######################################################
        self.jugadorTexto1.destroy()
        self.jugadorTexto2.destroy()
        self.entradaJugador1A.destroy()
        self.entradaJugador1B.destroy()
        self.entradaJugador2A.destroy()   
        self.entradaJugador2B.destroy()
        self.btnEscogerTablero.destroy()
        self.grid_columnconfigure((1,2), weight=0)
        #######################################################
        ##   Código dedicado a interfaz, realizada con CTk   ##
        #######################################################
        self.grid_columnconfigure((0), weight=1)
        self.grid_rowconfigure((0,1,2,3,4), weight=1)
        self.estadoMensaje = "Iniciar Partida"
        self.textoTamañoTrabajo = CTk.CTkLabel(self, text="Escoger Tablero", font=self.fuenteTextoGrande, text_color="#023047")
        self.textoTamañoTrabajo.grid(column=0, row=0, padx=150, pady=65, sticky="ew")
        self.entradaFilas = CTk.CTkEntry(self, font=self.fuenteTextoPequeño,placeholder_text="Filas", width=100, height=50)
        self.entradaFilas.grid(column=0, row=1, padx=150, pady=0)
        self.botónX = CTk.CTkButton(self,fg_color="#000000",hover_color="#000000", text="x", width=35, height=50, font=self.fuenteTexto, corner_radius=40)
        self.botónX.grid(column=0, row=2, padx=350, pady=15)
        self.entradaColumnas = CTk.CTkEntry(self, font=self.fuenteTextoPequeño, placeholder_text="Columnas", width=100, height=50)
        self.entradaColumnas.grid(column=0, row=3, padx=150, pady=0)
        self.btnIniciarPartida = CTk.CTkButton(self, fg_color="#023047",
                                               hover_color="#FF961F",
                                               text=self.estadoMensaje,
                                               width=250,
                                               height=150,
                                               font=self.fuenteTexto,
                                               corner_radius=0,
                                               command=self.preIniciarPartida)
        self.btnIniciarPartida.grid(column=0, row=4, padx=0, pady=0, sticky="ew")

    def preCargarPartida(self):
        self.btnCargarPartida.destroy()
        self.imagenTítulo.destroy()
        self.btnPartidaNueva.destroy()
        self.grid_columnconfigure((0,1,2,3,4), weight=1)
        self.grid_rowconfigure((0,1,2,3,4), weight=1)
        self.frameCubierta = CTk.CTkFrame(self,width=200,height=200,corner_radius=0,fg_color="#023047")
        self.frameCubierta.grid(column=0, row=0, padx=0, pady=0, sticky="nsew", columnspan=5, rowspan=5)
        self.entradaArchivo = CTk.CTkEntry(self, font=self.fuenteTexto, placeholder_text="Nombre del Archivo", width=450, height=80)
        self.entradaArchivo.grid(column=1, row=1, columnspan=3, padx=50, pady=20, sticky="ew")
        self.btnCubiertaCargar = CTk.CTkButton(self, fg_color="#101010",
                                         anchor="center",
                                         hover_color="#222222",
                                         bg_color="#023047",
                                         text="Cargar Partida",
                                         #text_color="#",
                                         width=650,
                                         height=90,
                                         font=self.fuenteTexto,
                                         corner_radius=50,
                                         command=self.cargarPartida)
        self.btnCubiertaCargar.grid(column=1, row=2, padx=0, pady=0, columnspan=3)
        self.frameCubierta.tkraise()
        self.entradaArchivo.tkraise()
        self.btnCubiertaCargar.tkraise()
    
    def cargarPartida(self):
        try:
            nombreArchivo = self.entradaArchivo.get()
            nombreArchivo = nombreArchivo.lower()
            #print(f"{nombreArchivo}.txt")
            archivoCargado = open(f"{nombreArchivo}.txt","r")
        except FileNotFoundError:
            self.btnCubiertaCargar.configure(text="No existe!")
            return
        líneasGuardadas = archivoCargado.readlines()
        datosDivididos = [[],[],[],[]]
        contadorDatos = -1
        contadorIndex = -1
        for línea in líneasGuardadas:
            línea = línea.strip()
            if contadorDatos >= 4:
                break
            elif línea == "#!":
                contadorDatos += 1
                contadorIndex = -1
            elif línea == "-":
                contadorIndex += 1
                datosDivididos[contadorDatos].append([])
            else:
                datosDivididos[contadorDatos][contadorIndex].append(línea)
        for Jugadores in datosDivididos[0]:
            print("Jugador", Jugadores)
        for naves1 in datosDivididos[1]:
            print("nave1", naves1)
        for naves1 in datosDivididos[2]:
            print("nave2",naves1)
        for filasMatriz in datosDivididos[3]:
            print("fila",filasMatriz)
        print("=================================")
        global partidaActual 
        partidaActual = Partida([],[[],[]],[])
        for jugador in range(2):
            subContador = 0
            partidaActual.listaJugadores.append(Jugador("",""))
            partidaActual.listaJugadores[jugador].realName = datosDivididos[0][jugador][0]
            partidaActual.listaJugadores[jugador].nickName = datosDivididos[0][jugador][1]
            partidaActual.listaJugadores[jugador].tirosAcertados = int(datosDivididos[0][jugador][2])
            partidaActual.listaJugadores[jugador].tirosFallidos = int(datosDivididos[0][jugador][3])
            partidaActual.listaJugadores[jugador].numHundimientos = datosDivididos[0][jugador][4].split(",")
            for x in partidaActual.listaJugadores[jugador].numHundimientos: x = int(x.strip("[]"))
            partidaActual.listaJugadores[jugador].navesPorColocar = datosDivididos[0][jugador][5].split(",")
            for x in partidaActual.listaJugadores[jugador].navesPorColocar: x = int(x.strip("[]"))
            partidaActual.listaJugadores[jugador].disparoReciente = datosDivididos[0][jugador][6].split(",")
            for x in partidaActual.listaJugadores[jugador].disparoReciente: x = int(x.strip("[]"))
            subContador += 1             
            for nave in range(len(datosDivididos[jugador+1])):
                print("??????????????????????")
                subContador = 0
                partidaActual.listaNaves[jugador].append(Nave(0,1,(1,1)))
                partidaActual.listaNaves[jugador][subContador].defaultNaves = [[1, 2], [2, 1], [3, 1]]
                partidaActual.listaNaves[jugador][subContador].tipoNave = int(datosDivididos[jugador+1][nave][1])
                partidaActual.listaNaves[jugador][subContador].dirNave = int(datosDivididos[jugador+1][nave][2])
                partidaActual.listaNaves[jugador][subContador].yPosInicial = int(datosDivididos[jugador+1][nave][3])
                partidaActual.listaNaves[jugador][subContador].xPosInicial = int(datosDivididos[jugador+1][nave][4])
                partidaActual.listaNaves[jugador][subContador].tamañoNave = int(datosDivididos[jugador+1][nave][1])
                partidaActual.listaNaves[jugador][subContador].movimientoMax = partidaActual.listaNaves[jugador][subContador].defaultNaves[int(datosDivididos[jugador+1][nave][1])-1][1]
                partidaActual.listaNaves[jugador][subContador].listaPosTotal = datosDivididos[jugador+1][nave][7]
                print("aw :(",partidaActual.listaNaves[jugador][subContador].listaPosTotal)
                tempString = ""
                appendCount=0
                tempBooleanoComa = False
                verdaderoListaPosTotal = [[]]
                for x in partidaActual.listaNaves[jugador][subContador].listaPosTotal:
                    x = x.strip("[]")
                    print("hey!", x)
                    if tempBooleanoComa and x == ",": 
                        verdaderoListaPosTotal[appendCount].append(int(tempString.split(",")[0]))
                        verdaderoListaPosTotal[appendCount].append(int(tempString.split(",")[1]))
                        verdaderoListaPosTotal.append([])
                        appendCount+=1
                        tempString = ""
                        tempBooleanoComa = False
                    elif x == ",":
                        tempBooleanoComa = True
                        tempString += ","
                    elif x:
                        tempString += x
                if len(tempString) > 2:
                    verdaderoListaPosTotal.append([])
                    verdaderoListaPosTotal[appendCount].append(int(tempString.split(",")[0]))
                    verdaderoListaPosTotal[appendCount].append(int(tempString.split(",")[1]))
                print(verdaderoListaPosTotal[:-1])
                partidaActual.listaNaves[jugador][subContador].listaPosTotal = verdaderoListaPosTotal[:-1]
                partidaActual.listaNaves[jugador][subContador].listaPosImpacto = datosDivididos[jugador+1][nave][8]
                print("aw :)",partidaActual.listaNaves[jugador][subContador].listaPosImpacto)
                tempString = ""
                appendCount=0
                tempBooleanoComa = False
                verdaderoListaPosImpacto = [[]]
                for x in partidaActual.listaNaves[jugador][subContador].listaPosImpacto:
                    x = x.strip("[]")
                    print("hey!", x)
                    if tempBooleanoComa and x == ",": 
                        verdaderoListaPosImpacto[appendCount].append(int(tempString.split(",")[0]))
                        verdaderoListaPosImpacto[appendCount].append(int(tempString.split(",")[1]))
                        verdaderoListaPosImpacto.append([])
                        appendCount+=1
                        tempString = ""
                        tempBooleanoComa = False
                    elif x == ",":
                        tempBooleanoComa = True
                        tempString += ","
                    elif x:
                        tempString += x
                if len(tempString) > 2:
                    verdaderoListaPosImpacto.append([])
                    verdaderoListaPosImpacto[appendCount].append(int(tempString.split(",")[0]))
                    verdaderoListaPosImpacto[appendCount].append(int(tempString.split(",")[1]))
                print(verdaderoListaPosImpacto[:-1])
                partidaActual.listaNaves[jugador][subContador].listaPosImpacto = verdaderoListaPosImpacto[:-1]
                partidaActual.listaNaves[jugador][subContador].numImpactos = int(datosDivididos[jugador+1][nave][9])
                partidaActual.listaNaves[jugador][subContador].hundida = eval(datosDivididos[jugador+1][nave][10])
                partidaActual.listaNaves[jugador][subContador].puedeMoverMínimo = eval(datosDivididos[jugador+1][nave][11])
                subContador += 1 
        partidaActual.matrizJuego = datosDivididos[3][0]
 

        archivoCargado.close()
        self.destroy() # Para salir a la ventana de batalla.
        """
        class Jugador:
            def __init__(self, realName, nickName):
                self.realName = realName
                self.nickName = nickName
                self.tirosAcertados = 0
                self.tirosFallidos = 0
                self.numHundimientos = [0,0,0]
                self.navesPorColocar = [1,1,1]
                self.disparoReciente = "x"

        class Nave:
            def __init__(self, tipoNave, dirNave, posNave):
                self
                self
                self
                self
                self
                self
                self
                self
                self
                self
                self
                self
        """



        

    def preIniciarPartida(self):
        try:
            # En caso de haber cambiado el mensaje del texto, esto lo revierte a su estado original
            self.estadoMensaje = "Iniciar Partida" if self.estadoMensaje == "Nombres Incompletos!" else "Iniciar Partida"
            self.btnIniciarPartida.configure(text=self.estadoMensaje)
            # Lista Nombres es la lista del nombre y nickname de cada jugador en el siguiente orden: [nom1,nick1,nom2,nick2]
            tamañoMatriz = self.getMatriz()
            for i in range(2):
                tamañoMatriz[i] = int(tamañoMatriz[i])
            for entrada in tamañoMatriz:
                if entrada in ["", " ", "  "]:
                    self.estadoMensaje = "Matriz Incompleta!" if self.estadoMensaje == "Iniciar Partida" else "Iniciar Partida"
                    self.btnIniciarPartida.configure(text=self.estadoMensaje)
                    return
                if int(entrada) % 2 != 0:
                    self.estadoMensaje = "Matriz Impar!" if self.estadoMensaje == "Iniciar Partida" else "Iniciar Partida"
                    self.btnIniciarPartida.configure(text=self.estadoMensaje)
                    return
            if tamañoMatriz[0] < 10 or tamañoMatriz[1] < 20:
                self.estadoMensaje = "Matriz muy chiquitica! (Al menos 10 filas con 20 columnas)" 
                self.btnIniciarPartida.configure(text=self.estadoMensaje)
                return
            partidaActual.matrizJuego = tamañoMatriz
            self.iniciarPartida()

        except ValueError:
            self.btnIniciarPartida.configure(text="Matriz Incompleta!")
            return

    def getMatriz(self):
        listaMatrizInterfaz = [str(self.entradaFilas.get()), str(self.entradaColumnas.get())]
        return listaMatrizInterfaz

    def getNombres(self):
        listaJugadoresInterfaz = [[str(self.entradaJugador1A.get()), str(self.entradaJugador1B.get())], [str(self.entradaJugador2A.get()), str(self.entradaJugador2B.get())]]
        return listaJugadoresInterfaz
    
    def iniciarPartida(self):
        #######################################################
        ## !! Código para ELIMINAR VENTANA  !! ################
        self.destroy() ########################################
        #######################################################
        

################################################  Comienzo del código de batalla #################################################################
################################################  Comienzo del código de batalla #################################################################
################################################  Comienzo del código de batalla #################################################################

class interfazTipoNave(CTk.CTkFrame):
    # Al iniciarse la matriz pide los argumentos de master (la ventana principal) y del color del foreground de los botones (fgColor)
    def __init__(self, master):
        super().__init__(master) 
        self.configure(width=100, height=600, corner_radius=24, bg_color="#CDE8F4", fg_color="#CDE8F4")
        self.rowconfigure((0,1,2), weight=1)
        self.columnconfigure(0, weight=1)
        self.btnDestructor = CTk.CTkButton(self, fg_color="#CDE8F4",
                                           anchor="center",
                                           hover_color="#99C8DD",
                                           bg_color="#CDE8F4",
                                           text=None,
                                           width=100,
                                           height=100,
                                           image=CTk.CTkImage(Image.open("Naves/destructorIcon.png"), size=(100,100)),
                                           corner_radius=20,
                                           command=lambda a=1: self.setTipoNaveInterfaz(a))
        self.btnDestructor.grid(row=0, pady=10)
        self.btnCrucero = CTk.CTkButton(self, fg_color="#CDE8F4",
                                           anchor="center",
                                           hover_color="#99C8DD",
                                           bg_color="#CDE8F4",
                                           text=None,
                                           width=100,
                                           height=100,
                                           image=CTk.CTkImage(Image.open("Naves/cruceroIcon.png"), size=(100,100)),
                                           corner_radius=20,
                                           command=lambda a=2: self.setTipoNaveInterfaz(a))
        self.btnCrucero.grid(row=1, pady=10)
        self.btnAcorazado = CTk.CTkButton(self, fg_color="#CDE8F4",
                                           anchor="center",
                                           hover_color="#99C8DD",
                                           bg_color="#CDE8F4",
                                           text=None,
                                           width=100,
                                           height=100,
                                           image=CTk.CTkImage(Image.open("Naves/acorazadoIcon.png"), size=(100,100)),
                                           corner_radius=20,
                                           command=lambda a=3: self.setTipoNaveInterfaz(a))
        self.btnAcorazado.grid(row=2, pady=10)
    
    def setTipoNaveInterfaz(self, tipoNave):
        listaBotones = [self.btnDestructor, self.btnCrucero, self.btnAcorazado]
        for num in range(3):
            if num+1 != tipoNave:
                listaBotones[num].configure(fg_color="#CDE8F4")
            else:
                listaBotones[num].configure(fg_color="#023047")
        

    def getTipoNave(self):
        listaBotones = [self.btnDestructor, self.btnCrucero, self.btnAcorazado]
        for num in range(3):
            if listaBotones[num].cget("fg_color") == "#023047":
                return num+1
        return False


# Se crea una clase de cuadrícula para crear 2 matrices sin tener que repetir código
# Hereda atributos de una clase padre: "CTk.CTkFrame"
# Un frame es una especie de contenedor para otros objetos, (como el panel gris que está detrás de los botones, conteniendo la matriz de botones en su interior)
class interfazMatriz(CTk.CTkFrame):
    # Al iniciarse la matriz pide los argumentos de master (la ventana principal) y del color del foreground de los botones (fgColor)
    def __init__(self, master, fgColor, numJugador):
        # En la documentación dice que se debe hacer esta siguiente línea, porque inicializa la clase padre de esta clase.
        # Es decir, sin esta línea, la clase "interfazMatriz" no tendría los poderes de un "CTk.CTkFrame", que es lo que deseamos para contener los botones
        super().__init__(master) 
        # Se crean 10 columnas con weight=1, que les dice que tomen el espacio que necesiten
        self.espacioCuadros = 0
        self.varDirElegida = CTk.StringVar()
        self.jugadorDeEstaMatriz = numJugador
        self.celdaReciente = []
        self.colorReciente = ""
        self.numColumnas = len(partidaActual.matrizJuego[0]) // 2
        self.numFilas = len(partidaActual.matrizJuego)
        self.tamañoBotones = (675 // self.numColumnas) * 0.65
        self.configure(width=self.tamañoBotones * self.numColumnas, height=self.tamañoBotones * self.numFilas)
        self.matrizInicial = [[0] * self.numColumnas for _ in range(self.numFilas)]
        self.grid_columnconfigure(tuple(range(self.numColumnas)), weight=1) #se hace un range, y el range se convierte en una tupla porque solo acepta tuplas ese primer argumento
        
        # Se crean 10 filas con weight=1, que les dice que tomen el espacio que necesiten
        self.grid_rowconfigure(tuple(range(self.numFilas)), weight=1)
        self.matrizDesplegada = []

        # Se agregan las filas a la matriz
        for i in range(self.numFilas):
            self.matrizDesplegada.append([])
            # Por cada fila se rellenan las columnas con 10 botones
            for j in range(self.numColumnas):
                # El botón debe ser metido en la lista de matrizDesplegada 
                # Se le deben asignar atributos al crearlo con "CTk.CTkButton()"
                # Los argumentos que yo le dí aquí son respectivamente: 
                #CTk.CTkButton(objeto que es dueño de este botón, tamaño del borde redondeado, 
                #                        texto que representa las coordenadas en la matriz, ancho del botón, 
                #                        alto del botón, color del botón (fg = foreground), 
                #                        inicializar la imágen vacía, y la acción que hace al presionarse (lambda con dos argumentos metidos en una tupla para llamar la función)
                # hay más argumentos, pero por defecto tienen valores que me sirven
                # Por ejemplo: Al poner el mouse por encima se resalta en azul
                self.matrizDesplegada[-1].append(CTk.CTkButton(self, corner_radius=4,
                                                               text=None,
                                                               image=CTk.CTkImage(Image.open(naveImágenes[-1]),
                                                               size=(self.tamañoBotones, self.tamañoBotones)),
                                                               width=self.tamañoBotones,
                                                               height=self.tamañoBotones,
                                                               fg_color=fgColor,
                                                               command=lambda a=(i, j): self.presionarBotón(a[0],a[1])))
                # Antes de explicar lo que hice a continuación, hay que explicar "padding"
                # Usted puede establecer "padx" y "pady" que son los pixeles de espacio personal que tiene el objeto
                # Nadie se va a acercar a ese widget hasta después de esa cantidad de pixeles.
                # En este caso, los botones tienen padx=2 y pady=2 para que guarden distancia de 2 pixeles entre sí mismos, para que no se vean tan pegados
                # Al final de esta línea de código está el argumento "sticky", que hace que se distribuyan en las direcciones cardinales que contenga el string
                # Como en este string están todas las iniciales de las direcciones cardinales, se distribuye en las 4 direcciones (north, south, east, west = "nsew")
                self.matrizDesplegada[-1][-1].grid(row=i,column=j,padx=self.espacioCuadros,pady=self.espacioCuadros, sticky="nsew") 

        # Sin este siguiente cuadro de código el programa todavía funciona, pero no tendría el bordecito gris lindo que hay a los bordes donde terminan los botones.
        # Básicamente ciclo por todas las laterales de la matriz de botones y les digo que guarden un padding de 20 según la direccion a la que se encuentra el final
        # Este ciclo para filas
        for i in range(self.numFilas):
            self.matrizDesplegada[i][0].grid(row=i,column=0,padx=(20,self.espacioCuadros),pady=(self.espacioCuadros,self.espacioCuadros), sticky="nsew")
            self.matrizDesplegada[i][-1].grid(row=i,column=self.numColumnas-1,padx=(self.espacioCuadros,20),pady=(self.espacioCuadros,self.espacioCuadros), sticky="nsew")
        # Este ciclo para columnas
        for i in range(self.numColumnas):
            self.matrizDesplegada[0][i].grid(row=0,column=i,padx=(self.espacioCuadros,self.espacioCuadros),pady=(20,self.espacioCuadros), sticky="nsew")
            self.matrizDesplegada[-1][i].grid(row=self.numFilas-1,column=i,padx=(self.espacioCuadros,self.espacioCuadros),pady=(self.espacioCuadros,20), sticky="nsew")
        # Estos 4 casos excepcionales para las esquinas, que deben tener padding a dos lados diferentes
        self.matrizDesplegada[0][0].grid(row=0,column=0,padx=(20,self.espacioCuadros),pady=(20,self.espacioCuadros), sticky="nsew")
        self.matrizDesplegada[self.numFilas-1][self.numColumnas-1].grid(row=self.numFilas-1,column=self.numColumnas-1,padx=(self.espacioCuadros,20),pady=(self.espacioCuadros,20), sticky="nsew")
        self.matrizDesplegada[0][self.numColumnas-1].grid(row=0,column=self.numColumnas-1,padx=(self.espacioCuadros,20),pady=(20,self.espacioCuadros), sticky="nsew")
        self.matrizDesplegada[self.numFilas-1][0].grid(row=self.numFilas-1,column=0,padx=(20,self.espacioCuadros),pady=(self.espacioCuadros,20), sticky="nsew")
        # Y listo, cuando se vaya a crear la clase con "interfazMatriz(argumentosAquí)" todo este código corre para que exista una nueva cuadrícula de botones

    
    ###################################################################################
    # presionarBotón(self,i,j) ejecuta las acciones adecuadas para cada tipo de botón #
    # se encarga de que funcione para colocar, direccionar y atacar                   #
    ###################################################################################


    def presionarBotón(self,i,j):
        #print(ventanaBatalla.modoMatriz)
        if ventanaBatalla.modoMatriz in ["colocar", "direccionar", "NINGUNA"]:
            if ventanaBatalla.numJugador == self.jugadorDeEstaMatriz:
                if ventanaBatalla.frameSelecciónNave.getTipoNave() != False:
                    if ventanaBatalla.modoMatriz == "colocar":
                        ventanaBatalla.modoMatriz = "direccionar"
                        ventanaBatalla.labelMensaje.configure(text="Indique el sentido de la cola de la nave")
                        self.celdaReciente = [i,j]
                        self.celdaActual = [i,j]
                        self.colorReciente = "#77A6BB"
                        self.resaltarDireccionarToggle()
                        self.wait_variable(self.varDirElegida)
                        if self.varDirElegida.get() == "0":
                            self.resaltarDireccionarToggle()
                            #print("going back!")
                            ventanaBatalla.modoMatriz = "colocar"
                            return
                        else:
                            self.resaltarDireccionarToggle()
                            dirNave = self.varDirElegida.get()
                            tipoNave = ventanaBatalla.frameSelecciónNave.getTipoNave()
                            #se transmite en un string separado por comas:
                            #tipoNave, dirNave, yPosInicial(i), xPosInicial(j)
                            variableTransmitida = ""
                            variableTransmitida += str(tipoNave)
                            variableTransmitida += ","+str(dirNave)
                            variableTransmitida += ","+str(i)
                            variableTransmitida += ","+str(j)
                            ventanaBatalla.varNaveColocada.set(variableTransmitida)
                            ventanaBatalla.modoMatriz = "colocar"
                    elif ventanaBatalla.modoMatriz == "direccionar":
                        y, x = self.celdaReciente[0], self.celdaReciente[1]
                        if [i, j] == [y-1,x]:
                            return self.varDirElegida.set("1")
                        elif [i, j] == [y+1,x]:
                            return self.varDirElegida.set("3")
                        elif [i, j] == [y,x+1]:
                            return self.varDirElegida.set("2")
                        elif [i, j] == [y,x-1]:
                            return self.varDirElegida.set("4")
                        else:
                            ventanaBatalla.labelMensaje.configure(text="Posicionamiento Cancelado!")
                            return self.varDirElegida.set("0")
                    else:
                        ventanaBatalla.labelMensaje.configure(text="Su turno ya pasó!")
                else:
                    ventanaBatalla.labelMensaje.configure(text="Seleccione un tipo de Nave!")
            else:
                ventanaBatalla.labelMensaje.configure(text="Matriz equivocada!")
        elif ventanaBatalla.modoMatriz == "atacar":
            if ventanaBatalla.numJugador != self.jugadorDeEstaMatriz:
                variableTransmitida = ""
                variableTransmitida += str(i)
                variableTransmitida += ","+str(j)
                ventanaBatalla.varNaveColocada.set(variableTransmitida)
                ventanaBatalla.modoMatriz == "NINGUNA"
            else:
                ventanaBatalla.labelMensaje.configure(text="Matriz equivocada!")

    def resaltarDireccionarToggle(self):
        self.colorReciente = "#77A6BB" if self.colorReciente != "#77A6BB" else "#67AE5B"
        if 0 <= self.celdaActual[0]+1 and self.celdaActual[0]+1 < len(self.matrizDesplegada):
            self.matrizDesplegada[self.celdaActual[0]+1][self.celdaActual[1]].configure(fg_color=self.colorReciente)
        if 0 <= self.celdaActual[0]-1 and self.celdaActual[0]-1 < len(self.matrizDesplegada):
            self.matrizDesplegada[self.celdaActual[0]-1][self.celdaActual[1]].configure(fg_color=self.colorReciente)
        if 0 <= self.celdaActual[1]+1 and self.celdaActual[1]+1 < len(self.matrizDesplegada[0]):
            self.matrizDesplegada[self.celdaActual[0]][self.celdaActual[1]+1].configure(fg_color=self.colorReciente)
        if 0 <= self.celdaActual[1]-1 and self.celdaActual[1]-1 < len(self.matrizDesplegada[0]):
            self.matrizDesplegada[self.celdaActual[0]][self.celdaActual[1]-1].configure(fg_color=self.colorReciente)
        
    def resaltarImpactos(self, esDerecha, numJugador):
        try:
            for nave in partidaActual.listaNaves[numJugador]:
                for parOrdenado in nave.listaPosImpacto:
                    y, x = parOrdenado[:]
                    self.matrizDesplegada[y][x-esDerecha].configure(fg_color="#FA4F00") # Configura el botón para que sea solo texto
                    self.matrizDesplegada[y][x-esDerecha].configure(True, width=self.tamañoBotones) # Se actualiza el tamaño del botón, colocando true para que se refresque y aparezca la imagen.
                    self.matrizDesplegada[y][x-esDerecha].configure(True, height=self.tamañoBotones) # Se actualiza el tamaño del botón, colocando true para que se refresque y aparezca la imagen.
            if partidaActual.listaJugadores[0 if (numJugador+1) != 1 else 1].disparoReciente != "x": # Si existe un disparo enemigo reciente, se despliega
                    y, x = partidaActual.listaJugadores[0 if (numJugador+1) != 1 else 1].disparoReciente[:]
                    if self.matrizDesplegada[y][x-esDerecha].cget("fg_color") != "#FA4F00":
                        self.matrizDesplegada[y][x-esDerecha].configure(fg_color="#FFB999") # Configura el botón para que sea solo texto
                        self.matrizDesplegada[y][x-esDerecha].configure(True, width=self.tamañoBotones) # Se actualiza el tamaño del botón, colocando true para que se refresque y aparezca la imagen.
                        self.matrizDesplegada[y][x-esDerecha].configure(True, height=self.tamañoBotones) # Se actualiza el tamaño del botón, colocando true para que se refresque y aparezca la imagen.
        except TypeError:
            return

    def actualizarMatrizParaJugadorActual(self, esDerecha):
        for nave in partidaActual.listaNaves[ventanaBatalla.numJugador]:
            for i in range(nave.tipoNave):
                #print("actualizando P/TN", ventanaBatalla.numJugador, nave.tipoNave)
                # Hace un nuevo objeto de imagen CTkImage y abre la imagen con PIL.Image.open()...(solo "Image" aquí por como se importó)
                gradosRotación = [-90,180,90,0]
                buttonImage = CTk.CTkImage(Image.open(naveImágenes[nave.tipoNave-1][i]).rotate(gradosRotación[nave.dirNave-1]), size=(self.tamañoBotones,self.tamañoBotones))
                direccionesPosibles = [[0, 1],[-1, 0],[0,-1],[1, 0]] 
                factorDirX, factorDirY = direccionesPosibles[nave.dirNave - 1] 
                y, x = nave.yPosInicial, nave.xPosInicial
                #print((y+(i*factorDirY),x+(i*factorDirX)-esDerecha))
                self.matrizDesplegada[y+(i*factorDirY)][x+(i*factorDirX)-esDerecha].configure(text="") # Configura el botón para que sea solo texto
                self.matrizDesplegada[y+(i*factorDirY)][x+(i*factorDirX)-esDerecha].configure(image=buttonImage) # Se coloca la imagen en el botón
                self.matrizDesplegada[y+(i*factorDirY)][x+(i*factorDirX)-esDerecha].configure(fg_color="#77A6BB")
                self.matrizDesplegada[y+(i*factorDirY)][x+(i*factorDirX)-esDerecha].configure(True, width=self.tamañoBotones) # Se actualiza el tamaño del botón, colocando true para que se refresque y aparezca la imagen.
                self.matrizDesplegada[y+(i*factorDirY)][x+(i*factorDirX)-esDerecha].configure(True, height=self.tamañoBotones) # Se actualiza el tamaño del botón, colocando true para que se refresque y aparezca la imagen.
        ventanaBatalla.matrizDerecha.resaltarImpactos(esDerecha, 1)
        ventanaBatalla.matrizIzquierda.resaltarImpactos(esDerecha, 0)


    #Versión vieja de ocultarTodaMatriz
    # Imita la función anterior pero oculta las imágenes del oponente
    def ocultarTodaMatriz(self, esDerecha):
        numJugador = 0
        esDerecha = 0
        for nave in partidaActual.listaNaves[numJugador]:
            for i in range(nave.tipoNave):
                direccionesPosibles = [[0, 1],[-1, 0],[0,-1],[1, 0]] 
                factorDirX, factorDirY = direccionesPosibles[nave.dirNave - 1] 
                y, x = nave.yPosInicial, nave.xPosInicial
                ventanaBatalla.matrizIzquierda.matrizDesplegada[y+(i*factorDirY)][x+(i*factorDirX)-esDerecha].configure(text="") # Configura el botón para que sea solo texto
                ventanaBatalla.matrizIzquierda.matrizDesplegada[y+(i*factorDirY)][x+(i*factorDirX)-esDerecha].configure(image=CTk.CTkImage(Image.open(naveImágenes[-1]),size=(self.tamañoBotones, self.tamañoBotones))) # Se coloca la imagen vacía en el botón
                ventanaBatalla.matrizIzquierda.matrizDesplegada[y+(i*factorDirY)][x+(i*factorDirX)-esDerecha].configure(fg_color="#77A6BB")
                ventanaBatalla.matrizIzquierda.matrizDesplegada[y+(i*factorDirY)][x+(i*factorDirX)-esDerecha].configure(True, width=self.tamañoBotones) # Se actualiza el tamaño del botón, colocando true para que se refresque y aparezca la imagen.
                ventanaBatalla.matrizIzquierda.matrizDesplegada[y+(i*factorDirY)][x+(i*factorDirX)-esDerecha].configure(True, height=self.tamañoBotones) # Se actualiza el tamaño del botón, colocando true para que se refresque y aparezca la imagen.
        for filaCeldas in ventanaBatalla.matrizIzquierda.matrizDesplegada:
            for celdaIndividual in filaCeldas:
                if celdaIndividual.cget("fg_color") != "#77A6BB":
                    celdaIndividual.configure(fg_color="#77A6BB")
        ventanaBatalla.matrizIzquierda.resaltarImpactos(esDerecha, 0)
        numJugador = 1
        esDerecha = self.numColumnas
        for nave in partidaActual.listaNaves[numJugador]:
            for i in range(nave.tipoNave):
                direccionesPosibles = [[0, 1],[-1, 0],[0,-1],[1, 0]] 
                factorDirX, factorDirY = direccionesPosibles[nave.dirNave - 1] 
                y, x = nave.yPosInicial, nave.xPosInicial
                ventanaBatalla.matrizDerecha.matrizDesplegada[y+(i*factorDirY)][x+(i*factorDirX)-esDerecha].configure(text="") # Configura el botón para que sea solo texto
                ventanaBatalla.matrizDerecha.matrizDesplegada[y+(i*factorDirY)][x+(i*factorDirX)-esDerecha].configure(image=CTk.CTkImage(Image.open(naveImágenes[-1]),size=(self.tamañoBotones, self.tamañoBotones))) # Se coloca la imagen vacía en el botón
                ventanaBatalla.matrizDerecha.matrizDesplegada[y+(i*factorDirY)][x+(i*factorDirX)-esDerecha].configure(fg_color="#77A6BB")
                ventanaBatalla.matrizDerecha.matrizDesplegada[y+(i*factorDirY)][x+(i*factorDirX)-esDerecha].configure(True, width=self.tamañoBotones) # Se actualiza el tamaño del botón, colocando true para que se refresque y aparezca la imagen.
                ventanaBatalla.matrizDerecha.matrizDesplegada[y+(i*factorDirY)][x+(i*factorDirX)-esDerecha].configure(True, height=self.tamañoBotones) # Se actualiza el tamaño del botón, colocando true para que se refresque y aparezca la imagen.
        for filaCeldas in ventanaBatalla.matrizDerecha.matrizDesplegada:
            for celdaIndividual in filaCeldas:
                if celdaIndividual.cget("fg_color") != "#77A6BB":
                    celdaIndividual.configure(fg_color="#77A6BB")
        ventanaBatalla.matrizDerecha.resaltarImpactos(esDerecha, 1)
        

class batallaApp(CTk.CTk):
    def __init__(self):
        #######################################################
        ##    Código que crea la ventana principal con CTk   ##
        #######################################################
        super().__init__()
        self.title("BATALLA NAVAL")
        self.configure(fg_color="#CDE8F4")
        self.geometry("1650x950+125+25")
        #######################################################
        ##     Código que indica si se cargó/creó partida    ##
        #######################################################
        if len(partidaActual.listaNaves) >= 1:
            if len(partidaActual.listaNaves[0]) >= 1:
                if isinstance(partidaActual.listaNaves[0][0],Nave):
                    self.modoMatriz = "cargar"
                else: self.modoMatriz = "colocar"
            else: self.modoMatriz = "colocar"
        else: self.modoMatriz = "colocar"
        #######################################################
        ##    Código dedicado a REGISTRO de los JUGADORES    ##
        #######################################################
        if self.modoMatriz != "cargar":
            self.listaTemp = partidaActual.listaJugadores
            partidaActual.listaJugadores = []
            for datoJugador in self.listaTemp:
                partidaActual.listaJugadores.append(Jugador(datoJugador[0],datoJugador[1]))
        #######################################################
        ##     Código dedicado a la MATRIZ de la PARTIDA     ##
        #######################################################
        if self.modoMatriz != "cargar":
            self.listaTemp = partidaActual.matrizJuego
            partidaActual.matrizJuego = [[0] * self.listaTemp[1] for _ in range(self.listaTemp[0])]
            self.modoMatriz = "colocar" # Para reutilizar interfaces
        else:
            print("HEY!", partidaActual.matrizJuego, type(partidaActual.matrizJuego))
            self.listaTemp = [int(partidaActual.matrizJuego[0].strip("[]").split(",")[0]),int(partidaActual.matrizJuego[0].strip("[]").split(",")[1])*2]
            print(self.listaTemp)
            partidaActual.matrizJuego = [[0] * self.listaTemp[1] for _ in range(self.listaTemp[0])]
        self.numJugador = 0 # (Empieza el jugador 1 entonces es [índice 0])
        self.varNaveColocada = CTk.StringVar()
        #######################################################
        ##   Código dedicado a interfaz, realizada con CTk   ##
        #######################################################
        self.grid_columnconfigure((0,1,2,3,4), weight=1)
        self.grid_rowconfigure((0,1,2,3,4), weight=1)
        self.estadoMensaje = f"Turno de '{partidaActual.listaJugadores[0].nickName}'"
        self.colorCubierta = ["#023047", "#FF961F"] # Contiene los colores de ambos jugadores
        self.colorResaltado = ["#045E8B", "#FFA947"] # Contiene los colores de ambos jugadores
        self.fuenteTexto = CTk.CTkFont(family="Basillion",size=35)
        self.frameCubierta = CTk.CTkFrame(self,width=200,height=200,corner_radius=0,fg_color=self.colorCubierta[0 if (self.numJugador+1) != 1 else 1])
        self.frameCubierta.grid(column=0, row=0, padx=0, pady=0, sticky="nsew", columnspan=5, rowspan=5)
        self.labelAdvertencia = CTk.CTkLabel(self,width=200,height=90,text="Advertencia: El programa dura unos segundos cargando!", bg_color=self.colorCubierta[0 if (self.numJugador+1) != 1 else 1], font=self.fuenteTexto, fg_color=self.colorCubierta[0 if (self.numJugador+1) != 1 else 1])
        self.labelAdvertencia.grid(column=2, row=1, padx=0, pady=10)
        if self.modoMatriz == "cargar":
            self.estadoMensaje = "Partida Cargada!"
        self.btnCubierta = CTk.CTkButton(self, fg_color=self.colorCubierta[self.numJugador],
                                         anchor="center",
                                         hover_color=self.colorResaltado[0 if (self.numJugador+1) != 1 else 1],
                                         bg_color=self.colorCubierta[0 if (self.numJugador+1) != 1 else 1],
                                         text=self.estadoMensaje,
                                         width=650,
                                         height=90,
                                         font=self.fuenteTexto,
                                         corner_radius=50,
                                         command=self.manejarTipoTurno)
        self.btnCubierta.grid(column=1, row=2, padx=0, pady=0, columnspan=3)
        self.frameCubierta.tkraise()
        self.labelAdvertencia.tkraise()
        self.btnCubierta.tkraise()
    
    #####################################################################################
    # manejarTipoTurno(self) controla el flujo entre los tipos de turnos que pueden haber
    # Se encarga primero de que las matrices están cubiertas para evitar trampa! 
    # Se controla el flujo de modos de matriz entre colocar, direccionar y atacar.
    # trabaja en conjunto con la función presionarBotón de las matrices
    #####################################################################################

    def manejarTipoTurno(self):
        if self.modoMatriz == "colocar":
            # Colocación del primer jugador
            if self.numJugador == 0: 
                self.labelAdvertencia.destroy()
                self.cargarMatriz() # Se cargan ambas matrices solamente una vez.
                self.btnCubierta.destroy()
                self.frameCubierta.destroy()
                self.colocaciónJugador()
                self.cambioTurno()
                self.modoMatriz = "colocar"
                self.labelMensaje.configure(text="Coloque la cabeza de la nave")
            # Colocación del segundo jugador
            else: 
                self.btnCubierta.destroy()
                self.frameCubierta.destroy()
                self.colocaciónJugador()
                self.modoMatriz = "atacar"
                self.labelMensaje.configure(text="Seleccione su Ataque!")
                self.labelNavesPendientes.configure(text=f"Destructores ({6}) Cruceros ({4}) Acorazados ({2})")
                self.frameSelecciónNave.destroy()
                self.cambioTurno()
        # Ataque de ambos jugadores está manejado en este else if
        elif self.modoMatriz == "atacar":
            if self.numJugador == 0:
                self.btnCubierta.destroy()
                self.frameCubierta.destroy()
                self.turnoJugador()
                self.modoMatriz = "atacar"
                self.cambioTurno()
            else:
                self.btnCubierta.destroy()
                self.frameCubierta.destroy()
                self.turnoJugador()
                self.numJugador = 0
                self.matrizIzquierda.actualizarMatrizParaJugadorActual(self.matrizIzquierda.numColumnas)
                self.matrizDerecha.ocultarTodaMatriz(self.matrizIzquierda.numColumnas)
                self.numJugador = 1
                self.moverNaves()
                self.revisarVictoria(False)
                self.cambioTurno()
        elif self.modoMatriz == "cargar":
            self.labelAdvertencia.destroy()
            self.cargarMatriz() # Se cargan ambas matrices solamente una vez.
            self.btnCubierta.destroy()
            self.frameCubierta.destroy()
            self.modoMatriz = "atacar"
            self.numJugador = 1
            self.cambioTurno()
        elif self.modoMatriz == "guardar":
            self.btnConfirmarGuardado
            self.guardarPartida(self.entradaGuardado.get())
            self.quit()
        elif self.modoMatriz == "terminar":
            self.wait_variable(self.varNaveColocada)
            self.quit()

        """
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
                self.numHundimientos = [0,0,0]
                self.navesPorColocar = [1,1,1]
                self.disparoReciente = "x"

        class Nave:
            def __init__(self, tipoNave, dirNave, posNave):
                self.defaultNaves = [[1,2],[2,1],[3,1]]
                self.tipoNave = tipoNave
                self.dirNave = dirNave
                self.yPosInicial, self.xPosInicial = posNave[0:]
                self.tamañoNave = self.defaultNaves[tipoNave-1][0]
                self.movimientoMax = self.defaultNaves[tipoNave-1][1]
                self.listaPosTotal = [] # Inicializa totalPos con las posiciones iniciales de la nave
                self.listaPosImpacto = []
                self.numImpactos = 0
                self.hundida = False
                self.puedeMoverMínimo = False
        """

    def guardarPartida(self, nombreArchivo):
        archivoGuardado = open(f"{nombreArchivo.lower()}.txt","w",encoding="utf-8") # utf-8 para poder emplear tildes
        archivoGuardado.write("#!\n")
        archivoGuardado.write("-\n")
        jug1 = partidaActual.listaJugadores[0]
        datosJugador1 = [str(jug1.realName)+"\n"
                        ,str(jug1.nickName)+"\n"
                        ,str(jug1.tirosAcertados)+"\n"
                        ,str(jug1.tirosFallidos)+"\n"
                        ,str(jug1.numHundimientos)+"\n"
                        ,str(jug1.navesPorColocar)+"\n"
                        ,str(jug1.disparoReciente)+"\n"]
        archivoGuardado.writelines(datosJugador1)
        archivoGuardado.write("-\n")
        jug2 = partidaActual.listaJugadores[1]
        datosJugador2 = [str(jug2.realName)+"\n"
                        ,str(jug2.nickName)+"\n"
                        ,str(jug2.tirosAcertados)+"\n"
                        ,str(jug2.tirosFallidos)+"\n"
                        ,str(jug2.numHundimientos)+"\n"
                        ,str(jug2.navesPorColocar)+"\n"
                        ,str(jug2.disparoReciente)+"\n"]
        archivoGuardado.writelines(datosJugador2)
        listasNaves = [[],[]]
        for i in range(2):
            for nave in partidaActual.listaNaves[i]:
                listasNaves[i].append("-"+"\n")
                listasNaves[i].append(str(nave.defaultNaves)+"\n")
                listasNaves[i].append(str(nave.tipoNave)+"\n")
                listasNaves[i].append(str(nave.dirNave)+"\n")
                listasNaves[i].append(str(nave.yPosInicial)+"\n")
                listasNaves[i].append(str(nave.xPosInicial)+"\n")
                listasNaves[i].append(str(nave.tamañoNave)+"\n")
                listasNaves[i].append(str(nave.movimientoMax)+"\n")
                listasNaves[i].append(str(nave.listaPosTotal)+"\n")
                listasNaves[i].append(str(nave.listaPosImpacto)+"\n")
                listasNaves[i].append(str(nave.numImpactos)+"\n")
                listasNaves[i].append(str(nave.hundida)+"\n")
                listasNaves[i].append(str(nave.puedeMoverMínimo)+"\n")
        archivoGuardado.write("#!\n")
        archivoGuardado.writelines(listasNaves[0])
        archivoGuardado.write("#!\n")
        archivoGuardado.writelines(listasNaves[1])
        archivoGuardado.write("#!\n")
        archivoGuardado.write("-\n")
        archivoGuardado.write(str([self.matrizDerecha.numColumnas,self.matrizDerecha.numFilas])+"\n")      
        archivoGuardado.write("#!")      
        archivoGuardado.close()
        print(f"guardado: {nombreArchivo}")



    def cargarMatriz(self):
        self.matrizIzquierda = interfazMatriz(self, "#77A6BB", 0)
        self.matrizIzquierda.grid(column=1, row=1, rowspan=3)
        self.matrizDerecha = interfazMatriz(self, "#77A6BB", 1)
        self.matrizDerecha.grid(column=3, row=1, rowspan=3)
        if self.modoMatriz != "cargar":
            self.frameSelecciónNave = interfazTipoNave(self)
            self.frameSelecciónNave.grid(column=2,row=1,rowspan=3,sticky="ew")
        self.labelMensaje = CTk.CTkLabel(self, width=450, height=200, font=self.fuenteTexto, text="Coloque la cabeza de la nave")
        self.labelMensaje.grid(column=1, row=0, columnspan=3, pady=20, sticky="ew")
        self.labelNavesPendientes = CTk.CTkLabel(self, width=450, height=200, font=self.fuenteTexto, text=f"Destructores ({6}) Cruceros ({4}) Acorazados ({2})")
        self.labelNavesPendientes.grid(column=1, row=4, columnspan=3, pady=20, sticky="ew")
        

    #-------------------------------------------------------------------------------------------------------------------------------------#

                      #   ---------------------------------- Ciclar Colocación para un jugador -------------------------------#

    def colocaciónJugador(self):
        # En caso de que la suma de los Naves faltantes del jugador sea 0, el ciclo termina
        while True:
            self.labelMensaje.configure(text="Coloque la cabeza de la nave")
            navesPorColocar = partidaActual.listaJugadores[self.numJugador].navesPorColocar
            self.labelNavesPendientes.configure(text=f"Destructores ({navesPorColocar[0]}) Cruceros ({navesPorColocar[1]}) Acorazados ({navesPorColocar[2]})")
            if navesPorColocar[0] + navesPorColocar[1] + navesPorColocar[2] == 0:
                return
            else:
                self.nuevoNave()


    #-------------------------------------------------------------------------------------------------------------------------------------#

                      #   ----------------------------------  Nuevo Nave  -------------------------------------------#

    def nuevoNave(self): 
        # Espera a recibir todas las naves del jugador
        while True:
            self.wait_variable(self.varNaveColocada)
            datosNave = self.varNaveColocada.get()
            datosNave = datosNave.split(",")
            for num in range(len(datosNave)):
                datosNave[num] = int(datosNave[num])

            # Para el jugador 2 se debe considerar la segunda mitad de la matriz
            # Se le suman columnas según el tamaño de la matriz izquierda dado que son gemelas las matrices
            if self.numJugador == 1:
                datosNave[3] += self.matrizIzquierda.numColumnas

            #print("datosNave", datosNave)
            tipoNave, dirNave, nFila, nColumna  = datosNave[:]

            # Inserta el número de la nave en la posición dada
            partidaActual.listaNaves[self.numJugador].append(Nave(tipoNave, dirNave, [nFila,nColumna])) # Añade un objeto de nave a la lista de naves del jugador
            
            # La siguiente condicional utiliza una función que revisa si es válido el posicionamiento de la nave.
            # En caso de serlo la misma función coloca la nave en la matriz y retorna un valor booleano.
            if self.colocarNave(): # Retorna verdadero en caso de colocar con éxito al jugador.
                if self.numJugador == 0: self.matrizIzquierda.actualizarMatrizParaJugadorActual(0)
                else: self.matrizDerecha.actualizarMatrizParaJugadorActual(self.matrizIzquierda.numColumnas)
                break # En caso de ser válida se rompe el ciclo para volver a colocaciónJugador()
            else:
                del partidaActual.listaNaves[self.numJugador][-1] # Borra la nave más reciente en caso de que la revisión sea inválida (retornado falso)
    
    
    
    #-------------------------------------------------------------------------------------------------------------------------------------#

                      #   ----------------------------------  Verificar Colocada  -------------------------------------------#

    def colocarNave(self):
        naveActual = partidaActual.listaNaves[self.numJugador][-1] # Se obtiene la nave más reciente del jugador actual
        #Se revisa si el jugador aún puede colocar este tipo de nave:
        if partidaActual.listaJugadores[self.numJugador].navesPorColocar[naveActual.tipoNave - 1] <= 0:
            self.labelMensaje.configure(text="Ya no le quedan naves de este tipo...")
            return False
        # Se utilizan índices en una lista temporal para obtener factores de dirección que definirán hacia a dónde debe simularse la posición de la nave en el tablero
        direccionesPosibles = [[0, 1],[-1, 0],[0,-1],[1, 0]] #Izquierda
        #print("dirNave",naveActual.dirNave)
        #print(self.numJugador)
        factorDirX, factorDirY = direccionesPosibles[naveActual.dirNave - 1]
        for i in range(naveActual.tamañoNave):  # Se revisa según el tamaño de la nave, todas las casillas que va a ocupar en el juego
            # A la posición de la nave se le suma i + un factor de dirección que cambia según la dirección de la Nave para evitar repetición de código
            # Se utiliza un try/except para evitar que el programa se caiga en caso de una posición equivocada
            # La posición yPosInicial va primero porque se define según la fila de la matriz (primer índice)
            try:
                if not 0 <= naveActual.yPosInicial+(i*factorDirY): 
                    self.labelMensaje.configure(text="La nave no cabe en el tablero...")
                    return False  
                if not 0 <= naveActual.xPosInicial+(i*factorDirX):
                    self.labelMensaje.configure(text="La nave no cabe en el tablero...")
                    return False  
                if partidaActual.matrizJuego[naveActual.yPosInicial+(i*factorDirY)][naveActual.xPosInicial+(i*factorDirX)] != 0:
                    self.labelMensaje.configure(text="Su nave choca con otra nave... ")
                    return False
                if self.numJugador == 1:
                    if self.matrizIzquierda.numColumnas > naveActual.xPosInicial+(i*factorDirX):
                        self.labelMensaje.configure(text="La nave no cabe en el tablero...")
                        return False
                else:
                    if self.matrizIzquierda.numColumnas <= naveActual.xPosInicial+(i*factorDirX):
                        self.labelMensaje.configure(text="La nave no cabe en el tablero...")
                        return False
            except IndexError:
                self.labelMensaje.configure(text="La nave no cabe en el tablero...")
                return False
        # Este código coloca la nave en la matriz, si nunca chocó contra nada.
        for i in range(naveActual.tamañoNave):
            # Marca las posiciones de cada espacio tomado por la nave con un 1 o un 2 según el jugador
            partidaActual.matrizJuego[naveActual.yPosInicial+(i*factorDirY)][naveActual.xPosInicial+(i*factorDirX)] = self.numJugador + 1
            #Los junta una vez para cada tamaño de la nave
            naveActual.listaPosTotal.append([naveActual.yPosInicial+(i*factorDirY),naveActual.xPosInicial+(i*factorDirX)]) 
        # Se le debe restar al jugador actual una de las naves disponibles del tipo que se acaba de colocar, para tener un máximo de naves
        partidaActual.listaJugadores[self.numJugador].navesPorColocar[naveActual.tipoNave - 1] -= 1
        #print(naveActual.listaPosTotal)
        return True

    def actualizarMatrizJuego(self):
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
                    marcaJugador = jugador_num if jugador_num != 2 else 2
                    partidaActual.matrizJuego[parOrdenado[0]][parOrdenado[1]] = marcaJugador


    #-------------------------------------------------------------------------------------------------------------------------------------#

                      #   ---------------------------------- Ciclar Movimiento de las Naves -------------------------------#

    def moverNaves(self):
        self.numJugador = 0
        for naveAMover in partidaActual.listaNaves[0]: #Itera sobre cada nave en la lista de naves del jugador 1.
            self.actualizarMatrizJuego()
            dirección = naveAMover.dirNave  # Utilizar la dirección de la nave
            if naveAMover.numImpactos == 0:  # Comprobar si la dirección es válida y si la nave puede moverse      
                 # Se asigna la variable un valor booleano con el fin de que cuando este cambie de estado el bucle finalice
                while True: #El bucle continuará ejecutandose siempre que "naveMoved" sea falsa               
                    if dirección == 3:  # Arriba #Se compara la dirección con la selección de dirNave               
                        if naveAMover.moverArriba(): #se llaman los metodos anteriormente definidos               
                            print("Nave movida arriba!")
                            ##naveAMover.navesDebug()#se imprime un mensaje indicando la dirección en la que se movió la nave                            
                            
                            break #Si el movimiento es exitoso, lo iguala a True para no inicializar con las otras comparaciones y finalizar el ciclo 
                        else:
                            if naveAMover.puedeMoverMínimo: # El destructor puede tal vez moverse 1 espacio, pero no 2. Esto se encarga de ese caso
                                naveAMover.movimientoMax = 1
                                if naveAMover.moverArriba():
                                    print("Nave movida arriba. PMM MODE!", naveAMover.tipoNave)#se imprime un mensaje indicando la dirección en la que se movió la nave                            
                                naveAMover.movimientoMax = 2
                                break # Se re-establece el movimiento máximo del destructor
                            else:
                                break
                    ## La logica se repite para abarcar los posibles casos ##    
                    elif dirección == 1:  # Abajo         
                        if naveAMover.moverAbajo():                    
                            print("Nave movida abajo!")
                            ##naveAMover.navesDebug()                                  
                            break      
                        else:
                            if naveAMover.puedeMoverMínimo: # El destructor puede tal vez moverse 1 espacio, pero no 2. Esto se encarga de ese caso
                                naveAMover.movimientoMax = 1
                                if naveAMover.moverAbajo():
                                    print("Nave movida abajo. PMM MODE!", naveAMover.tipoNave)#se imprime un mensaje indicando la dirección en la que se movió la nave                            
                                naveAMover.movimientoMax = 2
                                break
                            else:
                                break   
                    elif dirección == 2:  # Izquierda
                        if naveAMover.moverIzquierda():
                            print("Nave movida izquierda!")
                            ##naveAMover.navesDebug()
                            break
                        else:
                            if naveAMover.puedeMoverMínimo: # El destructor puede tal vez moverse 1 espacio, pero no 2. Esto se encarga de ese caso
                                naveAMover.movimientoMax = 1
                                if naveAMover.moverIzquierda():
                                    print("Nave movida izquierda. PMM MODE!", naveAMover.tipoNave)#se imprime un mensaje indicando la dirección en la que se movió la nave                            
                                naveAMover.movimientoMax = 2
                                break
                            else:
                                break
                    elif dirección == 4:  # Derecha
                        if naveAMover.moverDerecha():
                            print("Nave movida derecha!")
                            ##naveAMover.navesDebug()
                            break
                        else:
                            if naveAMover.puedeMoverMínimo: # El destructor puede tal vez moverse 1 espacio, pero no 2. Esto se encarga de ese caso
                                naveAMover.movimientoMax = 1
                                if naveAMover.moverDerecha():
                                    print("Nave movida derecha. PMM MODE!", naveAMover.tipoNave)#se imprime un mensaje indicando la dirección en la que se movió la nave                            
                                naveAMover.movimientoMax = 2
                                break
                            else:
                                break
            else:
                print("Nave Impactada, saltando")
        # Lo mismo para el jugador 2
        self.numJugador = 1
        for naveAMover in partidaActual.listaNaves[1]: #Itera sobre cada nave en la lista de naves del jugador 1.
            self.actualizarMatrizJuego()
            dirección = naveAMover.dirNave  # Utilizar la dirección de la nave
            if naveAMover.numImpactos == 0:  # Comprobar si la dirección es válida y si la nave puede moverse      
                while True: #El bucle continuará ejecutandose siempre que "naveMoved" sea falsa               
                    if dirección == 3:  # Arriba #Se compara la dirección con la selección de dirNave               
                        if naveAMover.moverArriba(): #se llaman los metodos anteriormente definidos               
                            print("Nave movida arriba!")
                            ##naveAMover.navesDebug()#se imprime un mensaje indicando la dirección en la que se movió la nave                            
                            break #Si el movimiento es exitoso, lo iguala a True para no inicializar con las otras comparaciones y finalizar el ciclo 
                        else:
                            if naveAMover.puedeMoverMínimo: # El destructor puede tal vez moverse 1 espacio, pero no 2. Esto se encarga de ese caso
                                naveAMover.movimientoMax = 1
                                if naveAMover.moverArriba():
                                    print("Nave movida arriba. PMM MODE!", naveAMover.tipoNave)#se imprime un mensaje indicando la dirección en la que se movió la nave                            
                                naveAMover.movimientoMax = 2
                                break # Se re-establece el movimiento máximo del destructor
                            else:
                                break
                    ## La logica se repite para abarcar los posibles casos ##    
                    elif dirección == 1:  # Abajo         
                        if naveAMover.moverAbajo():                    
                            print("Nave movida abajo!")
                            ##naveAMover.navesDebug()                                  
                            break      
                        else:
                            if naveAMover.puedeMoverMínimo: # El destructor puede tal vez moverse 1 espacio, pero no 2. Esto se encarga de ese caso
                                naveAMover.movimientoMax = 1
                                if naveAMover.moverAbajo():
                                    print("Nave movida abajo. PMM MODE!", naveAMover.tipoNave)#se imprime un mensaje indicando la dirección en la que se movió la nave                            
                                naveAMover.movimientoMax = 2
                                break
                            else:
                                break   
                    elif dirección == 2:  # Izquierda
                        if naveAMover.moverIzquierda():
                            print("Nave movida izquierda!")
                            ##naveAMover.navesDebug()
                            break
                        else:
                            if naveAMover.puedeMoverMínimo: # El destructor puede tal vez moverse 1 espacio, pero no 2. Esto se encarga de ese caso
                                naveAMover.movimientoMax = 1
                                if naveAMover.moverIzquierda():
                                    print("Nave movida izquierda. PMM MODE!", naveAMover.tipoNave)#se imprime un mensaje indicando la dirección en la que se movió la nave                            
                                naveAMover.movimientoMax = 2
                                break
                            else:
                                break
                    elif dirección == 4:  # Derecha
                        if naveAMover.moverDerecha():
                            print("Nave movida derecha!")
                            ##naveAMover.navesDebug()
                            break
                        else:
                            if naveAMover.puedeMoverMínimo: # El destructor puede tal vez moverse 1 espacio, pero no 2. Esto se encarga de ese caso
                                naveAMover.movimientoMax = 1
                                if naveAMover.moverDerecha():
                                    print("Nave movida derecha. PMM MODE!", naveAMover.tipoNave)#se imprime un mensaje indicando la dirección en la que se movió la nave                            
                                naveAMover.movimientoMax = 2
                                break
                            else:
                                break
            else:
                print("Nave Impactada, saltando")
    #-------------------------------------------------------------------------------------------------------------------------------------#


                      #   ----------------------------------  Revisar Ataque Realizado  -------------------------------------------#
    
    def ataqueFlota(self, fila, columna):
        try:
            ataqueExitoso = False
            naveImpactada = None
            numOponente = 0 if (self.numJugador+1) != 1 else 1 # Obtener cuál índice posee el oponente
            listaNavesOponente = partidaActual.listaNaves[numOponente] #Obtiene la lista de naves del oponente, haciendo que el indice cambie del jugador opuesto 
            parOrdenadoAtacado = [int(fila), int(columna)+(ventanaBatalla.matrizIzquierda.numColumnas if numOponente == 1 else 0)]
            # Se le acaban de restar 10 columnas a la coordenada en caso de que el oponente sea de la cuadrícula derecha
            # Iterar sobre las naves del jugador
            for numNave in range(len(listaNavesOponente)):
                naveActual = listaNavesOponente[numNave]
                if parOrdenadoAtacado in naveActual.listaPosTotal:
                    if parOrdenadoAtacado in naveActual.listaPosImpacto:
                        self.labelMensaje.configure(text="Ya atacaste esa casilla, intenta de nuevo.")
                        return False
                    naveImpactada = numNave
                    ataqueExitoso = True # Si en alguna de las coordenadas de la nave coinciden, el ataque fue exitoso!
            if ataqueExitoso:
                self.labelMensaje.configure(text="¡Acertaste un disparo! La nave ha sido impactada.")
                listaNavesOponente[naveImpactada].listaPosImpacto.append([int(fila), int(columna)]) #Agrega las casillas impactadas a la nave impactada y posteriormente detectan los hundimientos
                listaNavesOponente[naveImpactada].numImpactos += 1 #Aumenta la cantidad de impactos que posee la nave
                partidaActual.listaJugadores[self.numJugador].tirosAcertados += 1 # Incrementar el contador de tiros acertados del jugador
                #--------------------------- Control de hundimientos --------------------------------------#
                if listaNavesOponente[naveImpactada].numImpactos == listaNavesOponente[naveImpactada].tipoNave:  # Si la nave ha sido impactada, detectan los hundimientos
                    listaNavesOponente[naveImpactada].hundida = True
                    self.labelMensaje.configure(text="Hundiste una nave!")
                    hundidosJugador = partidaActual.listaJugadores[self.numJugador].numHundimientos
                    partidaActual.listaJugadores[self.numJugador].numHundimientos[listaNavesOponente[naveImpactada].tipoNave-1] += 1 
                    try:
                        self.labelNavesPendientes.configure(text=f"Naves del Oponente: {6-hundidosJugador[0]} Destructores, {4-hundidosJugador[1]} Cruceros, {2-hundidosJugador[2]} Acorazados")
                    except:
                        return
            else:
                self.labelMensaje.configure(text="Tiro fallido, no impactaste en ninguna nave.")
                partidaActual.listaJugadores[self.numJugador].tirosFallidos += 1
            return True
        except IndexError:
            print("Error de tiro... Reintentando...")
            return False


    #-------------------------------------------------------------------------------------------------------------------------------------#


                      #   ----------------------------------  Realizar 1 Turno de Ataque  -------------------------------------------#

    def turnoJugador(self):
        while True:    
            self.wait_variable(self.varNaveColocada)
            celdaAtacada = self.varNaveColocada.get()
            celdaAtacada = celdaAtacada.split(",")
            partidaActual.listaJugadores[self.numJugador].disparoReciente = [int(celdaAtacada[0]), int(celdaAtacada[1])]
            if self.ataqueFlota(celdaAtacada[0], celdaAtacada[1]):
                self.actualizarMatrizJuego()
                if self.numJugador == 1:
                    #self.matrizIzquierda.ocultarTodaMatriz(0)
                    self.matrizDerecha.actualizarMatrizParaJugadorActual(self.matrizIzquierda.numColumnas)
                else:
                    #self.matrizDerecha.ocultarTodaMatriz(self.matrizIzquierda.numColumnas)
                    self.matrizIzquierda.actualizarMatrizParaJugadorActual(0)
                if self.numJugador == 0:
                    self.aparecerBotónSiguiente()
                else:
                    self.aparecerMiniMenu()
                self.modoMatriz = "NINGUNA"
                self.wait_variable(self.varNaveColocada)
                if self.numJugador == 0:
                    self.btnSiguiente.destroy()
                else:
                    self.btnSiguiente.destroy()
                    self.btnGuardar.destroy()
                    self.btnFinalizar.destroy()
                self.modoMatriz = self.varNaveColocada.get()
                break
                
            
    #-------------------------------------------------------------------------------------------------------------------------------------#

                      #   ----------------------------------  Botón Siguiente  -------------------------------------------#
    
    def aparecerBotónSiguiente(self):
        self.btnSiguiente = CTk.CTkButton(self, fg_color=self.colorCubierta[0 if (self.numJugador+1) != 1 else 1],
                                         anchor="center",
                                         hover_color=self.colorResaltado[0 if (self.numJugador+1) != 1 else 1],
                                         bg_color="#CDE8F4",
                                         text="NEXT",
                                         width=120,
                                         height=90,
                                         font=self.fuenteTexto,
                                         corner_radius=50,
                                         command=lambda: self.varNaveColocada.set("atacar"))
        self.btnSiguiente.grid(column=2,row=2,sticky="ew")
    
    def aparecerMiniMenu(self):
        self.btnSiguiente = CTk.CTkButton(self, fg_color=self.colorCubierta[1 if (self.numJugador+1) != 1 else 0],
                                         anchor="center",
                                         hover_color=self.colorResaltado[1 if (self.numJugador+1) != 1 else 0],
                                         bg_color="#CDE8F4",
                                         text="SEGUIR",
                                         width=120,
                                         height=90,
                                         font=self.fuenteTexto,
                                         corner_radius=50,
                                         command=lambda: self.varNaveColocada.set("atacar"))
        self.btnSiguiente.grid(column=2,row=2,sticky="ew")
        self.btnGuardar = CTk.CTkButton(self, fg_color=self.colorCubierta[0 if (self.numJugador+1) != 1 else 1],
                                         anchor="center",
                                         hover_color=self.colorResaltado[0 if (self.numJugador+1) != 1 else 1],
                                         bg_color="#CDE8F4",
                                         text="GUARDAR",
                                         width=120,
                                         height=90,
                                         font=self.fuenteTexto,
                                         corner_radius=50,
                                         command=lambda: self.varNaveColocada.set("guardar"))
        self.btnGuardar.grid(column=2,row=1,sticky="ew")
        self.btnFinalizar = CTk.CTkButton(self, fg_color=self.colorCubierta[0 if (self.numJugador+1) != 1 else 1],
                                         anchor="center",
                                         hover_color=self.colorResaltado[0 if (self.numJugador+1) != 1 else 1],
                                         bg_color="#CDE8F4",
                                         text="TERMINAR",
                                         width=120,
                                         height=90,
                                         font=self.fuenteTexto,
                                         corner_radius=50,
                                         command=lambda: self.varNaveColocada.set("terminar"))
        self.btnFinalizar.grid(column=2,row=3,sticky="ew")


    #-------------------------------------------------------------------------------------------------------------------------------------#

                      #   ----------------------------------  Cambiar de un Jugador a Otro  -------------------------------------------#

    def cambioTurno(self):
        self.actualizarMatrizJuego()
        self.numJugador = 0 if (self.numJugador+1) != 1 else 1
        self.estadoMensaje = f"Turno de '{partidaActual.listaJugadores[self.numJugador].nickName}'"
        self.frameCubierta = CTk.CTkFrame(self,width=200,height=200,corner_radius=0,fg_color=self.colorCubierta[0 if (self.numJugador+1) != 1 else 1])
        self.frameCubierta.grid(column=0, row=0, padx=0, pady=0, sticky="nsew", columnspan=5, rowspan=5)
        self.frameCubierta.tkraise()
        if self.modoMatriz == "terminar":
            self.labelVictoria = CTk.CTkLabel(self, fg_color=self.colorCubierta[self.numJugador], bg_color=self.colorCubierta[0 if (self.numJugador+1) != 1 else 1], width=450, height=200, font=self.fuenteTexto, text="FIN", text_color="#F8F8F8", corner_radius=32)
            self.labelVictoria.grid(column=1, row=1, columnspan=3, pady=20, sticky="ew")
            self.labelVictoria.tkraise()
            self.revisarVictoria(True)
            self.btnSalir = CTk.CTkButton(self, fg_color=self.colorCubierta[self.numJugador],
                                            anchor="center",
                                            hover_color=self.colorResaltado[0 if (self.numJugador+1) != 1 else 1],
                                            bg_color=self.colorCubierta[0 if (self.numJugador+1) != 1 else 1],
                                            text="Salir",
                                            width=650,
                                            height=90,
                                            font=self.fuenteTexto,
                                            corner_radius=50,
                                            command=self.quit)
            self.btnSalir.grid(column=1, row=2, padx=0, pady=20, columnspan=3)
            self.btnSalir.tkraise()
        elif self.modoMatriz == "guardar":
            self.entradaGuardado = CTk.CTkEntry(self, font=self.fuenteTexto, placeholder_text="Nombre del Archivo", width=450, height=80)
            self.entradaGuardado.grid(column=1, row=1, columnspan=3, padx=50, pady=20, sticky="ew")
            self.btnConfirmarGuardado = CTk.CTkButton(self, fg_color=self.colorCubierta[self.numJugador],
                                            anchor="center",
                                            hover_color=self.colorResaltado[0 if (self.numJugador+1) != 1 else 1],
                                            bg_color=self.colorCubierta[0 if (self.numJugador+1) != 1 else 1],
                                            text="Guardar Partida",
                                            width=650,
                                            height=90,
                                            font=self.fuenteTexto,
                                            corner_radius=50,
                                            command=self.manejarTipoTurno)
            self.btnConfirmarGuardado.grid(column=1, row=2, padx=0, pady=20, columnspan=3)
            self.btnConfirmarGuardado.tkraise()
        else:
            self.btnCubierta = CTk.CTkButton(self, fg_color=self.colorCubierta[self.numJugador],
                                            anchor="center",
                                            hover_color=self.colorResaltado[0 if (self.numJugador+1) != 1 else 1],
                                            bg_color=self.colorCubierta[0 if (self.numJugador+1) != 1 else 1],
                                            text=self.estadoMensaje,
                                            width=650,
                                            height=90,
                                            font=self.fuenteTexto,
                                            corner_radius=50,
                                            command=self.manejarTipoTurno)
            self.btnCubierta.grid(column=1, row=2, padx=0, pady=0, columnspan=3)
            self.btnCubierta.tkraise()
        self.matrizIzquierda.ocultarTodaMatriz(0)
        if self.numJugador == 0: 
            self.matrizIzquierda.actualizarMatrizParaJugadorActual(0)
        else: 
            self.matrizDerecha.actualizarMatrizParaJugadorActual(self.matrizIzquierda.numColumnas)
        if self.modoMatriz == "atacar":
            self.actualizarMatrizJuego()
            hundidosJugador = partidaActual.listaJugadores[self.numJugador].numHundimientos
            self.labelMensaje.configure(text="Seleccione su Ataque!")
            try:
                self.labelNavesPendientes.configure(text=f"Naves del Oponente: {6-hundidosJugador[0]} Destructores, {4-hundidosJugador[1]} Cruceros, {2-hundidosJugador[2]} Acorazados")
            except:
                return

    def revisarVictoria(self, forzarTerminar):
        hundidosJugador1 = partidaActual.listaJugadores[0].numHundimientos
        hundidosJugador2 = partidaActual.listaJugadores[1].numHundimientos
        aciertosJugador1 = partidaActual.listaJugadores[0].tirosAcertados
        aciertosJugador2 = partidaActual.listaJugadores[1].tirosAcertados
        hundidosJugador1 = hundidosJugador1[0] + hundidosJugador1[1] + hundidosJugador1[2]
        hundidosJugador2 = hundidosJugador2[0] + hundidosJugador2[1] + hundidosJugador2[2]
        if  hundidosJugador2 >= 12 and hundidosJugador1 >= 12:
            self.labelVictoria.configure(text="Buenas noticias! La partida es un empate")
            self.configure(fg_color="#FFB999")
            self.modoMatriz = "NINGUNA"
        elif hundidosJugador2 >= 12:
            self.labelVictoria.configure(text=f"¡Felicidades {partidaActual.listaJugadores[0].nickName}, has ganado la partida!")
            self.configure(fg_color=self.colorCubierta[1])
            self.modoMatriz = "NINGUNA"
        elif hundidosJugador1 >= 12:
            self.labelVictoria.configure(text=f"¡Felicidades {partidaActual.listaJugadores[1].nickName}, has ganado la partida!")
            self.configure(fg_color=self.colorCubierta[0])
            self.modoMatriz = "NINGUNA"
        elif forzarTerminar:
            if hundidosJugador2 == hundidosJugador1:
                if aciertosJugador1 == aciertosJugador2:
                    self.labelVictoria.configure(text="Buenas noticias! La partida es un empate")
                    self.configure(fg_color="#FFB999")
                elif aciertosJugador1 > aciertosJugador2:
                    self.labelVictoria.configure(text=f"¡Felicidades {partidaActual.listaJugadores[0].nickName}, has ganado la partida!")
                    self.configure(fg_color=self.colorCubierta[0])
                    self.modoMatriz = "NINGUNA"
                elif aciertosJugador1 < aciertosJugador2:
                    self.labelVictoria.configure(text=f"¡Felicidades {partidaActual.listaJugadores[1].nickName}, has ganado la partida!")
                    self.configure(fg_color=self.colorCubierta[1])
                    self.modoMatriz = "NINGUNA"
            elif hundidosJugador2 > hundidosJugador1:
                self.labelVictoria.configure(text=f"¡Felicidades {partidaActual.listaJugadores[1].nickName}, has ganado la partida!")
                self.configure(fg_color=self.colorCubierta[1])
                self.modoMatriz = "NINGUNA"
            elif hundidosJugador2 < hundidosJugador1:
                self.labelVictoria.configure(text=f"¡Felicidades {partidaActual.listaJugadores[0].nickName}, has ganado la partida!")
                self.configure(fg_color=self.colorCubierta[0])
                self.modoMatriz = "NINGUNA"

################################################  Comienzo del código que ejecuta todas las funciones y clases anteriores #################################################################
################################################  Comienzo del código que ejecuta todas las funciones y clases anteriores #################################################################
################################################  Comienzo del código que ejecuta todas las funciones y clases anteriores #################################################################

####################################################
# Igual que tkinter, se corre la app con mainloop()
####################################################
ventanaSelección = selecciónApp()
ventanaSelección.mainloop()
#############################################################################
# Se elimina la ventana original, pero se mantienen las variables globales
del ventanaSelección
#############################################################################
# Cuando la ventana de selección deja de existir, la ventana de batalla entra en juego.
ventanaBatalla = batallaApp()
ventanaBatalla.mainloop()
