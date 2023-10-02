# Mostrar el producto escalar de dos vectores y modificar los valores si es necesario
def menu2():
    return "1.- Vector 1 \n2.- Vector 2"

def productoEscalar(v1,v2):
    producto = 0
    for i in range(len(v1)):
        producto += v1[i]*v2[i]
    return f"El producto escalar de {v1},{v2} es: {producto}"

def ModificarVector1(v1):
    elemento_a_Modificar = int(input(f" Ingrese el elemento que desea reemplazar: {v1}"))
    v1 = list(v1)
    if elemento_a_Modificar in v1:
        for i in range(len(v1)):
            if v1[i] == elemento_a_Modificar:
                v1[i] = int(input("Ingrese el nuevo elemento: "))
    print(v1)
    return tuple(v1)


def ModificarVector2(v2):
    elemento_a_Modificar = int(input(f" Ingrese el elemento que desea reemplazar: {v2}"))
    v2 = list(v2)
    if elemento_a_Modificar in v2:
        for i in range(len(v2)):
            if v2[i] == elemento_a_Modificar:
                v2[i] = int(input("Ingrese el nuevo elemento: "))
    print(v2)
    return tuple(v2)


def Modificacion(v1,v2):
    print(menu2())
    valor = int(input("Ingrese a que vectro va a modificar: "))
    if(valor == 1):
        productoEscalar(ModificarVector1(v1),v2)
    elif(valor == 2):
        productoEscalar(v1,ModificarVector2(v2))
    else:
        print("Opcion invalida vuelva a intentar")


def main():
    vector1 = (1,2,3)
    vector2 = (-1,0,2)
    print("Menu",end="\n\n")
    print(f"1.- Mostrar el producto escalar de los vectores {vector1},{vector2}")
    print(f"2.- Modificar el valor de un vector y mostrar el producto escalar")
    print("3.- Salir")

    match int(input("Elija una opcion: ")):
        case 1: 
            print(productoEscalar(vector1,vector2)) 
            return True
        case 2: 
            print(Modificacion(vector1,vector2))
            return True 
        case 3: 
            return False

if __name__ == '__main__':
    value = True
    while value:
        value = main()