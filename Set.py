'''
Set o conjuntos como algunos lo llaman son tambien parte de la colecciones en python estas tienen la 
caracteristica de ser inmutables {no se pueden modificar} y desordenadas {no tiene orden definido} 
ademas de que no se puede hacer referencia a los items mediante indices o claves

Nota: Los elementos deun set - conjunto pueden en algunos casos eliminar elementos iguales {true y 1 se
consideran iguales por lo tanto quedaria true o 1} ademas puede o no ordenarse segun el tipo de item
'''

# Declaracion de un set
newSet = {"hola","mucho","gusto",1,2,3,1}

# se ordena primero los numeros despues las cadenas de caracteres
print(newSet)

#Tipos de datos que se pueden almacenar
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#Acceso a items de un set puede ser por un forloop o verificando si el item se encuentra o no
for item in set2:
    print(item, end=" ")

print("\nel elemento 1 se encuentra dentro del set2: ",1 in set2) #out true