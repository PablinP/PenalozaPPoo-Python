import tkinter as tk
from tkinter import *
import tkinter as Tk
from PIL import Image, ImageTk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np # Importamos numpy como el alias np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 



#Login
ventanaLogin = tk.Tk() 
ventanaLogin.title("Login")
ventanaLogin.geometry("350x300+500+50")
ventanaLogin.resizable (width=False, height=False) 
#fondo = tk. PhotoImage(file="Foto1.gif")
fondo1 = tk.Label (ventanaLogin, background="#005588").place(x=0, y=0, relwidth=1, relheight=1)
mensajetitutlo1="Proyecto Final"
labelMensaje3=Tk.Label(ventanaLogin,text=mensajetitutlo1,justify=Tk.LEFT,background="#005588",
fg="white",font=("Comic Sans MS", 20, "bold")).place(x=75,y=5)
mensajetitutlo="Bienvenido"
labelMensaje3=Tk.Label(ventanaLogin,text=mensajetitutlo,justify=Tk.LEFT,background="#005588",
fg="white",font=("Comic Sans MS", 20, "bold")).place(x=100,y=50)
mensajeUusario="Usuario"
labelMensaje4=Tk.Label(ventanaLogin,text=mensajeUusario,justify=Tk.LEFT,background="#005588",
fg="white",font=("Comic Sans MS", 14, "bold")).place(x=30,y=100)
mensajeContraseña="Contraseña"
labelMensaje5=Tk.Label(ventanaLogin,text=mensajeContraseña,justify=Tk.LEFT,background="#005588",
fg="white",font=("Comic Sans MS", 14, "bold")).place(x=30,y=140)


#####################################################################################

usuario= StringVar()
password=StringVar()

# Entradas
entrada = tk. Entry (ventanaLogin, textvar=usuario, width=22, relief="flat", 
bg="#646464",foreground="black") .place(x=150, y=110)
entrada2 = tk. Entry (ventanaLogin, textvar=password, width=22, show="*",relief="flat", 
bg="#646464",foreground="black") .place (x=150, y=150)

#####################################################################################
#Funciones
def Ingresar():

       
    if usuario.get() == "Pablin" and password.get() == "1234":
        
        Principal()
        
    else:
        Incorrecta()


#####################################################################################
def Incorrecta():
    messagebox.showerror("ERROR","Datos Incorrectos")
    
#####################################################################################
def Principal():
    
    '''ventanaLogin.withdraw()
    window = tk.Tk() 
    window.title("Login")
    window.geometry("500x500+500+50")
    window.resizable (width=False, height=False) 
    #fondo = tk. PhotoImage(file="Foto1.gif")
    fondo1 = tk.Label (ventanaLogin, background="green").place(x=0, y=0, relwidth=1, relheight=1)'''
    #Ventana#
    ventanaLogin.withdraw()
    Ventana= Tk.Toplevel()
    Ventana.title("Proyecto Final")
    Ventana.geometry("1000x600")
    Ventana.geometry("+150+45")
    #Para que no se pueda cambiar de tamaño#
    Ventana.resizable(1,1)
    Ventana.iconbitmap("proyectofinal.ico")
    Fondo = PhotoImage(file="Fondo2.gif")
    fondo1=Label(Ventana, image=Fondo).place(x=1,y=1, relheight=1,relwidth=1)

    menu=Menu(Ventana)
    Ventana.config(menu=menu)

