# Aunque son inmutables podemos unirlas entre si de la sigueinte manera
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#Metodos para las tuplas
count = f"existen esta cantida de elementos 2 en la tupla {tuple3.count(2)}"
index = f"el elemento 1 se encuentra en la posicion {tuple3.index(1)}"
print("Metodo count cuenta las orcurrencias del elemento en la tupla: ",count)
print("Metodo index indica donde esta el elemento que se busca: ", index)