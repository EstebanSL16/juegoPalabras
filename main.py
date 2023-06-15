import random

palabras1 = ["oceano", "bosque", "playa", "páramo", "selva", "golfo", "desierto", "isla", "oceano", "bosque", "playa", "páramo", "selva", "golfo", "desierto", "isla"]

palabras = random.sample(palabras1, len(palabras1))

print("empieza", palabras, "Termina")

juegoPalabras = [[], [], [], []]

d = 0
k = 0
for j in range(0,16,4):
  print("j = ", j)
  d += 1
  k = d-1
  print("k = ",k)
  for i in range(0,4):
    h = j+i
    juegoPalabras[k].append(palabras[h])
    print("r = ", i, " h = ", h, palabras[h])
      
print(juegoPalabras) 

