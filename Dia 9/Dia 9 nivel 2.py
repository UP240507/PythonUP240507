#Ejercicios Nivel 2:
#Write a code which gives grade to students according to theirs scores:
print("Ejercicio 1:")
calif = int(input("Ingresa la calificacion:")) 

if calif>= 80:
    print('Tu calificacion es: A')
elif calif > 70 and calif < 79:
    print('Tu calificacion es: B')
elif calif > 60 and calif < 69:
    print('Tu calificacion es: C')
elif calif > 50 and calif < 59:
    print('Tu calificacion es: D')
else:
    print('Tu calificacion es: F')

#Ejercicio 2.
#Check if the season is Autumn, Winter, Spring or Summer. 
#If the user input is: September, October or November, the season is Autumn. December, January or February,
#the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
print("Ejercicio 2:")
mes = input('Ingresa el mes: ').capitalize()
if mes in ['Septiembre','Octubre','Noviembre']:
    print('La estacion es otoño')
elif mes in ['Diciembre','Enero','Febrero']:
    print('La estacion es invierno')
elif mes in ['Marzo','Abril','Mayo']:
    print('La estacion es primavera')

#Ejercicio 3.
#The following list contains some fruits:
frutas = ['platano', 'naranja', 'mango', 'limon']
frutas_existentes = input("Escriba la fruta que quiera: ").lower()
if frutas_existentes in frutas:
    print("La fruta que buscas ya está en la lista")
else: 
    frutas.append(frutas_existentes)
    print("La fruta se añadio a la lista: {frutas}")
    print(frutas) 