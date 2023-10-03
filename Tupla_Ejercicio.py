# Mostrar el producto escalar de dos vectores y modificar los valores si es necesario
def menu2():
    return "1.- Vector 1 \n2.- Vector 2"

def productoEscalar(v1,v2):
    producto = 0
    for i in range(len(v1)):
        producto += v1[i]*v2[i]
    return f"El producto escalar de {v1},{v2} es: {producto}"

def ModificarVector1(vector1):
    elemento_a_Modificar = int(input(f"Ingrese el elemento que desea reemplazar {vector1}: "))
    vector1 = list(vector1)
    if elemento_a_Modificar in vector1:
        vector1[vector1.index(elemento_a_Modificar)] = int(input("Ingrese el nuevo elemento: "))
    return tuple(vector1)

def ModificarVector2(vector2):
    elemento_a_Modificar = int(input(f" Ingrese el elemento que desea reemplazar {vector2}: "))
    vector2 = list(vector2)
    if elemento_a_Modificar in vector2:
        vector2[vector2.index(elemento_a_Modificar)] = int(input("Ingrese el nuevo elemento: "))
    return tuple(vector2)

def Modificacion(v1,v2):
    print(menu2())
    valor = int(input("Ingrese a qué vector va a modificar: "))
    if valor == 1:
        newVector1 = ModificarVector1(v1)
        print(productoEscalar(newVector1, v2))
    elif valor == 2:
        newVector2 = ModificarVector2(v2)
        print(productoEscalar(v1, newVector2))
    else:
        print("Opción inválida. Vuelva a intentar.")

def main():
    vector1 = (1, 2, 3)
    vector2 = (-1, 0, 2)
    print("Menu", end="\n\n")
    print(f"1.- Mostrar el producto escalar de los vectores {vector1},{vector2}")
    print(f"2.- Modificar el valor de un vector y mostrar el producto escalar")
    print("3.- Salir")

    opcion = int(input("Elija una opción: "))
    if opcion == 1:
        print(productoEscalar(vector1, vector2))
    elif opcion == 2:
        Modificacion(vector1, vector2)
    elif opcion == 3:
        return False
    else:
        print("Opción inválida. Vuelva a intentar.")
    
    return True

if __name__ == '__main__':
    value = True
    while value:
        value = main()
