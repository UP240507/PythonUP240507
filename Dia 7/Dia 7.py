#Ejercicio 1
#Find the length of the set it_companies
print("Ejercicio 1: ")
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
longitud_set = len(it_companies)
print(longitud_set)

#Ejercicio 2
#Add 'Twitter' to it_companies
print("Ejercicio 2:")
it_companies.add("Twitter")
print(it_companies)

#Ejercicio 3
#Insert multiple IT companies at once to the set it_companies
print("Ejercicio 3:")
new_companies = {'Instagram', 'Tik Tok', 'WhatsAp', 'Spotify'}
it_companies.union(new_companies)
print(it_companies)


#Ejercicio 4
#Remove one of the companies from the set it_companies
print("Ejercicio 4:")
it_companies.remove("Facebook")
print(it_companies)

#Ejercicio 5
#What is the difference between remove and discard
print("Ejercicio 5:")
#Ejemplo
it_companies.remove('Google')
print("remove: se usa cuando estas seguro de que algo si este y poder eliminarlo")

#Ejemplo:
it_companies.discard('Google')
it_companies.discard('Tiktok')
print("discard: se usa cuando no estas seguro y evitar errores")
