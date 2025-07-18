#Ejercicio 1
#Create an empty dictionary called dog
print("Ejercicio 1:")
dog_empty ={}

#Ejercicio 2
#Add name, color, breed, legs, age to the dog dictionary
print("Ejercicio 2:")
dog_empty = {"Firulais", "Café", "Chihuahua","4", "5"}
print(dog_empty)

#Ejercicio 3
#Create a student dictionary and add first_name, last_name, gender, age, 
#marital status, skills, country, city and address as keys for the dictionary
print("Ejercicio 3:")
student = {
    'first_name' : 'Christopher',
    'last_name' : 'Gómez',
    'gender' : 'Masculino',
    'age' : '24',
    'marital status': 'Soltero',
    'skills': ["Redactar"],
    'country': 'Mexico',
    'city': 'Aguascalientes',
    'address' : 'Av. Heroe de Nacozari'
    }   
print(student)  

#Ejercicio 4
#Get the length of the student dictionary  
print("Ejercicio 4:")
print("La longitud del diccionario student es:", len(student))

#Ejercicio 5
#Get the value of skills and check the data type, it should be a list
print("Ejercicio 5:")
valor_skills = student["skills"]
print(valor_skills)
print(type(valor_skills))

#Ejercicio 6
#Modify the skills values by adding one or two skills
print("Ejercicio 6:")
student['skills'].extend(["matematica", "deportes", "idiomas"])  
print(student['skills'])

#Ejercicio 7
#Get the dictionary keys as a list
print("Ejercicio 7:")
print(list(student.keys()))

#Ejercicio 8
#Get the dictionary values as a list
print("Ejercicio 8:")
print(list(student.values()))

#Ejercicio 9
#Change the dictionary to a list of tuples using items() method
print("Ejercicio 9:")
student_list = list(student.items())
print(student_list)

#Ejercicio 10
#Delete one of the items in the dictionary
print("Ejercicio 10:")
student.pop('address')
print(student)

#Ejercicio 11
#Delete one of the dictionaries
print("Ejercicio 11:")
del student
print("El diccionario student se eliminó")