#####################################################################################
    def V_Matplot():
        ventanaMatplot = tk.Toplevel() 
        ventanaMatplot.title("Grafico Libreria Matplotlib")
        ventanaMatplot.geometry("350x300+500+100")
        ventanaMatplot.resizable (width=False, height=False) 
        fondo1 = tk.Label (ventanaMatplot, background="#080736").place(x=0, y=0, relwidth=1, relheight=1)
        mensajetitutloMatplt="Libreria  Matplot"
        labelMensajeMatplot=Tk.Label(ventanaMatplot,text=mensajetitutloMatplt,justify=Tk.LEFT,
        background="#080736",fg="white",
        font=("Comic Sans MS", 20, "bold")).place(x=60,y=10)

        objetivo= StringVar()
        meses=StringVar()

        entrada = tk. Entry (ventanaMatplot, textvar=objetivo, width=22, relief="flat", 
        bg="white") .place(x=160, y=70)
        mensajeejesx="X:Meses"
        labelMensajex=Tk.Label(ventanaMatplot,text=mensajeejesx,justify=Tk.LEFT,
        background="#080736",fg="white",
        font=("Comic Sans MS", 14, "bold")).place(x=20,y=60)

        entrada2 = tk. Entry (ventanaMatplot, textvar=meses, width=22, relief="flat", 
        bg="white") .place(x=160, y=110)
        mensajeejesy="Y:Ventas"
        labelMensajey=Tk.Label(ventanaMatplot,text=mensajeejesy,justify=Tk.LEFT,
        background="#080736",fg="white",
        font=("Comic Sans MS", 14, "bold")).place(x=20,y=100)

        arrayObjetivo=[]
        arrayMeses=[]

        def Ingresar1():
            arrayMeses.append(float(meses.get()))
            print(arrayMeses)
            
                   
        def Ingresar2():
            arrayObjetivo.append(float(objetivo.get()))
            print(arrayObjetivo)
            

        def graficar():
            fig, ax = plt.subplots()
            ax.bar(arrayObjetivo, arrayMeses)
            plt.xlabel("Meses", fontsize = 20, color= 'blue')
            plt.title("Ventas", fontsize = 20)
            plt.ylabel("Objetivo", fontsize = 20, color = 'blue')
            plt.show()
        
      
        graficar1 = tk.Button(ventanaMatplot, text="Graficar",command=graficar, 
        cursor="hand2", bg_="#120A8F", width=12,height=1, relief="flat",border=1,foreground="white",
        font=("Comic Sans MS", 12, "bold"))
        graficar1.place(x=100, y=200)

        IngresarDatosy = tk.Button(ventanaMatplot, text="Ventas",command=Ingresar1, 
        cursor="hand2", bg="#4B4B4B", width=12,height=1, relief="flat",border=0,foreground="white",
        font=("Comic Sans MS", 12, "bold"))
        IngresarDatosy.place(x=180, y=150)

        IngresarDatosx = tk.Button(ventanaMatplot, text="Meses",command=Ingresar2, 
        cursor="hand2", bg_="#4B4B4B", width=12,height=1, relief="flat",border=1,foreground="white",
        font=("Comic Sans MS", 12, "bold"))
        IngresarDatosx.place(x=20, y=150)

        
        def graficoMatplot():
            a =np.linspace(0,20,50)
            b= np.sin(a)
            c=plt.plot(a, b, 'c-3', linewidth = 2)
            c=plt.plot(a+0.2, b-1, 'r-o', linewidth = 2)
             
            plt.xlabel("Tiempo (s)", fontsize = 20, color= 'blue')
            plt.ylabel(r"$Distancia$", fontsize = 20, color = 'blue')
            plt.text(30,30, "Más texto", fontsize = 12)
            plt.title("Velocidad (m/s)", fontsize = 20)
            plt.legend( ('Etiqueta1', 'Etiqueta2', 'Etiqueta3'), loc = 'best')
            plt.grid(True)
            plt.savefig('F_Matplot1.png', dpi = 300) #guarda la gráfica con 300dpi (puntos por pulgada)
            plt.show()
            
##*************************************************************************************************##
        #crear una ventana#
    def ConceptoMatplot():
        v_matplot1 = Tk.Toplevel()
        v_matplot1.title("Libreria Matplot")
        v_matplot1.geometry("550x540")
        v_matplot1.geometry("+380+98")
        v_matplot1.configure()
        mensaje="La Libreria de Matplot"
        labelMensaje=Tk.Label(v_matplot1,text=mensaje,justify=Tk.CENTER,font=32,fg="red").pack()
        mensaje1="""    Matplotlib es una librería de Python especializada en la creación de gráficos en dos dimensiones.
        Permite crear y personalizar los tipos de gráficos más comunes, entre ellos:
            -Diagramas de barras
            -Histograma
            -Diagramas de sectores
            -Diagramas de caja y bigotes
            -Diagramas de violín
            -Diagramas de dispersión o puntos
            -Diagramas de lineas
            -Diagramas de areas
            -Diagramas de contorno
            -Mapas de color
        y combinaciones de todos ellos."""
        labelMensaje1=Tk.Label(v_matplot1,text=mensaje1,justify=Tk.LEFT,fg="blue").pack()
    
        mensaje2="Creación de gráficos con matplotlib"
        labelMensaje2=Tk.Label(v_matplot1,text=mensaje2,fg="red",font=1).place(x=20,y=230)
    
        mensaje3="""Para crear un gráfico con matplotlib es habitual seguir los siguientes pasos:

            1.-Importar el módulo pyplot.

            2.-Definir la figura que contendrá el gráfico, que es la region (ventana o página) 
            donde se dibujará y los ejes sobre los que se dibujarán los datos. Para ello se 
            utiliza la función subplots().

            3.-Dibujar los datos sobre los ejes. Para ello se utilizan distintas funciones 
            dependiendo del tipo de gráfico que se quiera.
            4.-Personalizar el gráfico. Para ello existen multitud de funciones que permiten 
            añadir un título, una leyenda, una rejilla, cambiar colores o personalizar los ejes.

            5.-Guardar el gráfico. Para ello se utiliza la función savefig().

            6.-Mostrar el gráfico. Para ello se utiliza la función show().


            """
        labelMensaje3=Tk.Label(v_matplot1,text=mensaje3,justify=Tk.LEFT,fg="blue").place(x=20,y=260)
