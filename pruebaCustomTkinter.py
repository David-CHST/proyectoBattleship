import customtkinter
from PIL import Image, ImageTk
import random

#archivo de pruebas con Tkinter

#Se guardan imágenes en una lista para ser usadas por el programa
listaImágenes=[["Naves/b1 (Custom).png"], ["Naves/b22 (Custom).png", "Naves/b21 (Custom).png", ], ["Naves/b33 (Custom).png", "Naves/b32 (Custom).png", "Naves/b31 (Custom).png"]]

# Se crea una clase de cuadrícula para crear 2 matrices sin tener que repetir código
# Hereda atributos de una clase padre: "customtkinter.CTkFrame"
# Un frame es una especie de contenedor para otros objetos, (como el panel gris que está detrás de los botones, conteniendo la matriz de botones en su interior)
class cuadrículaMatriz(customtkinter.CTkFrame):
    # Al iniciarse la matriz pide los argumentos de master (la ventana principal) y del color del foreground de los botones (fgColor)
    def __init__(self, master, fgColor):
        # En la documentación dice que se debe hacer esta siguiente línea, porque inicializa la clase padre de esta clase.
        # Es decir, sin esta línea, la clase "cuadrículaMatriz" no tendría los poderes de un "customtkinter.CTkFrame", que es lo que deseamos para contener los botones
        super().__init__(master) 
        # Se crean 10 columnas con weight=1, que les dice que tomen el espacio que necesiten
        self.grid_columnconfigure(tuple(range(10)), weight=1) #se hace un range, y el range se convierte en una tupla porque solo acepta tuplas ese primer argumento
        # Se crean 10 filas con weight=1, que les dice que tomen el espacio que necesiten
        self.grid_rowconfigure(tuple(range(10)), weight=1)

        # Se crea una variable (está adentro de la clase entonces debe decir self.NOMBRE_VARIABLE)
        self.matrizDesplegada = []

        # Se agregan 10 filas a la matriz
        for i in range(10):
            self.matrizDesplegada.append([])
            # Por cada fila se rellenan las columnas con 10 botones
            for j in range(10):
                # El botón debe ser metido en la lista de matrizDesplegada 
                # Se le deben asignar atributos al crearlo con "customtkinter.CTkButton()"
                # Los argumentos que yo le dí aquí son respectivamente: 
                #customtkinter.CTkButton(objeto que es dueño de este botón, tamaño del borde redondeado, 
                #                        texto que representa las coordenadas en la matriz, ancho del botón, 
                #                        alto del botón, color del botón (fg = foreground), 
                #                        inicializar la imágen vacía, y la acción que hace al presionarse (lambda con dos argumentos metidos en una tupla para llamar la función)
                # hay más argumentos, pero por defecto tienen valores que me sirven
                # Por ejemplo: Al poner el mouse por encima se resalta en azul
                self.matrizDesplegada[-1].append(customtkinter.CTkButton(self, corner_radius=4, text=f"{i}, {j}", width=55, height=55, fg_color=fgColor, image=None, command=lambda a=(i, j): self.presionarBotón(a[0],a[1])))
                # Antes de explicar lo que hice a continuación, hay que explicar "padding"
                # Usted puede establecer "padx" y "pady" que son los pixeles de espacio personal que tiene el objeto
                # Nadie se va a acercar a ese widget hasta después de esa cantidad de pixeles.
                # En este caso, los botones tienen padx=2 y pady=2 para que guarden distancia de 2 pixeles entre sí mismos, para que no se vean tan pegados
                # Al final de esta línea de código está el argumento "sticky", que hace que se distribuyan en las direcciones cardinales que contenga el string
                # Como en este string están todas las iniciales de las direcciones cardinales, se distribuye en las 4 direcciones (north, south, east, west = "nsew")
                self.matrizDesplegada[-1][-1].grid(row=i,column=j,padx=2,pady=2, sticky="nsew") 

        # Este siguiente segmeto es un despijeo de espaguetti de código pero por mi propia incompetencia
        # Esto no es culpa del programa, es culpa mía de que no sé cómo darle un "padding" al frame en lugar de darle un "padding" a cada botón del borde
        # Sin este siguiente cuadro de código el programa todavía funciona, pero no tendría el bordecito gris lindo que hay a los bordes donde terminan los botones.
        ############ Inicio Spaghetti ##############
        # Básicamente ciclo por todas las laterales de la matriz de botones y les digo que guarden un padding de 20 según la direccion a la que se encuentra el final
        # Este ciclo para filas
        for i in range(10):
            self.matrizDesplegada[i][0].grid(row=i,column=0,padx=(20,2),pady=(2,2), sticky="nsew")
            self.matrizDesplegada[i][-1].grid(row=i,column=9,padx=(2,20),pady=(2,2), sticky="nsew")
        # Este ciclo para columnas
        for i in range(10):
            self.matrizDesplegada[0][i].grid(row=0,column=i,padx=(2,2),pady=(20,2), sticky="nsew")
            self.matrizDesplegada[-1][i].grid(row=9,column=i,padx=(2,2),pady=(2,20), sticky="nsew")
        # Estos 4 casos excepcionales para las esquinas, que deben tener padding a dos lados diferentes
        self.matrizDesplegada[0][0].grid(row=0,column=0,padx=(20,2),pady=(20,2), sticky="nsew")
        self.matrizDesplegada[9][9].grid(row=9,column=9,padx=(2,20),pady=(2,20), sticky="nsew")
        self.matrizDesplegada[0][9].grid(row=0,column=9,padx=(2,20),pady=(20,2), sticky="nsew")
        self.matrizDesplegada[9][0].grid(row=9,column=0,padx=(20,2),pady=(2,20), sticky="nsew")
        ############ Fin Spaghetti #################
        # Y listo, cuando se vaya a crear la clase con "cuadrículaMatriz(argumentosAquí)" todo este código corre para que exista una nueva cuadrícula de botones

    # Al presionar el botón se ejecuta esto
    # Esta función es un despelote de prueba que lo que hace es quitar el texto y colocar imágenes
    def presionarBotón(self,i,j):
        print("i",i,"j", j)
        tipoNave = random.randint(0,2) # para esto es la librería random, solo para esto jaja
        for x in range(tipoNave+1):
            # Hace un nuevo objeto de imagen CTkImage y abre la imagen con PIL.Image.open()...(solo "Image" aquí por como se importó)
            buttonImage = customtkinter.CTkImage(Image.open(listaImágenes[tipoNave][x]), size=(42,42)) 
            self.matrizDesplegada[i][j+x].configure(text="") # Configura el botón para que sea solo texto
            self.matrizDesplegada[i][j+x].configure(image=buttonImage) # Se coloca la imagen en el botón
            self.matrizDesplegada[i][j+x].configure(True, width=55) # Se actualiza el tamaño del botón, colocando true para que se refresque y aparezca la imagen.
            self.matrizDesplegada[i][j+x].configure(True, height=55) # Se actualiza el tamaño del botón, colocando true para que se refresque y aparezca la imagen.


