from Tkinter import *
import random
r=Tk()
## se crea una clase que se encargue de tomar variables como objetos para que estos objetos puedan ser llamados por cualquier funcion simplemente aclarando que la variable pertenece a la clase
class variables:
    x=random.randint(200,650)
    y=random.randint(40,150)
    nombre=raw_input('ingrese su nombre: ')
    gas=100.0
    x1=0.01
    g=0.000163
    y2=0.00001
    prpl=0.0
    eff_grv=0.0
    spd=0.0
    arriba=False
    abajo=False
    izquierda=False
    derecha=False
    
vr=variables()
##funcion principal que permite mostrar todo en pantalla
def inicio():
    c.pack()
    c.update()
    r.mainloop()
    
def salir():
    exit()
def reiniciar():
    vr.x=random.randint(200,650)
    vr.y=random.randint(40,150)
    vr.gas=100.0
    vr.x1=0.01
    vr.g=0.000163
    vr.y2=0.0001
    vr.prpl=0.0
    vr.eff_grv=0.0
    vr.spd=0.0
    vr.arriba=False
    vr.abajo=False
    vr.izquierda=False
    vr.derecha=False
    c.delete('nave','ganador','perdedor','crater','nombre','altura')
    c.create_image(vr.x,vr.y,image=nave,tag='nave')
    c.update()
    

def pausa(event):
    inicio()
##funcion diseñada para implementar gravedad
def gravedad(event):
    vr.arriba=False
    vr.abajo=True
    vr.izquierda=False
    vr.derecha=False
    t=0.0
    vr.prpl=0.0
    vr.eff_grv=0.0
## mientras la condicion sea verdadera, se ira sumando progresivamete a 0 el valor de 0.16 tantas veces se actualize el loop    
    while vr.abajo==True:
        vr.y=vr.y+vr.eff_grv
        vr.spd+=vr.g*t-vr.prpl
        vr.eff_grv+=vr.g
        t+=1.0
        c.move('nave',0.0,vr.eff_grv)
        c.delete('velocidad','altura')
        c.create_text(720,100,text=('altura: ',int(520-vr.y)),font='times 15 bold',fill='white',tag='altura')
        c.create_text(750,50,text=(int(vr.spd),'M/s'),font='times 15 bold',fill='white',tag='velocidad')
        c.update()
        if vr.y>=520.0:
            vr.abajo=False
            c.move('nave',0.0,0.0)
            c.update()
        if vr.y>=520.0 and vr.spd<=20.0:
            c.create_text(380,280,text='G A N A S T E ! ! !',font='Times 30 bold',fill='White',tag='ganador')
            c.update()
        if vr.y>=520.0 and vr.spd>=20.0:
            c.delete('nave')
            c.create_oval((vr.x-vr.spd),(vr.y-vr.spd),(vr.x+vr.spd),(vr.y+vr.spd),fill='Black',tag='crater')
            c.create_text(vr.x,vr.y,text=vr.nombre,font='times 15 bold',fill='white',tag='nombre')
            c.create_text(350,250,text='H O U S T O N ,   W E   H A V E   A   P R O B L E M ! ',font='arial 15 bold',fill='white',tag='perdedor')
            c.update()
def mover_arriba(event):
      vr.abajo = True
      vr.izquierda = False
      vr.derecha = False
      t1=1.0
      while vr.abajo==True:
          vr.spd=0.0
          vr.spd+=vr.g*t1-vr.prpl
          vr.prpl=vr.prpl+vr.spd
          vr.y=vr.y-vr.prpl
          vr.gas=vr.gas-0.05
          if vr.y<=50.0:
              vr.gas=100
          if vr.gas<=0.0:
              c.destroy('nave','altura')
              c.update()  
          t1+=1.0
          c.move('nave',0.0,-vr.prpl)
          c.delete('velocidad','gasoil')
          c.create_text(50,50,text=(int(vr.gas),'%'),font='times 15 bold',fill='white',tag='gasoil')
          c.create_text(750,50,text=(int(vr.spd),'M/s'),font='times 15 bold',fill='white',tag='velocidad')
          c.update()
          
        
def mover_derecha(event):
      vr.arriba = False
      vr.abajo = False
      vr.izquierda = False
      vr.derecha = True
      vr.prpl=0.0
      vr.spd=0.0
      while vr.derecha==True:
            vr.x=vr.x+vr.x1
            vr.eff_grv=0.0
            c.move('nave',vr.x1,vr.prpl)
            c.delete('velocidad')
            c.create_text(750,50,text=(int(vr.spd),'M/s'),font='times 15 bold',fill='white',tag='velocidad')
            c.update()
def mover_izquierda(event):
      vr.arriba = False
      vr.abajo = False
      vr.izquierda = True
      vr.derecha = False
      vr.prpl=0.0
      vr.spd=0.0
      while vr.izquierda==True:
            vr.x=vr.x-vr.x1
            vr.eff_grv=0.0
            c.move('nave',-vr.x1,vr.prpl)
            c.delete('velocidad')
            c.create_text(750,50,text=(int(vr.spd),'M/s'),font='times 15 bold',fill='white',tag='velocidad')
            c.update()
##se crea una clase que a traves de un constructor, se encargue de crear botones
class Botones:
    def __init__(self,r2):
        self.boton = Frame(r2)
        self.boton.pack()
                 
        self.botonsalir = Button(self.boton)
        self.botonsalir.configure(text='S A L I R ',width=50,background='orange',command=salir)
        self.botonsalir.pack(side=RIGHT)

        self.botonreiniciar=Button(self.boton)
        self.botonreiniciar.configure(text=' R E I N I C I A R ',width=50,background='orange',command=reiniciar)
        self.botonreiniciar.pack(side=LEFT)
        
        
##se le atribuye una variable a la clase botones          
bt=Botones(r)
def key(event):
        f.focus_force()
        repr(event.keysym)
        

f=Frame(width=1,height=1)
f.bind('<Up>',mover_arriba)
f.bind('<Down>',gravedad)
f.bind('<Left>',mover_izquierda)
f.bind('<Right>',mover_derecha)
f.bind('<p>',pausa)
f.pack()
f.focus_set()


fondo=PhotoImage(file=('E:\\programacion\\pro1\\obligatorio\\alunizaje\\alunizaje\\fondo.gif'))
nave=PhotoImage(file=('E:\\programacion\\pro1\\obligatorio\\alunizaje\\alunizaje\\naveV2.gif'))
alien=PhotoImage(file=('E:\\programacion\\pro1\\obligatorio\\alunizaje\\alunizaje\\alien.gif'))
c= Canvas(r,width=800,height=600)
escenario=c.create_image(400,300,image=fondo)
velocidad=c.create_text(750,50,text=(vr.spd,'M/s'),font='times 15 bold',fill='white',tag='velocidad')
altura=c.create_text(720,100,text=('altura: ',520-vr.y),font='times 15 bold',fill='white',tag='altura')
gasoil=c.create_text(50,50,text=(vr.gas,'%'),font='times 15 bold',fill='white',tag='gasoil')
c.create_image(vr.x,vr.y,image=nave,tag='nave')
c.create_image(50,500,image=alien,tag='alien')
c.move('alien',500,0.0)
c.update()

if __name__=='__main__':
    inicio()