##*************************************************************************************************##   
         
        v_matplot1.mainloop()
##*************************************************************************************************##
    def SalirMatplot():
        Ventana.withdraw()
        Ventana.deiconify()
###################################################################################################
    Matplot=Menu(menu, tearoff=0)
    Matplot.add_command(label="Concepto",command=ConceptoMatplot)
    Matplot.add_command(label="Ejemplo",command=V_Matplot)
    Matplot.add_command(label="Regresar",command=SalirMatplot)
###################################################################################################
    def V_Seaborn():
        ventanaSeaborn = tk.Toplevel() 
        ventanaSeaborn.title("Grafico Libreria Seaborn")
        ventanaSeaborn.geometry("350x400+500+100")
        ventanaSeaborn.resizable (width=False, height=False) 
        fondo1 = tk.Label (ventanaSeaborn, background="#003153").place(x=0, y=0, relwidth=1, relheight=1)
        mensajetitutloSeaborn="Libreria  Seaborn"
        labelMensajeSeaborn=Tk.Label(ventanaSeaborn,text=mensajetitutloSeaborn,justify=Tk.LEFT,
        background="#003153",fg="white",
        font=("Comic Sans MS", 20, "bold")).place(x=60,y=10)

        Personal= StringVar()
        tareas=StringVar()
        minuto=StringVar()

        entrada = tk. Entry (ventanaSeaborn, textvar=Personal, width=22, relief="flat", 
        bg="white") .place(x=160, y=70)
        mensajeejesx="X:Personal"
        labelMensajex=Tk.Label(ventanaSeaborn,text=mensajeejesx,justify=Tk.LEFT,
        background="#003153",fg="white",
        font=("Comic Sans MS", 14, "bold")).place(x=20,y=60)

        entrada2 = tk. Entry (ventanaSeaborn, textvar=tareas, width=22, relief="flat", 
        bg="white") .place(x=160, y=110)
        mensajeejesy="Y:Tareas"
        labelMensajey=Tk.Label(ventanaSeaborn,text=mensajeejesy,justify=Tk.LEFT,
        background="#003153",fg="white",
        font=("Comic Sans MS", 14, "bold")).place(x=20,y=100)

        entrada3 = tk. Entry (ventanaSeaborn, textvar=minuto, width=22, relief="flat", 
        bg="white") .place(x=160, y=150)
        mensajeejesy="Y:Indice"
        labelMensajey=Tk.Label(ventanaSeaborn,text=mensajeejesy,justify=Tk.LEFT,
        background="#003153",fg="white",
        font=("Comic Sans MS", 14, "bold")).place(x=20,y=140)

        arrayPersonal=[]
        arrayTareas=[]
        arrayMinutos=[]

        def Ingresar1():
            arrayTareas.append(float(tareas.get()))
            print(arrayTareas)
            
                   
        def Ingresar2():
            arrayPersonal.append(float(Personal.get()))
            print(arrayPersonal)

        def Ingresar3():
            arrayMinutos.append(float(minuto.get()))
            print(arrayMinutos)


        def graficar():
            x = arrayPersonal
            y_bar = arrayTareas
            y_line = arrayMinutos

            sns.set()  # Declarar el uso del estilo Seaborn

            plt.bar(x, y_bar)
            plt.plot(x, y_line, '-o', color='y')
            plt.xlabel("Personal", fontsize = 20, color= 'blue')
            plt.title("Productividad", fontsize = 20)
            plt.ylabel("Tareas", fontsize = 20, color = 'blue')
            plt.show()
            '''fig, ax = plt.subplots()
            ax.bar(arrayDias, arrayYear)
            plt.xlabel("Meses", fontsize = 20, color= 'blue')
            plt.title("Ventas", fontsize = 20)
            plt.ylabel("Objetivo", fontsize = 20, color = 'blue')
            plt.show()'''
           

        
        graficar1 = tk.Button(ventanaSeaborn, text="Graficar",command=graficar, 
        cursor="hand2", bg_="#120A8F", width=12,height=1, relief="flat",border=1,foreground="white",
        font=("Comic Sans MS", 12, "bold"))
        graficar1.place(x=20, y=250)

        IngresarDatosy = tk.Button(ventanaSeaborn, text="Tareas",command=Ingresar1, 
        cursor="hand2", bg="#4B4B4B", width=12,height=1, relief="flat",border=0,foreground="white",
        font=("Comic Sans MS", 12, "bold"))
        IngresarDatosy.place(x=180, y=200)

        IngresarDatosx = tk.Button(ventanaSeaborn, text="Personal",command=Ingresar2, 
        cursor="hand2", bg_="#4B4B4B", width=12,height=1, relief="flat",border=1,foreground="white",
        font=("Comic Sans MS", 12, "bold"))
        IngresarDatosx.place(x=20, y=200)

        IngresarDatosyy = tk.Button(ventanaSeaborn, text="Indice",command=Ingresar3, 
        cursor="hand2", bg_="#4B4B4B", width=12,height=1, relief="flat",border=1,foreground="white",
        font=("Comic Sans MS", 12, "bold"))
        IngresarDatosyy.place(x=180, y=250)





        def GraficoSeaborn():
        # Definir datos de dibujo
            x = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
            y_bar = [3, 8, 6, 8, 9, 10, 9, 11, 7, 8]
            y_line = [2, 9, 5, 7, 8, 9, 8, 10, 6, 7]

            sns.set()  # Declarar el uso del estilo Seaborn

            plt.bar(x, y_bar)
            plt.plot(x, y_line, '-o', color='y')
            plt.show()
