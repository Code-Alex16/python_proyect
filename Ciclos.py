# Ciclos Repetitivos y entrada de datos

'''En Python existen los ciclos los cuales nos ayudan a repetir una tarea hasta que tenga que terminar ademas
podemos ingresar datos para que el usuario pueda realizar alguna actividad en especifico

En el sigueinte programa revisaremos una cantidad limitada de datos los cuales especificara el usuario para comprobar
si son pares o no los datos'''

# Comprobacion de datos
def comprobaciones(numero):
	return numero.isnumeric()


# Datos de ejecucion del programa
def loop(numero_usuario):
	#ciclo que se detiene automaticamente indicamso de donde comienza y donde termina
	for i in range (1,int(numero_usuario)):
		if (i % 2 == 0):
			print(f"El número {i} es par")
		else:
			print(f"El número {i} es impar")


#Funcion principal de ejecucion
def main():
	#pedimos al usuario que ingrese un dato con input y especificamos que tipo de dato es
	numero_usuario = input("Ingrese un numero: ")

	#mediante un bloque de control verificamos si es o no un dato numerico
	try:
		if(comprobaciones(numero_usuario)):
			loop(numero_usuario)
		else:
			print("El valor ingresado no es un número válido.")
	except ValueError as e:
		print("Error en el ingreso:", e)


#Cuerpo principal del programa
if __name__ == '__main__':
	main()