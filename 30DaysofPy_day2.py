#Día 2: Días de programación Python#
print("---Ejercicio 1---")
primer_nombre, apellido, pais, ciudad="Christopher","Gómez","México","Aguascalientes"
nombre_completo="Christopher Rubén Rosales Gómez"
edad=24
año=2025
es_casado=False
is_true=True
esta_la_luz_prendida=False

print("---Ejercicio 2---")

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

print("---Ejercicio 3---")
print(len(primer_nombre))

print("---Ejercicio 4---")
print(len(primer_nombre) > len(apellido))  
print(len(primer_nombre) == len(apellido))  

print("---Ejercicio 5---")
num = 5
num2 = 4

suma = num + num2
resta = num - num2
mult = num * num2
division = num / num2
residuo = num2 % num
exp = num ** num2
division_entera = num // num2

print("suma: ", suma)
print("resta: ", resta)
print("Multiplicación:", mult)
print("Division: ", division)
print("Residuo: ", residuo)
print("Potencia:", exp)
print("Division entera: ", division_entera)

print("---Ejercicio 6---")
radio = 30
pi = 3.1416

areaC = pi * radio ** 2
circunferencia = 2 * pi * radio

print("Area del circulo: ", areaC)
print("Circunferencia del circulo: ", circunferencia)

print("---Ejercicio 7---")
radio2 = float(input("Ingresa el radio del circulo: "))
areaC2 = pi * radio2 ** 2
print("El area del circulo 2 es: ", areaC2)

print("---Ejercicio 8---")
nombre = input("Ingresa tu nombre: ")
apellido2 = input("Ingresa tu apellido: ")
pais2 = input("Ingresa tu país: ")
edad2 = int(input("Ingresa tu edad: "))

print("Nombre: ", nombre)
print("Apellido: ", apellido2)
print("País: ", pais2)
print("Edad: ", edad2)

print("---Ejercicio 9---")
help('keywords')


