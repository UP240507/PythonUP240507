#Ejercicio 1
#Use for loop to iterate from 0 to 100 and print the sum of all numbers.
#The sum of all numbers is 5050.
print("Ejercicio 1:")
num = 0
for i in range(101):
    num = num + i 
    print(num)
print("------")
#Ejercicio 2
#Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
#The sum of all evens is 2550. And the sum of all odds is 2500.
print("Ejercicio 2:")
suma_pares = 0
suma_impares = 0

for num in range(0, 101):  
    if num % 2 == 0: 
        suma_pares += num
    else: 
        suma_impares += num

print("La suma par es: ", suma_pares)
print("La suma impar es:", suma_impares)