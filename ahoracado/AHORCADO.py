
from Tkinter import *
import sys
import random
import os
from functools import partial as pto
from Tkinter import Tk, Button, X
from tkMessageBox import showwarning


def juego():
    obtener_palabra()
    root.mainloop()



def dibujar_muneco(opcion):
    if opcion == 1:
        #se crea la cuerda y la cabeza#
        C.create_line(320,105,320,140,width=5,fill="grey")
        C.create_line(317,141,325,141,width=3,fill="black")
        C.create_oval(305,139,335,170,width=2,fill="pink")

    if opcion == 2:
        #se crea el cuello y el cuerpo#
        C.create_line(320,174,320,170,width=10,fill="pink")
        C.create_line(320,174,320,255,width=20,fill="dark blue")

    if opcion == 3:
        #se crea la pierna izquierda junto con el zapato#
        C.create_line(296,315,315,250,width=14,fill="dark blue")
        C.create_line(279,314,300,321,width=10,fill="black")
    if opcion == 4:
        #se crea la pierna derecha junto con el zapato#
        C.create_line(344,315,325,250,width=14,fill="dark blue")
        C.create_line(361,314,340,321,width=10,fill="black")
    if opcion == 5:
        #se crea el brazo izquierdo y la mano#
        C.create_line(280,235,315,176,width=12,fill="dark blue")
        C.create_line(275,242,280,234,width=12,fill="pink")

    if opcion == 6:
        #se crea el brazo derecho y la mano#
        C.create_line(360,235,325,176,width=12,fill="dark blue")
        C.create_line(364,242,359,234,width=12,fill="pink")
    if opcion == 7:
        #se crea la cruz que aparece en la cara cuando perdes#
        C.create_line(310,165,330,144,width=2,fill="red")
        C.create_line(330,165,310,144,width=2,fill="red")


def obtener_palabra():#funcion para obtener una palabra de una lista de manera aleatoria#
    global adivinar, oportunidades, fin_juego, numerradas, palabra, digitadas #todas las variables que seran necesarias se las asigna a una funcion global para no tener que estar redefiniendolas nuevamente#
    adivinar=[]
    opciones=[]
    try:            #apertura de archivo#
        archivo=open("E:\\programacion\\pro1\\obligatorio\\ahorcadoTrueMetal\\esp.txt","r")          #ruta del archivo#
    except IOError:
        print "NO SE PUDO ABRIR EL ARCHIVO. VERIFIQUE EL PATH O SI EL ARCHIVO EXISTE"           #imprimir en caso de que el archivo no existe o la ruta es incorrecta#   
        sys.exit()
    for linea in archivo:            #variable que toma el lugar de cada una de las palabras que se encuentern en el archivo#
        opciones.append (linea.strip())             #convierto todo el contenido del archivo que esta separado por un espacio en listas#
    adivinar=opciones[random.randint(0,len(opciones)-1)]#seguramente aca este el problema,dentro de las listas se le pide que elija una de manera aleatoria entre la lista numero 0 y la ultima
    archivo.close()#cerrar archivo#

    # LISTA MOSTRADA EN PANTALLA PARA LA PALABRA A ENCONTRAR
    palabra = [" "]*(len(adivinar))

    # LISTA CON LAS LETRAS ERRADAS DIGITADAS POR EL USUARIO
    digitadas = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    #VARIABLES DEL JUEGO
    oportunidades = 7
    fin_juego = 0
    # NÚMERO DE LETRAS ERRADAS DIGITADAS
    numerradas = 0

    i = 0
    while i<len(adivinar):#remplaza cada letra por "_" deacuerdo a la longitud que tiene la palabra a ser adivinada#
        palabra[i] = '_'
        i = i + 1

    # posicion para colocar las letras
    i = 0
    j = 0 
    while i<len(adivinar):
        C.create_text(50 + j, 370, text = palabra[i], font='Times 15 bold', fill='white')#aumenta 20 pixeles haciendolo como si fuera un espacio entre letras#
        j = j + 20
        i = i + 1
   