##*************************************************************************************************##
    #crear una ventana#
    def ConceptoSeaborn():
        v_seaborn1 = Tk.Toplevel()
        v_seaborn1.title("Libreria Seaborn")
        v_seaborn1.geometry("550x540")
        v_seaborn1.geometry("+380+98")
        v_seaborn1.configure()
        mensaje="La Libreria de Seaborn"
        labelMensaje=Tk.Label(v_seaborn1,text=mensaje,justify=Tk.CENTER,font=32,fg="red").pack()
        mensaje1="""            Seaborn es una librería de visualización de datos para Python desarrollada 
            sobre matplotlib. Ofrece una interfaz de alto nivel para la creación de atractivas gráficas. 
            Además, está íntimamente integrada con las estructuras de datos de pandas, lo que permite 
            utilizar el nombre de los DataFrames y campos directamente como argumentos de las funciones 
            de visualización.

            seaborn tiene como objetivo convertir la visualización en una parte central de la exploración 
            y comprensión de los datos, generando atractivas gráficas con sencillas funciones que ofrecen 
            una interfaz semejante, facilitando el paso de unas funciones a otras.
            y combinaciones de todos ellos."""
        labelMensaje1=Tk.Label(v_seaborn1,text=mensaje1,justify=Tk.LEFT,fg="blue").pack()
    
        mensaje2="Seaborn ofrece varias características destacadas como: "
        labelMensaje2=Tk.Label(v_seaborn1,text=mensaje2,fg="red",font=1).place(x=20,y=230)
    
        mensaje3=""" 
            1.-Gráficas visualmente atractivas sin necesidad de realizar complicados ajustes.

            2.-Una API orientada a conjuntos de datos para examinar la relación entre múltiples
               variables.

            3.-Opciones para mostrar la distribución de variables univariadas y bivariadas.

            4.-Cálculo automático y dibujo de modelos de regresión lineal para diferentes tipos de 
                variables dependientes.

            5.-Herramientas para mostrar la estructura de datasets complejos.

            6.-Sencillo control sobre los estilos gráficos disponibles.

            7.-Herramientas para la elección de paletas de color adecuadas que permitan revelar 
               patrones en los datos.
              
                   
        """
        labelMensaje3=Tk.Label(v_seaborn1,text=mensaje3,justify=Tk.LEFT,fg="blue").place(x=20,y=260)
