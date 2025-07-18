#Ejercicio 1
#Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: 
#You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
print("Ejercicio 1:")
edad = int(input("Escribe tu edad: "))
if edad >= 18:
    print("You are old enough to learn drive.")
else:
    print(f"you need {18 - edad} more years to learn to drive. ")

#Ejercicio 2.
#Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) 
# to get the age as input. 
#You can use a nested condition to print 'year' for 1 year difference in age, 
# 'years' for bigger differences, and a custom text if my_age = your_age. Output:
print("Ejercicio 2:")
mi_edad = int(input("Escribe tu edad: "))
tu_edad = int(input("Escribe tu edad: "))
print("Quien es mas grande tu o yo: ")
if mi_edad == tu_edad:
    print("Tenemos la misma edad.")
elif mi_edad < mi_edad:
    print(f"Tu eres { tu_edad - mi_edad} años mayor que yo.")
else:
    print(f"Yo soy {tu_edad - mi_edad} año(s) mayor que tu. ")

#Ejercicio 3.
#Get two numbers from the user using input prompt.
#If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
print("Ejercicio 3:")
num1 =int(input("Escribe el primer numero: ")) 
num2 = int(input("Escribe el segundo numero: "))
if num1 == num2:
    print("Los numeros son iguales.")
elif num1 < num2:
    print(f"El numero {num1} es menor que el {num2}.")
else: 
    print(f"El numero {num1} es mayor que el {num2}.")