# Esta es la clase de la app principal, para más información de clases vea los comentarios anteriores o pregúnteme jeje
class principalApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # título de la ventana
        self.title("my app")
        # Dimensiones de la ventana
        self.geometry("1400x800")
        
        # Se crean 5 columnas por capricho porque se usan 2
        self.grid_columnconfigure((0,1,2,3,4), weight=1)
        # Se crean 3 filas por capricho, porque se usa 1
        self.grid_rowconfigure((0,1,2), weight=1)

        # Se crean 2 variables dentro de esta clase, una para cada frame de botones (una cuadrícula)
        # Se les da el parámetro del dueño y el color de botón deseado
        # No sé por qué gray40 es más oscuro que gray60 pero así funcionó jajaja
        self.frame1Cuadrícula = cuadrículaMatriz(self, "gray40")
        # Luego de crear el objeto se coloca en la hipotética cuadrícula que tiene la ventana principal
        self.frame1Cuadrícula.grid(row=1, column=1, padx=5, pady=(10, 0), columnspan=1, sticky="ew") # Colocado en fila 1 columna 1, tomando todo el espacio en east y west (sticky= "ew") (ver comentarios de más arriba)
        # Se crea la segunda cuadrícula de botones
        self.frame2Cuadrícula = cuadrículaMatriz(self, "gray60")
        # Luego de crear el objeto se coloca en la hipotética cuadrícula que tiene la ventana principal
        self.frame2Cuadrícula.grid(row=1, column=3, padx=5, pady=(10, 0), columnspan=1, sticky="ew") # Colocado en fila 1 columna 3, tomando todo el espacio en east y west (sticky= "ew") (ver comentarios de más arriba)

# Igual que tkinter, se corre la app con mainloop()
ventanaPrincipal = principalApp() # Se crea una instancia de la clase de ventana principal y se guarda en una variable para ejecutarle el .mainloop()
ventanaPrincipal.mainloop()
