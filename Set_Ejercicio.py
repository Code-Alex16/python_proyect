'''
Teniendo en cuenta el conjunto S y el conjunto T, 
sin usar el operador de intersección &, calcularemos la intersección de dichos conjuntos.

Entonces, tenemos un conjunto S, que vamos a definir como 1, 2, 3, 4; 
y un conjunto T, definido por los valores 3, 4, 5, 6.
'''

def BusquedaInterseccion(set1,set2):
    newSet = set()
    for item in set1:
        if item in set2:
            newSet.add(item)
    
    return newSet


def main():
    S = {1,2,3,4}
    T = {3,4,5,6}
    print(f"Interseccion de los conjuntos {S} y {T} es: ",BusquedaInterseccion(S,T))

if __name__ == '__main__':
    main()