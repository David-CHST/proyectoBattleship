import customtkinter
from PIL import Image, ImageTk
import random

#archivo de pruebas con Tkinter

listaImágenes=[["Naves/b1 (Custom).png"], ["Naves/b22 (Custom).png", "Naves/b21 (Custom).png", ], ["Naves/b33 (Custom).png", "Naves/b32 (Custom).png", "Naves/b31 (Custom).png"]]

class cuadrículaMatriz(customtkinter.CTkFrame):
    def __init__(self, master, fgColor):
        super().__init__(master) # En la documentación dice que se debe hacer esto para llamar el método de crear clases de interfaz
        self
        self.grid_columnconfigure(tuple(range(10)), weight=1)
        self.grid_rowconfigure(tuple(range(10)), weight=1)

        self.matrizDesplegada = []
        for i in range(10):
            self.matrizDesplegada.append([])
            for j in range(10):
                self.matrizDesplegada[-1].append(customtkinter.CTkButton(self, corner_radius=4, border_width=0, text=f"{i}, {j}", width=55, height=55, fg_color=fgColor, image=None, command=lambda a=(i, j): self.presionarBotón(a[0],a[1])))
                self.matrizDesplegada[-1][-1].grid(row=i,column=j,padx=2,pady=2, sticky="ew")
                self.matrizDesplegada[-1][-1].configure(True, width=55)
                self.matrizDesplegada[-1][-1].configure(True, height=55)
        for i in range(10):
            self.matrizDesplegada[i][0].grid(row=i,column=0,padx=(20,2),pady=(2,2), sticky="ew")
            self.matrizDesplegada[i][-1].grid(row=i,column=9,padx=(2,20),pady=(2,2), sticky="ew")
        for i in range(10):
            self.matrizDesplegada[0][i].grid(row=0,column=i,padx=(2,2),pady=(20,2), sticky="ew")
            self.matrizDesplegada[-1][i].grid(row=9,column=i,padx=(2,2),pady=(2,20), sticky="ew")
        self.matrizDesplegada[0][0].grid(row=0,column=0,padx=(20,2),pady=(20,2), sticky="ew")
        self.matrizDesplegada[9][9].grid(row=9,column=9,padx=(2,20),pady=(2,20), sticky="ew")
        self.matrizDesplegada[0][9].grid(row=0,column=9,padx=(2,20),pady=(20,2), sticky="ew")
        self.matrizDesplegada[9][0].grid(row=9,column=0,padx=(20,2),pady=(2,20), sticky="ew")
    
    def presionarBotón(self,i,j):
        print("i",i,"j", j)
        tipoNave = random.randint(0,2)
        match tipoNave:
            case 0:
                for x in range(1):
                    buttonImage = customtkinter.CTkImage(light_image=Image.open(listaImágenes[tipoNave][x]), size=(42,42))
                    self.matrizDesplegada[i][j+x].configure(text="")
                    self.matrizDesplegada[i][j+x].configure(image=buttonImage)
                    self.matrizDesplegada[i][j+x].configure(True, width=55)
                    self.matrizDesplegada[i][j+x].configure(True, height=55)
            case 1:
                for x in range(2):
                    buttonImage = customtkinter.CTkImage(Image.open(listaImágenes[tipoNave][x]), size=(42,42))
                    self.matrizDesplegada[i][j+x].configure(text="")
                    self.matrizDesplegada[i][j+x].configure(True, image=buttonImage)
                    self.matrizDesplegada[i][j+x].configure(True, width=55)
                    self.matrizDesplegada[i][j+x].configure(True, height=55)
            case 2:
                for x in range(3):
                    buttonImage = customtkinter.CTkImage(Image.open(listaImágenes[tipoNave][x]), size=(42,42))
                    self.matrizDesplegada[i][j+x].configure(text="")
                    self.matrizDesplegada[i][j+x].configure(image=buttonImage)
                    self.matrizDesplegada[i][j+x].configure(True, width=55)
                    self.matrizDesplegada[i][j+x].configure(True, height=55)
        
class principalApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("1400x800")
        
        self.grid_columnconfigure((0,1,2,3,4), weight=1)
        self.grid_rowconfigure((0,1,2), weight=1)

        #self.checkbox_frame = MyCheckboxFrame(self)
        self.frame1Cuadrícula = cuadrículaMatriz(self, "gray40")
        self.frame1Cuadrícula.grid(row=1, column=1, padx=5, pady=(10, 0), columnspan=1, sticky="ew")
        self.frame2Cuadrícula = cuadrículaMatriz(self, "gray60")
        self.frame2Cuadrícula.grid(row=1, column=3, padx=5, pady=(10, 0), columnspan=1, sticky="ew")

        #self.button = customtkinter.CTkButton(self, text="my button", command=self.presionarBotón)
        #self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=3)

    
ventanaPrincipal = principalApp()
ventanaPrincipal.mainloop()
