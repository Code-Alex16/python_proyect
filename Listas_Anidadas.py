#Listas Anidadas
#Busqueda de un dato dentro de una matriz
def BusquedaMatriz(matriz,user):
    for filas in matriz:
        in1 = matriz.index(filas)
        if user in filas:
            in2 = filas.index(user)
            return (f"El elemento se encuentra dentro de la matriz en la posicion {in1},{in2}")
        
    return (f"El elemento '{user}' no se encuentra dentro de la matriz")
        

def main():
    #Declaracion de los elementos de la lista
    fila_1=[1,2,3]
    fila_2=[4,5,6]
    fila_3=[7,8,9]
    matriz=[fila_1,fila_2,fila_3]

    try:
        user = input("Ingrese el elemento que desea buscar: ")
        print(BusquedaMatriz(matriz,int(user)))
    except:
        print("Error en los datos de ingreso")


if __name__ == '__main__':
    main()