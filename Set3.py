# Metodos Exclusivos de los sets

# Metodo union en set consisten en crear un nuevo set uniendo dos o mas de estos
set1 = {1,2,3,4,5}
set2 = {6,7,5,9,4}
set3 = set1.union(set2)
print(set1)
print(set2)
print("Union de los conjuntos - set: ",set3) # se auto eliminan elementos iguales

# Metodo intersection devulve un nuevo conjunto con los items solo iguales
set4 = set1.intersection(set2)
print("Interseccion de conjuntos - set: ",set4)

# Meetodo intersction_update mantendra los elementos que se encuentra ne los mismos cojuntos sin crear uno nuevo
set1.intersection_update(set2)
print("items que se encuentran en ambos set [uso de intesection_update]: ",set1)

# Metodo symmetric_difference_update() mantiene los item que no se estan presentes en ambos set
set1.symmetric_difference_update(set2)
set2.symmetric_difference_update(set1)
print("Elementos unicos del primer set: ",set1,"\n","elementos que no se repiten en el segundo set",set2)

# Metodo symmetric_difference() devuelve un nuevo set con los elementos que No estan presente en ambos set
Unique = set1.symmetric_difference(set2)
print("Todos los elementos unicos de ambos set [symmetric_difference]: ",Unique)