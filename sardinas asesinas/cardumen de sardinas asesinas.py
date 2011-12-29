from visual import *
from visual.controls import *
import random
import math
#Tamaño de la pantalla
scene.width=600
scene.height=600


#propiedades
lados= 100
# radio de los cardumenes represantados por una esfera y valor de z en equivalencia con los cardumenes
fondo=-60
grosor= 1
#para formar un cuadrado
lado2=lados*2 - grosor
lado3=lados*2 + grosor

#diseño del area grafica
tierra1=box(pos=(0,0,-45),size=(400,350,120),material=materials.marble,color=(0.57,0.32,0.06))
tierra2=box(pos=(-150,0,65),size=(100,350,100),material=materials.marble,color=(0.00,0.42,0.00))
visual.label(pos=(0,180,100),color=color.white,text='CARDUMEN DE SARDINAS ASESINAS')
tierra3=box(pos=(150,0,65),size=(100,350,100),material=materials.marble,color=(0.00,0.42,0.00))
tierra4=box(pos=(0,138,65),size=(200,74,100),material=materials.marble,color=(0.00,0.42,0.00))
tierra5=box(pos=(0,-138,65),size=(200,74,100),material=materials.marble,color=(0.00,0.42,0.00))
pared_agua1=box(pos=(lados,0,0),size=(grosor,lado2,lado3), material=materials.blazed,color=(0.17,0.40,1.00))
pared_agua2=box(pos=(-lados,0,0),size=(grosor,lado2,lado3), material=materials.blazed,color=(0.17,0.40,1.00))
pared_agua3=box(pos=(0,-lados,0),size=(lado3,grosor,lado3),material=materials.blazed,color=(0.17,0.40,1.00))
pared_agua4=box(pos=(0,lados,0),size=(lado3,grosor,lado3),material=materials.blazed,color=(0.17,0.40,1.00))
fondo=box(pos=(0,0,-fondo),size=(lado2,lado2,grosor),material=materials.blazed,color=(0.17,0.40,1.00))
#tapa=box(pos=(0,0,lados),size=(lado2,lado2,grosor),material=materials.blazed,color=(0.17,0.40,1.00))
posicion_aleatoria=((random.randint(-95,95),random.randint(-95,95),random.randint(60,95)))
sardinas_locas=sphere(pos=(posicion_aleatoria),material=materials.glass,color=color.cyan, radius = 4)
#vector de movimiento para que las sardinas se actualizen en base a numeros esnteros
sardinas_locas.p = vector(-1,1,1)
#funcion para determinar la posicion de la sonda

def posicion():
    sardinas_locas.p=vector(0,0,0)
    eje_x=input('ingrese el valor para x: ')
    eje_y=input('ingrese el valor para y: ')
    posicion_sonda=sphere(pos=(eje_x,eje_y,100),radius=5,material=materials.shiny,color=color.red)
    d_x=(sardinas_locas.x-posicion_sonda.x)**2
    d_y=(sardinas_locas.y-posicion_sonda.y)**2
    d_z=(sardinas_locas.z-posicion_sonda.z)**2
    distancia=int(math.sqrt(d_x+d_y+d_z))
    vector_error=vector(random.randint(-1,1),random.randint(-1,1),random.randint(-1,1))
    print distancia ,'kilometros de distancia','(cordenadas aproximadas= ',sardinas_locas.pos+vector_error,')'    
#funcion para determinar la posicion que se debera lanzar el misil
def misil():
#al momento de ejecutarse esta funcion las sardinas dejan de moverse
    sardinas_locas.p=vector(0,0,0)
    cordenada_x=input('ingrese las cordenadas para x: ')
    cordenada_y=input('ingrese las cordenadas para y: ')
    cordenada_z=input('ingrese las cordenadas para z: ')
    if sardinas_locas.x==cordenada_x and sardinas_locas.y==cordenada_y and sardinas_locas.z==cordenada_z:
        print 'LES PEGASTE!!!! HAS SALVADO A LA TIERRA SUPERMAN!!!'
        
    else:
#al momento de terminar la ejecucion de la funcion las sardinas vuelven a su movimiento
        sardinas_locas.p=vector(-1,1,1)
        print 'le erraste...pero MAL!!!!... trata de embocarle a las sardinas la proxima...!!!'
#funcion para permitir que los cardumenes vuelvan a moverse'salir'
def saltar_turno():
    if sardinas_locas.p==vector(0,0,0):
        sardinas_locas.p=vector(-1,1,1)
    else:
        pass
def salir():
    exit()
#funcion extra para los mas impacientes, que se le asigna al boton 'trampa' que en pantalla se representa como '...'
def sos_re_tramposo():
    print sardinas_locas.pos

#creacion de la pantalla con los botones correspondientes para ser utilizados por las funciones
sonda=button(pos=(-50,45),width=100,height=100,text='tirar sonda',font='arial 15 bold',action=posicion,color=color.orange)
misil=button(pos=(50,45),width=100,height=100,text='tirar misil',font='arial 15 bold',action=misil,color=color.orange)
salir=button(pos=(50,-80),width=100,height=30,text='salir',font='times 15',action=salir,color=color.white)
trampa=button(pos=(89,-55),width=20,height=20,text='...',font='arial 5 bold',action=sos_re_tramposo,color=color.red)
saltar_turno=button(pos=(0,-30),width=70,height=40,text='nuevo turno',action=saltar_turno)
#comienzo del loop infinito
while True:
#velocidad que debera realizar los calculos python
    rate(10)
#se limitan las posiciones de las sardinas para que no se salgan del poso mediante inversion de signo de la variable de movimiento que es'sardinas_locas.p=vector(1,1,1)'
    sardinas_locas.pos = sardinas_locas.pos+sardinas_locas.p
    
    if not(lados-sardinas_locas.radius > sardinas_locas.x > -lados+sardinas_locas.radius):
      sardinas_locas.p.x = -sardinas_locas.p.x
    if not(lados-sardinas_locas.radius > sardinas_locas.y > -lados+sardinas_locas.radius):
      sardinas_locas.p.y = -sardinas_locas.p.y
    if not(lados-sardinas_locas.radius > sardinas_locas.z >lados-40+sardinas_locas.radius):
      sardinas_locas.p.z = -sardinas_locas.p.z


