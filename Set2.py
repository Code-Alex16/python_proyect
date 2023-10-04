# Set o conjuntos { agregar datos y eliminar datos}

#podemos agregar datos mediante add o update 
setNumbers = {1, 5, 7, 9, 3}
print(setNumbers)

setNumbers.add(16) #out {16,1,5,....}
print("dato agregado: ",setNumbers)

#Para agregar otros tipos de elementos como otro conjunto o cualquier otra coleccion se usa update
setNumbersDecimal = {1.25,2.25,3.25}
list = [3,6,25]
setNumbers.update(setNumbersDecimal)
print("datos agregados de otro set: ",setNumbers)
setNumbers.update(list)
print("datos agregados de otro tipo de coleccion [lista en este caso]",setNumbers)


# Eliminar datos de un set
'''existen diversos metodos para eliminar un dato en un set como por ejemplo: '''
setNumbers.remove(3)
print("usando remove para eliminar el item 3: ",setNumbers)

setNumbers.discard(1.25)
print("Eliminando un elemento con el metodo discard [1.25 item eliminado] ",setNumbers)

'''Existen otras maneras como el metodo pop sin embargo este eliminara cualquier elemento al azar
el metodo clear el cual deja vacia un set, y por ultimo el del el cual elimina un set completamente'''
print("usando pop en sets: ",setNumbers.pop())

print("Limpiando un set con clear: ",setNumbers.clear())

try:
    del setNumbers
    print(setNumbers)
except:
    print("usando del en un set, aqui saltaria un error si se imprimiera o se llamara")
