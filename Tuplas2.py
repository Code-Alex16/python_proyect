''' maneras de asignar elementos de una tupla'''

Fruta = ("manzana","pera","sandia","uvas")

#cada variable se autosaignara por oden los elementos
print("Asignacion por separacion de variables: var1,var2,...")
manzana, pera, sandia, uvas = Fruta
print("Tupla: ",Fruta,end="\n")
print(manzana,end="\n")
print(pera,end="\n")
print(sandia,end="\n")
print(uvas,end="\n")

# Asignacion de todos los elementos a una variable se usa un asterisco encima de la variable
print("Asginacion de varios elementos a una sola variable devuelta en forma de lista: *variable")
fruta1,fruta2, *frutasRestantes = Fruta
print(fruta1,end="\n")
print(fruta2,end="\n")
#Esta se devuleve en forma de lista
print(frutasRestantes,end="\n\n")

print("Recorrido de tuplas con ciclos: ")
for elementos in Fruta:
    print(elementos)