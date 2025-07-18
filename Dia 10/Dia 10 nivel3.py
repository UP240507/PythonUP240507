#Ejercicios de Nivel 3
#Ejercicio 1
# Go to the data folder and use the countries.py file.
# Loop through the countries and extract all the countries containing the word 'land'.
print("Ejercicio 1:")
import countries as pais
paises = pais.countries
paises_con_land = []
for pais in paises:
    if 'land' in pais:
        paises_con_land.append(pais)
print(paises_con_land)
print("----------------")
print()
#Ejercicio 2
#This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
print("Ejercicio 2:")
frutas = ['banana', 'orange', 'mango', 'lemon']
for i in range(len(frutas)-1, -1, -1):
    print(frutas[i])
print("----------------")
print()
#Ejercicio 3
# Go to the data folder and use the countries_data.py file.
# 3.1.What are the total number of languages in the data
print("Ejercicio 3 y 3.1:")
import countries_data as cd
num_lenguaje = cd.paises
lenguajes = set()
for pais in num_lenguaje:
    for idioma in pais['languages']:
        lenguajes.add(idioma)
print("El total de idiomas es:", len(lenguajes))
print("----------------")
print()
#Ejercicio 3.2
#Find the ten most spoken languages from the data
print("Ejercicio 3.2:")
setLanguages = set()
dictLanguages = {}

for country in cd.paises:
    for language in country['languages']:
        setLanguages.add(language)

for language in setLanguages:
    dictLanguages[language] = 0

for language in dictLanguages:
    for country in cd.paises:  
        if language in country['languages']:
            dictLanguages[language] += country['population']

sortValuesLanguagesPopulation = sorted(dictLanguages.values(), reverse=True)
sortKeysLanguagesPopulation = sorted(dictLanguages, key=dictLanguages.get, reverse=True)
print('Los 10 idiomas más hablados en el mundo son: ')
for i in range(10):
    print(" El idioma es: ",  sortKeysLanguagesPopulation[i])
    print("Cantidad de personas que lo hablan: ", sortValuesLanguagesPopulation[i])

#Ejercicio 3.3
#Find the 10 most populated countries in the world
print("----------------")
print()
print("Ejercicio 3.3:")
paises = cd.paises
paises_poblacion = {}
for pais in paises:
    paises_poblacion[pais['name']] = pais['population']
paises_poblacion_ordenados = sorted(paises_poblacion.items(), key=lambda x: x[1], reverse=True)
print("Los 10 países más poblados del mundo son:")
for i in range(10):
    print(paises_poblacion_ordenados[i][0], ":", paises_poblacion_ordenados[i][1])