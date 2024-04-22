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
        self.puedeMoverMínimo = False
        self.seMueveEsteTurno = True

    
    #cambiar de acuerdo a la función
    def moverArriba(self):
        self.puedeMoverMínimo = False
        # Verifica si la nave puede moverse hacia arriba sin salir del borde superior del tablero
        for parOrdenado in self.listaPosTotal:
            for distanciaMax in range(self.movimientoMax):
                if not parOrdenado[0]-(distanciaMax) in range(len(partidaActual.matrizJuego)): #0=y 1=x 
                    print("Error: La nave no puede moverse más hacia arriba.")
                    if not self.puedeMoverMínimo:
                        self.dirNave = 1
                        self.yPosInicial -= self.tipoNave-1
                    return
                self.puedeMoverMínimo = True
                
        for parOrdenado in self.listaPosTotal:
            parOrdenado[0] -= self.movimientoMax
            self.yPosInicial -= self.movimientoMax
        return True  # Devuelve True para indicar que el movimiento fue exitoso
    

    def moverAbajo(self):
        self.puedeMoverMínimo = False
        # Verifica si la nave puede moverse hacia arriba sin salir del borde superior del tablero
        for parOrdenado in self.listaPosTotal:
            for distanciaMax in range(self.movimientoMax):
                if not parOrdenado[0]+(distanciaMax) in range(len(partidaActual.matrizJuego)): #0=y 1=x 
                    print("Error: La nave no puede moverse más hacia arriba.")
                    if not self.puedeMoverMínimo:
                        self.dirNave = 3
                        self.yPosInicial += self.tipoNave-1
                    return
                self.puedeMoverMínimo = True
                
        for parOrdenado in self.listaPosTotal:
            parOrdenado[0] += self.movimientoMax
            self.yPosInicial += self.movimientoMax
        return True  # Devuelve True para indicar que el movimiento fue exitoso


    def moverIzquierda(self):
        self.puedeMoverMínimo = False
        # Verifica si la nave puede moverse hacia arriba sin salir del borde superior del tablero
        for parOrdenado in self.listaPosTotal:
            for distanciaMax in range(self.movimientoMax):
                if not parOrdenado[1]-(distanciaMax) in range(len(partidaActual.matrizJuego[0])):
                    print("Error: La nave no puede moverse más hacia arriba.")
                    if not self.puedeMoverMínimo:
                        self.dirNave = 4
                        self.xPosInicial -= self.tipoNave-1
                    return
                self.puedeMoverMínimo = True
                
        for parOrdenado in self.listaPosTotal:
            parOrdenado[1] -= self.movimientoMax
            self.xPosInicial -= self.movimientoMax
        return True  # Devuelve True para indicar que el movimiento fue exitoso
    
    def moverDerecha(self):
        self.puedeMoverMínimo = False
        # Verifica si la nave puede moverse hacia arriba sin salir del borde superior del tablero
        for parOrdenado in self.listaPosTotal:
            for distanciaMax in range(self.movimientoMax):
                if not parOrdenado[1]+(distanciaMax) in range(len(partidaActual.matrizJuego[0])):
                    print("Error: La nave no puede moverse más hacia arriba.")
                    if not self.puedeMoverMínimo:
                        self.dirNave = 2
                        self.xPosInicial += self.tipoNave-1
                    return
                self.puedeMoverMínimo = True
                
        for parOrdenado in self.listaPosTotal:
            parOrdenado[1] += self.movimientoMax
            self.xPosInicial += self.movimientoMax
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
        self.btnCargarPartida = CTk.CTkButton(self,fg_color="#023047",hover_color="#FF961F", text="Cargar Partida", width=350, height=150, font=self.fuenteTexto, corner_radius=8, command=print)
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
        self.numJugador = numJugador
        self.modoMatriz = "colocar"
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

    # Al presionar el botón se ejecuta esto
    # Esta función es un despelote de prueba que lo que hace es quitar el texto y colocar imágenes

    def resaltarDireccionarToggle(self):
        self.colorReciente = "#77A6BB" if self.colorReciente != "#77A6BB" else "#67AE5B"
        print("color",self.colorReciente)
        print("celda",self.celdaActual)
        if 0 <= self.celdaActual[0]+1 and self.celdaActual[0]+1 < len(self.matrizDesplegada):
            self.matrizDesplegada[self.celdaActual[0]+1][self.celdaActual[1]].configure(fg_color=self.colorReciente)
        if 0 <= self.celdaActual[0]-1 and self.celdaActual[0]-1 < len(self.matrizDesplegada):
            self.matrizDesplegada[self.celdaActual[0]-1][self.celdaActual[1]].configure(fg_color=self.colorReciente)
        if 0 <= self.celdaActual[1]+1 and self.celdaActual[1]+1 < len(self.matrizDesplegada[0]):
            self.matrizDesplegada[self.celdaActual[0]][self.celdaActual[1]+1].configure(fg_color=self.colorReciente)
        if 0 <= self.celdaActual[1]-1 and self.celdaActual[1]-1 < len(self.matrizDesplegada[0]):
            self.matrizDesplegada[self.celdaActual[0]][self.celdaActual[1]-1].configure(fg_color=self.colorReciente)
        
    def resaltarImpactos(self, esDerecha):
        for nave in partidaActual.listaNaves[[0 if (ventanaBatalla.numJugador+1) != 1 else 1]]:
            for parOrdenado in nave.listaPosImpacto:
                y, x = parOrdenado[:]
                self.matrizDesplegada[y][x].configure(fg_color="#FA4F00") # Configura el botón para que sea solo texto
                self.matrizDesplegada[y][x].configure(True, width=self.tamañoBotones) # Se actualiza el tamaño del botón, colocando true para que se refresque y aparezca la imagen.
                self.matrizDesplegada[y][x].configure(True, height=self.tamañoBotones) # Se actualiza el tamaño del botón, colocando true para que se refresque y aparezca la imagen.

    def presionarBotón(self,i,j):
        if ventanaBatalla.numJugador == self.numJugador:
            if ventanaBatalla.frameSelecciónNave.getTipoNave() != False:
                if self.modoMatriz == "colocar":
                    self.modoMatriz = "direccionar"
                    ventanaBatalla.labelMensaje.configure(text="Indique el sentido de la cola de la nave")
                    self.celdaReciente = [i,j]
                    self.celdaActual = [i,j]
                    self.colorReciente = "#77A6BB"
                    self.resaltarDireccionarToggle()
                    self.wait_variable(self.varDirElegida)
                    if self.varDirElegida.get() == "0":
                        self.resaltarDireccionarToggle()
                        print("going back!")
                        self.modoMatriz = "colocar"
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
                        ventanaBatalla.varBarcoColocado.set(variableTransmitida)
                        self.modoMatriz = "colocar"
                elif self.modoMatriz == "direccionar":
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
                elif self.modoMatriz == "atacar":
                    pass
            else:
                ventanaBatalla.labelMensaje.configure(text="Seleccione un tipo de Nave!")
        else:
            ventanaBatalla.labelMensaje.configure(text="Matriz equivocada!")

    def actualizarMatrizParaJugadorActual(self, esDerecha):
        for nave in partidaActual.listaNaves[ventanaBatalla.numJugador]:
            for i in range(nave.tipoNave):
                # Hace un nuevo objeto de imagen CTkImage y abre la imagen con PIL.Image.open()...(solo "Image" aquí por como se importó)
                gradosRotación = [-90,180,90,0]
                buttonImage = CTk.CTkImage(Image.open(naveImágenes[nave.tipoNave-1][i]).rotate(gradosRotación[nave.dirNave-1]), size=(self.tamañoBotones,self.tamañoBotones))
                direccionesPosibles = [[0, 1],[-1, 0],[0,-1],[1, 0]] #Izquierda
                factorDirX, factorDirY = direccionesPosibles[nave.dirNave - 1] 
                y, x = nave.yPosInicial, nave.xPosInicial
                self.matrizDesplegada[y+(i*factorDirY)][x+(i*factorDirX)-esDerecha].configure(text="") # Configura el botón para que sea solo texto
                self.matrizDesplegada[y+(i*factorDirY)][x+(i*factorDirX)-esDerecha].configure(image=buttonImage) # Se coloca la imagen en el botón
                self.matrizDesplegada[y+(i*factorDirY)][x+(i*factorDirX)-esDerecha].configure(fg_color="#77A6BB")
                self.matrizDesplegada[y+(i*factorDirY)][x+(i*factorDirX)-esDerecha].configure(True, width=self.tamañoBotones) # Se actualiza el tamaño del botón, colocando true para que se refresque y aparezca la imagen.
                self.matrizDesplegada[y+(i*factorDirY)][x+(i*factorDirX)-esDerecha].configure(True, height=self.tamañoBotones) # Se actualiza el tamaño del botón, colocando true para que se refresque y aparezca la imagen.

    # Imita la función anterior pero oculta las imágenes del oponente
    def ocultarMatrizOponente(self, esDerecha):
            for nave in partidaActual.listaNaves[0 if (ventanaBatalla.numJugador+1) != 1 else 1]:
                for i in range(nave.tipoNave):
                    direccionesPosibles = [[0, 1],[-1, 0],[0,-1],[1, 0]] #Izquierda
                    factorDirX, factorDirY = direccionesPosibles[nave.dirNave - 1] 
                    y, x = nave.yPosInicial, nave.xPosInicial
                    self.matrizDesplegada[y+(i*factorDirY)][x+(i*factorDirX)-esDerecha].configure(text="") # Configura el botón para que sea solo texto
                    self.matrizDesplegada[y+(i*factorDirY)][x+(i*factorDirX)-esDerecha].configure(image=CTk.CTkImage(Image.open(naveImágenes[-1]))) # Se coloca la imagen vacía en el botón
                    self.matrizDesplegada[y+(i*factorDirY)][x+(i*factorDirX)-esDerecha].configure(fg_color="#77A6BB")
                    self.matrizDesplegada[y+(i*factorDirY)][x+(i*factorDirX)-esDerecha].configure(True, width=self.tamañoBotones) # Se actualiza el tamaño del botón, colocando true para que se refresque y aparezca la imagen.
                    self.matrizDesplegada[y+(i*factorDirY)][x+(i*factorDirX)-esDerecha].configure(True, height=self.tamañoBotones) # Se actualiza el tamaño del botón, colocando true para que se refresque y aparezca la imagen.
            self.resaltarImpactos(esDerecha)

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
        ##    Código dedicado a REGISTRO de los JUGADORES    ##
        #######################################################
        self.listaTemp = partidaActual.listaJugadores
        partidaActual.listaJugadores = []
        for datoJugador in self.listaTemp:
            partidaActual.listaJugadores.append(Jugador(datoJugador[0],datoJugador[1]))
        #######################################################
        ##     Código dedicado a la MATRIZ de la PARTIDA     ##
        #######################################################
        self.listaTemp = partidaActual.matrizJuego
        partidaActual.matrizJuego = [[0] * self.listaTemp[1] for _ in range(self.listaTemp[0])]
        self.numJugador = 0 # (Empieza el jugador 1 entonces es [índice 0])
        self.modoMatriz = "colocar" # Para reutilizar interfaces
        self.varBarcoColocado = CTk.StringVar()
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
                self.cambioTurno()
        # Ataque de ambos jugadores está manejado en este else if
        elif self.modoMatriz == "atacar":
            if self.numJugador == 0: 
                self.turnoJugador()
                self.cambioTurno()
            else:
                self.turnoJugador()
                self.cambioTurno()
                self.moverNaves()


    def cargarMatriz(self):
        self.matrizIzquierda = interfazMatriz(self, "#77A6BB", 0)
        self.matrizIzquierda.grid(column=1, row=1, rowspan=3)
        self.matrizDerecha = interfazMatriz(self, "#77A6BB", 1)
        self.matrizDerecha.grid(column=3, row=1, rowspan=3)
        self.frameSelecciónNave = interfazTipoNave(self)
        self.frameSelecciónNave.grid(column=2,row=1,rowspan=3,sticky="ew")
        self.labelMensaje = CTk.CTkLabel(self, width=450, height=200, font=self.fuenteTexto, text="Coloque la cabeza de la nave")
        self.labelMensaje.grid(column=1, row=0, columnspan=3, pady=20, sticky="ew")
        self.labelNavesPendientes = CTk.CTkLabel(self, width=450, height=200, font=self.fuenteTexto, text=f"Destructores ({6}) Cruceros ({4}) Acorazados ({2})")
        self.labelNavesPendientes.grid(column=1, row=4, columnspan=3, pady=20, sticky="ew")
        

    #-------------------------------------------------------------------------------------------------------------------------------------#

                      #   ---------------------------------- Ciclar Colocación para un jugador -------------------------------#

    def colocaciónJugador(self):
        # En caso de que la suma de los barcos faltantes del jugador sea 0, el ciclo termina
        while True:
            self.labelMensaje.configure(text="Coloque la cabeza de la nave")
            navesPorColocar = partidaActual.listaJugadores[self.numJugador].navesPorColocar
            self.labelNavesPendientes.configure(text=f"Destructores ({navesPorColocar[0]}) Cruceros ({navesPorColocar[1]}) Acorazados ({navesPorColocar[2]})")
            if navesPorColocar[0] + navesPorColocar[1] + navesPorColocar[2] == 0:
                return
            else:
                self.nuevoBarco()


    #-------------------------------------------------------------------------------------------------------------------------------------#

                      #   ----------------------------------  Nuevo Barco  -------------------------------------------#

    def nuevoBarco(self): 
        # Espera a recibir todas las naves del jugador
        while True:
            #temp
            for i in partidaActual.matrizJuego:
                print(i)
            self.wait_variable(self.varBarcoColocado)
            datosNave = self.varBarcoColocado.get()
            datosNave = datosNave.split(",")
            for num in range(len(datosNave)):
                datosNave[num] = int(datosNave[num])

            # Para el jugador 2 se debe considerar la segunda mitad de la matriz
            if self.numJugador == 1:
                datosNave[3] += self.matrizIzquierda.numColumnas

            print("datosNave", datosNave)
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

                      #   ----------------------------------  Verificar Barco  -------------------------------------------#

    def colocarNave(self):
        naveActual = partidaActual.listaNaves[self.numJugador][-1] # Se obtiene la nave más reciente del jugador actual
        #Se revisa si el jugador aún puede colocar este tipo de nave:
        if partidaActual.listaJugadores[self.numJugador].navesPorColocar[naveActual.tipoNave - 1] <= 0:
            self.labelMensaje.configure(text="Ya no le quedan naves de este tipo...")
            return False
        # Se utilizan índices en una lista temporal para obtener factores de dirección que definirán hacia a dónde debe simularse la posición de la nave en el tablero
        direccionesPosibles = [[0, 1],[-1, 0],[0,-1],[1, 0]] #Izquierda
        print("dirNave",naveActual.dirNave)
        factorDirX, factorDirY = direccionesPosibles[naveActual.dirNave - 1]
        for i in range(naveActual.tamañoNave):  # Se revisa según el tamaño de la nave, todas las casillas que va a ocupar en el juego
            # A la posición de la nave se le suma i + un factor de dirección que cambia según la dirección del barco para evitar repetición de código
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
        print(naveActual.listaPosTotal)
        return True

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
                    partidaActual.matrizJuego[parOrdenado[0]][parOrdenado[1]] = jugador_marca
        # Iterar sobre la lista de naves de cada jugador en el juego para marcar las posiciones hundidas
        for numJugador, jugador in enumerate(partidaActual.listaNaves):    
            for nave in jugador:        
                for parOrdenado in nave.listaPosImpacto:            
                    partidaActual.matrizJuego[parOrdenado[0]][parOrdenado[1]] = "x"


    #-------------------------------------------------------------------------------------------------------------------------------------#

                      #   ---------------------------------- Ciclar Movimiento de las Naves -------------------------------#



    def moverNaves(self):
        self.actualizarMatrizJuego()
        for naveAMover in partidaActual.listaNaves[0]: #Itera sobre cada nave en la lista de naves del jugador 1.
            direccion = naveAMover.dirNave  # Utilizar la dirección de la nave
            if direccion in [1, 2, 3, 4] and naveAMover.impactos == 0:  # Comprobar si la dirección es válida y si la nave puede moverse      
                naveMoved = False # Se asigna la variable un valor booleano con el fin de que cuando este cambie de estado el bucle finalice
                while not naveMoved: #El bucle continuará ejecutandose siempre que "naveMoved" sea falsa               
                    if direccion == 3:  # Arriba #Se compara la dirección con la selección de dirNave               
                        if naveAMover.moverArriba(): #se llaman los metodos anteriormente definidos               
                            print("Nave movida arriba.")#se imprime un mensaje indicando la dirección en la que se movió la nave                            
                            naveMoved = True #Si el movimiento es exitoso, lo iguala a True para no inicializar con las otras comparaciones y finalizar el ciclo 
                        else:
                            if naveAMover.puedeMoverMínimo: # El destructor puede tal vez moverse 1 espacio, pero no 2. Esto se encarga de ese caso
                                naveAMover.movimientoMax = 1
                                if naveAMover.moverArriba():
                                    print("Nave movida arriba.")#se imprime un mensaje indicando la dirección en la que se movió la nave                            
                                    naveMoved = True
                                naveAMover.movimientoMax = 2 # Se re-establece el movimiento máximo del destructor
                            else:
                                naveMoved = True
                    ## La logica se repite para abarcar los posibles casos ##    
                    elif direccion == 1:  # Abajo         
                        if naveAMover.moverAbajo():                    
                            print("Nave movida abajo.")                                  
                            naveMoved = True      
                        else:
                            if naveAMover.puedeMoverMínimo: # El destructor puede tal vez moverse 1 espacio, pero no 2. Esto se encarga de ese caso
                                naveAMover.movimientoMax = 1
                                if naveAMover.moverAbajo():
                                    print("Nave movida abajo.")#se imprime un mensaje indicando la dirección en la que se movió la nave                            
                                    naveMoved = True
                                naveAMover.movimientoMax = 2
                            else:
                                naveMoved = True   
                    elif direccion == 2:  # Izquierda
                        if naveAMover.moverIzquierda():
                            print("Nave movida izquierda.")
                            naveMoved = True
                        else:
                            if naveAMover.puedeMoverMínimo: # El destructor puede tal vez moverse 1 espacio, pero no 2. Esto se encarga de ese caso
                                naveAMover.movimientoMax = 1
                                if naveAMover.moverIzquierda():
                                    print("Nave movida izquierda.")#se imprime un mensaje indicando la dirección en la que se movió la nave                            
                                    naveMoved = True
                                naveAMover.movimientoMax = 2
                            else:
                                naveMoved = True
                    elif direccion == 4:  # Derecha
                        if naveAMover.moverDerecha():
                            print("Nave movida derecha.")
                            naveMoved = True
                        else:
                            if naveAMover.puedeMoverMínimo: # El destructor puede tal vez moverse 1 espacio, pero no 2. Esto se encarga de ese caso
                                naveAMover.movimientoMax = 1
                                if naveAMover.moverDerecha():
                                    print("Nave movida derecha.")#se imprime un mensaje indicando la dirección en la que se movió la nave                            
                                    naveMoved = True
                                naveAMover.movimientoMax = 2
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

    
    #-------------------------------------------------------------------------------------------------------------------------------------#

                      #   ----------------------------------  Realizar 1 Turno de Ataque  -------------------------------------------#

    def turnoJugador(self):
        while True:    
            #esperar input
            self.wait_variable(self.varBarcoColocado)
            #5. revisar ataque
        #6. verificar fin partida
            pass
    
    #-------------------------------------------------------------------------------------------------------------------------------------#

                      #   ----------------------------------  Cambiar de un Jugador a Otro  -------------------------------------------#

    def cambioTurno(self):
        self.numJugador = 0 if (self.numJugador+1) != 1 else 1
        if self.numJugador == 0: self.matrizIzquierda.actualizarMatrizParaJugadorActual(0)
        else: self.matrizDerecha.actualizarMatrizParaJugadorActual(self.matrizIzquierda.numColumnas)
        if self.numJugador == 1: self.matrizIzquierda.ocultarMatrizOponente(0)
        else: self.matrizDerecha.ocultarMatrizOponente(self.matrizIzquierda.numColumnas)
        self.estadoMensaje = f"Turno de '{partidaActual.listaJugadores[self.numJugador].nickName}'"
        self.frameCubierta = CTk.CTkFrame(self,width=200,height=200,corner_radius=0,fg_color=self.colorCubierta[0 if (self.numJugador+1) != 1 else 1])
        self.frameCubierta.grid(column=0, row=0, padx=0, pady=0, sticky="nsew", columnspan=5, rowspan=5)
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
        self.btnCubierta.tkraise()
        if self.modoMatriz == "atacar":
            self.actualizarMatrizJuego()
            hundidosJugador = partidaActual.listaJugadores[self.numJugador].numHundimientos
            self.labelNavesPendientes.configure(text=f"Destructores ({6-hundidosJugador[0]}) Cruceros ({4-hundidosJugador[1]}) Acorazados ({2-hundidosJugador[2]})")


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
