#Busquea de un elemento dentro de una lista simple

def BuscarElemento(element,datos):
    if element not in datos:
        return False
    return True

def main():
    list = [x for x in range(1,20)]
    try:
        User = input("Indique el elemento a buscar en la lista: ")
        if not(BuscarElemento(int(User),list)):
            return (f"El elemento {User} no esta en la lista {list}")
        
        return (f"El elemento {User} si se encuentra en la lista de datos {list}")
    except:
        return (f"Error dato ingresado es invalido {User}")


if __name__ == '__main__':
    print(main())