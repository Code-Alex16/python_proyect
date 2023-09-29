#Las Listas en ytho nos permiten trabajar con varios datos aqui estas pueden tener varios tipos
#de datos como uno solo

#Añadiendo los valores que tome x en el ciclo
Lista = [x for x in range(10)]
print(Lista)

#Añadiendo un dato
Lista.append(1)
print(Lista)

#contando la cantidad de ocurrencias del dato que pasamos
count_datos = Lista.count(1)
print(f"Existen {count_datos} cantidad de 1")

#insertando datos en una posicion determinada {posicion,dato a ingresar}
Lista.insert(1,50)
print(Lista)

#limpiando todos los datos de la lista
Lista.clear()
print(Lista)

Lista.append(1)
Lista.append(2)
Lista.append(3)

print(Lista)

#eliminando el ultimo elemento de la lista
Lista.pop()
print(Lista)

#copiando la lista
Lista_2 = Lista.copy()
print(Lista_2)

#invirtiendo la lista
Lista.reverse()
print(Lista)

#Eliminando un dato en especifico
Lista.remove(1)
print(Lista)