''' Las tuplas son un tipo de colecciones estas a diferencia de las listas y otras colecciones es
inmutable osea no se pueden modificar se declaran con parentesis y se autoseparan con comas'''

tupla = 1,2,5,5

tupla2 = ("manzana",2.56,"pera",8)

#out <'class' tuple> y se mostraran las tuplas
print("tupla 1: ",tupla," ",type(tupla)," tupla 2: ",tupla2," ",type(tupla2))     

# Metodos con tuplas
# Nos podemos mover entre los elemento mediante indices
print("Primer elemento de la tupla: ",tupla[0])
print("Elementos despues del primero: ",tupla[1:])
print("Elementos anteriores del indice 3: ",tupla[:3])

# Asi como en las listas las tuplas nos permiten comprobar si un elemento existe o no
print("BUSQUEDA DE ELEMENTO:",end="\n")
elemento = "manzana"
if elemento in tupla2:
    print(f"el elemento {elemento} si se encuentra dentro de la tupla")

# Update en tuplas: 
# Al ser un elemento inmutable para poder añadir o eliminar elementos podemos hacerlo asi

def addElemento(tupla):
    lista = list(tupla)
    lista.append(85)
    return tuple(lista)

def deleteElemento(elemento,tupla):
    lista = list(tupla)
    if elemento in lista:
        lista.remove(elemento)
        return tuple(lista)
    else:
        return "error elemento no encontrado"

print("Añadiendo nuevo elemento a tupla: ",addElemento(tupla))
print("Eliminando elemento: ",deleteElemento( 85,tupla))



