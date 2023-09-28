#Condicionales en python

'''consiste en crear bloques de codigo que se ejecutan si lo propuesto es verdadero dan valores true o false

Encontramos los if es la primera condicion podemos usar diferentes operadores de comparacion o funciones que retornen
los valores de verdad 
los elif es una segunda condicion dentro de la estructura y por ultimo esta el else el cual se ejecuta si no se cumplio
la condicion'''

def main():
	edad = 18
	if(edad == 18):
		print("edad es igual a 18")
	elif(edad > 18):
		print("edad es mayor a 18")
	else:
		print("edad es menor de 18")


#Existen otras formas de usar las condicionales negando o retornando los valores de comparacion
def forma2(edad):
	#negamos el resultado de la comparacion retorna false con el operador not lo volvemos true y se ejecuta
	#esto con la finalidad de tratar de una manera mas ordenada los datos
	if not(edad == 18):
		print("la edad no es igual a 18")

def forma3(edad):
	#podemos tambien retornan de manera mas eficiente la comparacion directa esta devolvera true o false
	return edad == 30



if __name__ == '__main__':
	main()
	forma2(20)
	print(forma3(30))

