import math

print("--- Escribe un ejemplo para cada tipo diferente de datos de Python---")
print ('numero entero: ', 10)
print ('numero flotante: ', 10.3)
print ('numero complejo: ', 10+11j)
print ("cadena de caracteres: ", 'Hola mundo')
print ("booleano = ", True)
print ('ejemplo de lista: ', [10,20,"Mexico"])
print ('ejemplo de tupla: ', (10,30, "Hola"))
print ('ejemplo de un set', {10,10,20,30,40})
print ('ejemplo de un diccionario: ',{"nombre": "Christopher", "edad": 24})

print ("---Encuentra la distancia euclidiana---")

x1,y1= 2,3
x2,y2 = 10,8

distancia=math.sqrt((x2-x1)**2+(y2-y1)**2)
print ('La distancia euclidiana es: ', distancia)