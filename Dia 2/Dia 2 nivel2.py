
print("---Ejercicios Nivel 2---")
print()

primer_nombre, apellido, pais, ciudad="Christopher","Gómez","México","Aguascalientes"
nombre_completo="Christopher Rubén Rosales Gómez"
edad=24
año=2025
es_casado=False
is_true=True
esta_la_luz_prendida=False

print()
#Checar tipo de datos de variables
print(type(primer_nombre))     
print(type(apellido))      
print(type(nombre_completo))      
print(type(pais))        
print(type(ciudad))           
print(type(edad))            
print(type(año))           
print(type(es_casado))     
print(type(is_true))        
print(type(esta_la_luz_prendida))    

#Revisar la longitud de la palabra
print()
print(len(primer_nombre))

#Comparar la longitud del nombre y apellido
print()
print(len(primer_nombre) > len(apellido))  
print(len(primer_nombre) == len(apellido))  

print()
#Declarar variables
num = 5
num2 = 4
#Operaciones matematicas
total = num + num2
resta = num - num2
mult = num * num2
division = num / num2
residuo = num2 % num
exp = num ** num2
division_entera = num // num2

print("suma: ", total)
print("resta: ", resta)
print("Multiplicación:", mult)
print("Division: ", division)
print("Residuo: ", residuo)
print("Potencia:", exp)
print("Division entera: ", division_entera)

print()
#Area del circulo con variables con valor asignado
radio = 30
pi = 3.1416

areaC = pi * radio ** 2
circunferencia = 2 * pi * radio

print("Area del circulo: ", areaC)
print("Circunferencia del circulo: ", circunferencia)

print()
#Area del circulo pidiendo valores
radio2 = float(input("Ingresa el radio del circulo: "))
areaC2 = pi * radio2 ** 2
print("El area del circulo 2 es: ", areaC2)

print()
#Pedir informacion al usuario
nombre = input("Ingresa tu nombre: ")
apellido2 = input("Ingresa tu apellido: ")
pais2 = input("Ingresa tu país: ")
edad2 = int(input("Ingresa tu edad: "))

print("Nombre: ", nombre)
print("Apellido: ", apellido2)
print("País: ", pais2)
print("Edad: ", edad2)

print()
#Mostrar palabras reservadas de Python
help('keywords')