##*************************************************************************************************##        
        v_seaborn1.mainloop()
##*************************************************************************************************##
    def SalirSeaborn():
        Ventana.withdraw()
        Ventana.deiconify()
###################################################################################################    
    Seaborn=Menu(menu, tearoff=0)
    Seaborn.add_command(label="Concepto",command=ConceptoSeaborn)
    Seaborn.add_command(label="Ejemplo",command=V_Seaborn)
    Seaborn.add_command(label="Regresar",command=SalirSeaborn)
###################################################################################################    
    def G_Panda():
        ventanaPanda = tk.Toplevel() 
        ventanaPanda.title("Grafico Libreria Panda")
        ventanaPanda.geometry("350x400+500+100")
        ventanaPanda.resizable (width=False, height=False) 
        fondo1 = tk.Label (ventanaPanda, background="#0088b6").place(x=0, y=0, relwidth=1, relheight=1)
        mensajetitutloPanda="Libreria Panda"
        labelMensajePanda=Tk.Label(ventanaPanda,text=mensajetitutloPanda,justify=Tk.LEFT,
        background="#0088b6",fg="white",
        font=("Comic Sans MS", 20, "bold")).place(x=60,y=10)

        homicidio= StringVar()
        year=StringVar()
        minuto=StringVar()

        entrada = tk. Entry (ventanaPanda, textvar=homicidio, width=22, relief="flat", 
        bg="white") .place(x=160, y=70)
        mensajeejesx="X:Trimestres"
        labelMensajex=Tk.Label(ventanaPanda,text=mensajeejesx,justify=Tk.LEFT,
        background="#0088b6",fg="white",
        font=("Comic Sans MS", 14, "bold")).place(x=20,y=60)

        entrada2 = tk. Entry (ventanaPanda, textvar=year, width=22, relief="flat", 
        bg="white") .place(x=160, y=110)
        mensajeejesy="IngresosQ"
        labelMensajey=Tk.Label(ventanaPanda,text=mensajeejesy,justify=Tk.LEFT,
        background="#0088b6",fg="white",
        font=("Comic Sans MS", 14, "bold")).place(x=20,y=100)

        entrada3 = tk. Entry (ventanaPanda, textvar=minuto, width=22, relief="flat", 
        bg="white") .place(x=160, y=150)
        mensajeejesy="IngresosA"
        labelMensajey=Tk.Label(ventanaPanda,text=mensajeejesy,justify=Tk.LEFT,
        background="#0088b6",fg="white",
        font=("Comic Sans MS", 14, "bold")).place(x=20,y=140)

        arrayDias=[]
        arrayYear=[]
        arrayMinutos=[]

        def Ingresar1():
            arrayYear.append(float(year.get()))
            print(arrayYear)
            
                   
        def Ingresar2():
            arrayDias.append(float(homicidio.get()))
            print(arrayDias)

        def Ingresar3():
            arrayMinutos.append(float(minuto.get()))
            print(arrayMinutos)
            

        def graficar():
            df = pd.DataFrame({'Años':arrayDias, 
                   'Quito':arrayYear, 
                   'Ambato':[85.5, 25.5, 55.5]})
            df = df.set_index('Años')
            fig, ax = plt.subplots()
            df.plot(ax = ax)
            plt.title("Balance de Ingresos de Quito y Ambato", fontsize = 20)
            plt.show()

        

        graficar1 = tk.Button(ventanaPanda, text="Graficar",command=graficar, 
        cursor="hand2", bg_="#120A8F", width=12,height=1, relief="flat",border=1,foreground="white",
        font=("Comic Sans MS", 12, "bold"))
        graficar1.place(x=20, y=250)

        IngresarDatosy = tk.Button(ventanaPanda, text="IngresoQ",command=Ingresar1, 
        cursor="hand2", bg="#4B4B4B", width=12,height=1, relief="flat",border=0,foreground="white",
        font=("Comic Sans MS", 12, "bold"))
        IngresarDatosy.place(x=180, y=200)

        IngresarDatosx = tk.Button(ventanaPanda, text="Trimestre",command=Ingresar2, 
        cursor="hand2", bg_="#4B4B4B", width=12,height=1, relief="flat",border=1,foreground="white",
        font=("Comic Sans MS", 12, "bold"))
        IngresarDatosx.place(x=20, y=200)

        IngresarDatosyy = tk.Button(ventanaPanda, text="IngresoA",command=Ingresar3, 
        cursor="hand2", bg_="#4B4B4B", width=12,height=1, relief="flat",border=1,foreground="white",
        font=("Comic Sans MS", 12, "bold"))
        IngresarDatosyy.place(x=180, y=250)

        
     
   
    

