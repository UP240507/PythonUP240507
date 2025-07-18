print ("---Ejercicio 1---")
print()
Mi_edad = 24
Mi_peso = 1.80
Complejo = 4 + 4j

print ("---Ejercicio 2---")
print()
base= float(input("Ingresa la base del triangulo: "))
altura= float(input("Ingresa la altura del triangulo: "))
area= base * altura * 0.5
print ("El area del triangulo es: ", area)

print ("---Ejercicio 3---")
print() 
a= float(input("Ingresa el lado a: "))
b= float(input("Ingresa el lado b: "))
c= float(input("Ingresa el lado c: "))
perimetro= a + b + c
print("El perimetro del triangulo es: ", perimetro)

print ("---Ejercicio 4---")
print()
ancho= float(input("Ingresa el ancho del rectangulo: "))
alto= float(input("Ingresa la altura del rectangulo: "))
areaR= ancho * alto
perimetroR = 2 * (ancho + alto)
print ("El area del rectangulo es: ", areaR)
print("El perimetro del rectangulo es: ", perimetroR)

print ("---Ejercicio 5---")
print()
radio = float(input("Ingresa el radio del circulo: "))
pi = 3.14
areaC = pi * radio ** 2
circunferencia = 2 * pi * radio
print("El area del circulo es: ", areaC)
print("La circunferencia del circulo es: ", circunferencia)

print ("---Ejercicio 6---")
print()
m = 2
interseccion_en_y = -2
interseccion_en_x = -interseccion_en_y / m
print("Pendiente:", m)
print("La interseccion_en_x es: ", interseccion_en_x)
print("La interseccion_en_y es: ", interseccion_en_y)

print ("---Ejercicio 7---")
print()
x1, y1 = 2, 2
x2, y2 = 6, 10
puntos_pendiente = (y2 - y1) / (x2 - x1)
distancia_euclidiana = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print("La pendiente entre los puntos es: ", puntos_pendiente)
print("La distancia euclidiana entre los puntos es: ", distancia_euclidiana)
print("¿Las pendientes son iguales? ", m==puntos_pendiente)

print ("---Ejercicio 8---")
print()
valores_de_x = [-2, 0, 2]
for x in valores_de_x:
    y = x**2 + 6*x + 9
    print(f"Cuando x = {x}, y = {y}")

print ("---Ejercicio 9---")
print()
print(len("python") != len("dragon"))
print('on' in 'python' and 'on' in 'dragon')

print ("---Ejercicio 10---")
print()
oracion = "I hope this course is not full of jargon."
print('jargon' in oracion)
print('on' not in 'dragon' and 'on' not in 'python')


print ("---Ejercicio 11---")
print()

longitud = len('python')
print("Float:", float(longitud))
print("String:", str(longitud))

print ("---Ejercicio 12---")
print()
num = int(input("Ingresa un numero para ver si es par: "))
if (num % 2 == 0): print("El numero es par")
else: print("No es par")

print(7 // 3 == int(2.7))
print(type('10') == type(10))
print(int(float('9.8')) == 10)

print ("---Ejercicio 13---")
print()
horas_trabajadas = float(input("Ingresa las horas trabajadas: "))
salario = float(input("Ingresa el pago por hora: "))
pagoF = horas_trabajadas * salario
print("Tu pago semanal es de: $", pagoF)

print ("---Ejercicio 14---")
print()
años_vivo = int(input("Ingresa los años que ha vivido la persona: "))
segundos_vivo = años_vivo * 365 * 24 * 60 * 60
print("La ha persona ha vivido ", segundos_vivo, " segundos ")

print ("---Ejercicio 15---")
print()
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)
#Declarar variables con diferente tipo de dato
print()
Mi_edad = 24
Mi_peso = 1.80
Complejo = 4 + 4j

#Pedir la base y la altura de un triangulo
print()
base= float(input("Ingresa la base del triangulo: "))
altura= float(input("Ingresa la altura del triangulo: "))
area= base * altura * 0.5
print ("El area del triangulo es: ", area)

#Pedir el tamaño de los lados de un triangulo
print() 
a= float(input("Ingresa el lado a: "))
b= float(input("Ingresa el lado b: "))
c= float(input("Ingresa el lado c: "))
perimetro= a + b + c
print("El perimetro del triangulo es: ", perimetro)

#Pedir el ancho y el largo de un rectangulo
print()
ancho= float(input("Ingresa el ancho del rectangulo: "))
alto= float(input("Ingresa la altura del rectangulo: "))
areaR= ancho * alto
perimetroR = 2 * (ancho + alto)
print ("El area del rectangulo es: ", areaR)
print("El perimetro del rectangulo es: ", perimetroR)

#Pedir el valor del radio del circulo
print()
radio = float(input("Ingresa el radio del circulo: "))
pi = 3.14
areaC = pi * radio ** 2
circunferencia = 2 * pi * radio
print("El area del circulo es: ", areaC)
print("La circunferencia del circulo es: ", circunferencia)

#Calcular la pendiente  e intersecciones
print()
m = 2
interseccion_en_y = -2
interseccion_en_x = -interseccion_en_y / m
print("Pendiente:", m)
print("La interseccion_en_x es: ", interseccion_en_x)
print("La interseccion_en_y es: ", interseccion_en_y)

#Encontrar la pendiente y la distancia euclidiana
print()
x1, y1 = 2, 2
x2, y2 = 6, 10
puntos_pendiente = (y2 - y1) / (x2 - x1)
distancia_euclidiana = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print("La pendiente entre los puntos es: ", puntos_pendiente)
print("La distancia euclidiana entre los puntos es: ", distancia_euclidiana)
#Comparar si las pendientes son iguales
print("¿Las pendientes son iguales? ", m==puntos_pendiente)

#Calcular el valor de y
print()
valores_de_x = [-2, 0, 2]
for x in valores_de_x:
    y = x**2 + 6*x + 9
    print(f"Cuando x = {x}, y = {y}")

#Encontrar la longitud de las palabras y comparar si son diferentes
#Ver si "on" está dentro de alguna de las palabras
print()
print(len("python") != len("dragon"))
print('on' in 'python' and 'on' in 'dragon')

#Revisar si cierta palabra está en la oracion
print()
oracion = "I hope this course is not full of jargon."
print('jargon' in oracion)

#Ver si "on" no está dentro de alguna de las palabras
print('on' not in 'dragon' and 'on' not in 'python')


#Encontrar la longitud de la palabra y
# despues convertirlo en flotante y luego en string
print()

longitud = len('python')
print("Float:", float(longitud))
print("String:", str(longitud))

#Ver si un numero es par
print()
num = int(input("Ingresa un numero para ver si es par: "))
if (num % 2 == 0): print("El numero es par")
else: print("No es par")

#Ver si la division entera es igual a la conversion del valor 2.7
print(7 // 3 == int(2.7))
#Comparar si el tipo de dato es igual
print(type('10') == type(10))
#Comparar si son iguales 
print(int(float('9.8')) == 10)

#Calcular el sueldo de un chambeador
print()
horas_trabajadas = float(input("Ingresa las horas trabajadas: "))
salario = float(input("Ingresa el pago por hora: "))
pagoF = horas_trabajadas * salario
print("Tu pago semanal es de: $", pagoF)

#Convertir edad a segundos
print()
años_vivo = int(input("Ingresa los años que ha vivido la persona: "))
segundos_vivo = años_vivo * 365 * 24 * 60 * 60
print("La ha persona ha vivido ", segundos_vivo, " segundos ")

#Generar una tablas
print()
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)