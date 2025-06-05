import math

print (3+4)
print (3-4)
print (3*4) 
print (3/4)
print (3%4)
print (3**4)
print (3//4)
print ('--- Ejercicio 2 ---')
print ('Christopher Rubén Rosales Gómez')
print ("Diana, Kevin, Rubén, Jacky")
print ("Aguascalientes,Mexico")
print ("Estoy disfrutando de 30 de días de python")
print ('--- Ejercicio 3 ---')
print (type(10))
print (type(9.8))
print (type(4-4j))
print (type(['Asabeneh','Python','Finland']))
print (type("Christopher Rubén Rosales Gómez"))
print (type("Diana, Kevin, Rubén, Jacky"))
print (type("Mexico"))

print("--- Ejercicio 3.3 ---")
print ('numero entero: ', 10)
print ('numero flotante: ', 10.3)
print ('numero complejo: ', 10+11j)
print ("cadena de caracteres: ", 'Hola mundo')
print ("booleano = ", True)
print ('ejemplo de lista: ', [10,20,"Mexico"])
print ('ejemplo de tupla: ', (10,30, "Hola"))
print ('ejemplo de un set', {10,10,20,30,40})
print ('ejemplo de un diccionario: ',{"nombre": "Christopher", "edad": 24})

print ("---Ejercicio 3.4---")

x1,y1= 2,3
x2,y2 = 10,8

distancia=math.sqrt((x2-x1)**2+(y2-y1)**2)
print ('La distancia euclidiana es: ', distancia)