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