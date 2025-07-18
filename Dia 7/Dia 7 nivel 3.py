#Ejercicio 1
#Convert the edades to a set and compare the length of the list and the set, 
#which one is bigger?
print("Ejercicio 1:")
edadLista = [22, 19, 24, 25, 26, 24, 25, 24]
edades = set(edadLista)
print("edadLista converido en set es:", edades)
len(edadLista)
print("La longitud del set es:", len(edades))
len(edades)
print("La longitud de la lista es:", len(edadLista))
masGrande = len(edadLista) > len(edades)
print(masGrande)

#Ejercicio 2
#Explain the difference between the following data types: string, list, tuple and set
print("Ejercicio 2:")

#Ejemplo string: 
string = "Hola mundo"
print("Es una cadena de caracteres: ", string)

#Ejemplo list:
lista = ['Frutas', 'Comida', 'Numeros', 'Edades', 'Etc']
print("La lista se usa para ordenar datos que pueden ser de distintos tipos de datos: ", lista)

#Ejemplo tuple:
tuple = ('Frutas', 'Comida', 'Numeros', 'Edades', 'Animales', 'Etc')
print("La tupla es igual a una lista solo que esta no se puede modificar directamente: ", tuple)

#Ejemplo Set:
set1 = {'Frutas', 'Comida', 'Numeros', 'Edades', 'Animales', 'Etc'}
print("Un set es un conjunto de datos ordenados o sin ordenar: ", set1)

#Ejercicio 3
print("Ejercicio 3:")
oracion = "I am a teacher and I love to inspire and teach people."
palabrasUnicas = set(oracion.split())
numPalabrasUnicas = len(palabrasUnicas)
print(numPalabrasUnicas)
