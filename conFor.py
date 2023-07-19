from tkinter import*
from tkinter import messagebox
import random
import time


raiz = Tk()
raiz.title("Juego De Parejas")
raiz.geometry("800x800")

#----------------Funcionalidad------------------------------
palabras1 = ["carro", "casa", "avion", "hospital", "arbol", "moto", "tulipan", "celular", "carro", "casa", "avion", "hospital", "arbol", "moto", "tulipan", "celular"]
palabras = random.sample(palabras1, len(palabras1))

juegoPalabras = [[], [], [], []]
botones = []


miFrame=Frame(raiz,  padx="10", pady="10")
miFrame.pack(fill="both", expand="True", anchor="center")
miFrame.config(bg="grey")

miImagen = PhotoImage(file="imgBase.png")

#-----------------archivos imagenes------------

carro = PhotoImage(file="carro.png")
casa = PhotoImage(file="casa.png")
avion = PhotoImage(file="avion.png")
hospital = PhotoImage(file="hospital.png")
arbol = PhotoImage(file="arbol.png")
moto = PhotoImage(file="moto.png")
tulipan = PhotoImage(file="tulipan.png")
celular = PhotoImage(file="celular.png")
mono_img=PhotoImage(file="mono_img.png")

Imagenes = []
Imagenes.append(carro)
Imagenes.append(casa)
Imagenes.append(avion)
Imagenes.append(hospital)
Imagenes.append(arbol)
Imagenes.append(moto)
Imagenes.append(tulipan)
Imagenes.append(celular)


#------------loop para botones----------
   

d = 0
k = 0
contador = 0
valor = str
t=0
for j in range(0,16,4):
  d += 1
  k = d-1
  for i in range(0,4):
    h = j+i
    juegoPalabras[k].append(palabras[h])
    boton=Button(miFrame, image=miImagen, width="155", height="155", command=lambda c=contador, valor = juegoPalabras[k][i]:botonPulsado(c,valor))
    boton.grid(row=[k], column=[i])
    botones.append(boton)
    
    contador += 1


print(juegoPalabras)

#----------------Pulsaciones teclado-----------

def temporizador():
  i=3
  while(i>0):
    print("este es iiii=", i)
    i-=1
    time.sleep(1)
    
def opciones(c,valor):
      if valor == "casa":
        botones[c].configure(image=casa)
        return valor
      elif valor == "carro":
        botones[c].configure(image=carro)
        return valor
      elif valor == "avion":
        botones[c].configure(image=avion)
        return valor
      elif valor == "moto":
        botones[c].configure(image=moto)
        return valor
      elif valor == "tulipan":
        botones[c].configure(image=tulipan)
        return valor
      elif valor == "hospital":
        botones[c].configure(image=hospital)
        return valor
      elif valor == "arbol":
        botones[c].configure(image=arbol)
        return valor
      elif valor == "celular":
        botones[c].configure(image=celular)
        return valor
      else:
        print("no se pudo")

        
conter = 0
lista1 = []
final = []
listaBotones = []
def botonPulsado(c,valor):
  global conter
  conter+=1
  print("conter = ", conter)
  numero = c
  numero2 = valor    
  value = opciones(numero,numero2)
  
  if conter==1:
    lista1.append(value)
    listaBotones.append(numero)

  elif conter==2:
    lista1.append(value)
    listaBotones.append(numero)
  print(lista1)
  print(listaBotones)
  if conter==3:
    if len(final)!=8:
      listaBotones.append(numero)
      botones[listaBotones[2]].configure(image=miImagen)
      if lista1[0] == lista1[1]:
        print("iguales")
        conter = 0
        lista1.clear()
        listaBotones.clear()
        final.append(1)
        print("final ", final)
        if len(final)==8:
          print("Ganaste")
          messagebox.showinfo("Ganaste|!")
      else:   
        print("no son iguales")
        botones[listaBotones[0]].configure(image=miImagen)
        botones[listaBotones[1]].configure(image=miImagen)
        conter = 0
        lista1.clear()
        listaBotones.clear()
  
  


      



raiz.mainloop()





  