def ahorcado():
    global adivinar, letra, oportunidades,fin_juego, numerradas, palabra, digitadas
    
    i = 0
    contar_letras = 0
    while i<len(adivinar):
        if adivinar[i] == letra.get():
            palabra[i] = letra.get()
            contar_letras = 1
        i = i + 1

    if contar_letras == 0:
        oportunidades = oportunidades - 1
        digitadas[numerradas] = letra.get()
        numerradas = numerradas + 1
	    
    i = 0
    j = 0 
    while i<len(palabra):
        C.create_text(50 + j, 370, text = palabra[i], font='Times 15 bold', fill='white')
        j = j + 20
        i = i + 1

    i = 0
    j = 0 
    while i<len(digitadas):
        C.create_text(350 + j, 320, text=digitadas[i], font='Times 15 bold', fill='white')
        j = j + 20
        i = i + 1

    if numerradas == 1:#primera equivocacion ejecuta la opcion 1 en la funcion dibujar_muñeco que se encuentra arriba#
        dibujar_muneco(1)
    if numerradas == 2:#segunda     "           "     "     "  2  "   "   "           "        "   "     "        " #
        dibujar_muneco(2)
    if numerradas == 3:
        dibujar_muneco(3)#tercera   "           "     "     "  3  "   "   "           "        "   "     "        " #
    if numerradas == 4:
        dibujar_muneco(4)#cuarta    "           "     "     "  4  "   "   "           "        "   "     "        " #
    if numerradas == 5:
        dibujar_muneco(5)#quinta    "           "     "     "  5  "   "   "           "        "   "     "        " #
    if numerradas == 6:
        dibujar_muneco(6)#sexta     "           "     "     "  6  "   "   "           "        "   "     "        " #
    if numerradas == 7:
        dibujar_muneco(7)#septima   "           "     "     "  7  "   "   "           "        "   "     "        " #
        
    
    if oportunidades == 0:#verificar si perdio#
        C.create_text(400,50, text="Mala Suerte!!!", font='Times 15 bold', fill="dark red")#texto a ser imprimdo dando tanto cordenadas como fuente y color#
        C.create_text(150,230, text="MIRA LO QUE ERA", font="Times 12 bold", fill="dark red")#texto que muestra la palabra que era dando cordenadas para que aparesca el texto junto con la fuente y el color#
        i = 0
        j = 0 
        while i<len(adivinar):
            C.create_text(150 + j,270, text=adivinar[i], font="Times 15 bold", fill="white")
            j = j + 20
            i = i + 1
        showwarning('IMPORTANTE','Has perdido\n Si quieres jugar nuevamente,\n Cierre el programa y vuelva a abrirlo\n (presione SALIR)')                  
        del letra



    # VERIFICAR SI GANÓ
    i = 0
    lleno = 0
    while i < len(palabra):
        if palabra[i] != '_':
            lleno = lleno + 1
        i = i + 1
    
    if lleno == len(palabra):
        C.create_text(400,70 , text="Buenisimo, adivinaste!!!", font="Times 20 bold", fill="black")
        showwarning('IMPORTANTE','Felicidades, \nSi quieres jugar nuevamente,\n Cierre el programa y vuelva a abrirlo\n (presione SALIR)')     
        del letra        #siempre que termine el juego,(con victoria o derrota) no permite seguir jugando a menos que se reinicie

    entrada.delete(0,END)
        
def abrir():
    archivo=os.startfile('C:\Prog 1\obligatorio\\Manual de usuario.doc')
    return archivo
#abre el manual de usuario


#
# -------------------------------------------------------------------
#                                JUEGO
# -------------------------------------------------------------------

root = Tk()
#se crea tanto la ventana, como todo el "ynque" del ahorcado
C = Canvas(root, width=600, height=400, background='orange')
C.create_oval(20,200,200,20,fill="yellow")
C.create_line(45,100,330,100,width=10,fill="brown")
C.create_line(50,100,50,350,width=10,fill="brown")
C.create_line(50,150,105,100,width=10,fill="brown")
C.create_line(0,355,600,355,width=10,fill="dark green")
C.create_line(0,347,600,347,width=8,fill="green")
C.create_line(0,400,600,400,width=80,fill="brown")

# ELEMENTOS A COLOCAR EN EL CANVAS

letra = StringVar()
entrada = Entry(root, textvariable = letra)
solicitud = Label(root, text="DIGITE UNA LETRA: ")
boton = Button(root, text = " J U G A R ", command = ahorcado, width=20)
botonsalida = Button(root, text = "S A L I R", command=exit, width=20)

C.grid(row=1, column=1, columnspan=4)
solicitud.grid(row=2, column=1)
entrada.grid(row=2, column=2)
boton.grid(row=2, column=3)
botonsalida.grid(row=2, column=4)



#MENU


menu=Menu(root)
root.config(menu=menu)
hiMenu=Menu(menu)
menu.add_cascade(label="MENU",menu=hiMenu)
hiMenu.add_command(label="MANUAL", command=abrir)



hiMenu.add_separator()
hiMenu.add_command(label="exit",command=exit)




if __name__=="__main__":
    juego()