##*************************************************************************************************##

    def ConceptoPanda():
        v_panda = Tk.Toplevel()
        v_panda.title("Libreria Seaborn")
        v_panda.geometry("550x540")
        v_panda.geometry("+380+98")
        v_panda.configure()
        mensaje="La Libreria de Panda"
        labelMensaje=Tk.Label(v_panda,text=mensaje,justify=Tk.CENTER,font=32,fg="red").pack()
        mensaje1="""            Pandas es una librería de Python especializada en el manejo y análisis de estructuras de datos.
            Las principales características de esta librería son:

            1.-Define nuevas estructuras de datos basadas en los arrays de la librería NumPy
               pero con nuevas funcionalidades.
            
            2.-Permite leer y escribir fácilmente ficheros en formato CSV, Excel y bases de datos SQL.

            3.-Permite acceder a los datos mediante índices o nombres para filas y columnas.

            4.-Ofrece métodos para reordenar, dividir y combinar conjuntos de datos.

            5.-Permite trabajar con series temporales.
            
                   
          
        """
        labelMensaje1=Tk.Label(v_panda,text=mensaje1,justify=Tk.LEFT,fg="blue").pack()
    
        mensaje2=" Tipos de datos de Pandas"
        labelMensaje2=Tk.Label(v_panda,text=mensaje2,fg="red",font=1).place(x=20,y=230)
    
        mensaje3=""" 
            Pandas dispone de tres estructuras de datos diferentes:

                1.-Series: Estructura de una dimensión.

                2.-DataFrame: Estructura de dos dimensiones (tablas).

                3.-Panel: Estructura de tres dimensiones (cubos).

            Estas estructuras se construyen a partir de arrays de la librería NumPy, 
            añadiendo nuevas funcionalidades.
              
                   
        """
        labelMensaje3=Tk.Label(v_panda,text=mensaje3,justify=Tk.LEFT,fg="blue").place(x=20,y=260)

    def SalirPanda():
        Ventana.withdraw()
        Ventana.deiconify()

    def SalirPrincipal():
        Ventana.destroy()
 
   
#####################################################################################################
    Panda=Menu(menu, tearoff=0)
    Panda.add_command(label="Concepto",command=ConceptoPanda)
    Panda.add_command(label="Ejemplo",command=G_Panda)
    Panda.add_command(label="Regresar",command=SalirPanda)
#####################################################################################################
    Salir=Menu(menu, tearoff=0)
    Salir.add_command(label="Salir",command=SalirPrincipal)
    

    
#####################################################################################################

    menu.add_cascade(label='Libreria Matplot',menu=Matplot)
    menu.add_cascade(label='Libreria Seaborn',menu=Seaborn)
    menu.add_cascade(label='Libreria Panda',menu=Panda)
    menu.add_cascade(label='Salir',menu=Salir)

    

    Ventana.mainloop()
    #Llmar una imagen#
    '''
    def imagen():
    Ventana1=Tk.Tk
    Ventana1.title("Ventana2")
    Ventana1.geometry("1024x672")
    Ventana1.mainloop()
    
    img=Image.open('Matplotlib1.png')
    new_img=img.resize((600,400))
    render= ImageTk.PhotoImage(new_img)
    Img1=Label(Ventana,image=render)
    Img1.image=render
    Img1.place(x=10,y=30)'''
   

def SalirLogin():
    ventanaLogin.destroy()


# Botones
boton = tk.Button(ventanaLogin, text="Entrar",command=Ingresar, 
cursor="hand2", bg_="#005588", width=12,height=1, relief="flat",border=0,foreground="white",
font=("Comic Sans MS", 12, "bold"))
boton.place(x=50, y=220)

boton1 = tk.Button(ventanaLogin, text="Salir",command=SalirLogin,foreground="white",
cursor="hand2", bg_="#005588", width=12,height=1, relief="flat",border=0, 
font=("Comic Sans MS", 12, "bold"))
boton1.place(x=140, y=220)

ventanaLogin.mainloop()
