#Ejercicio 1:
#Iterate 0 to 10 using for loop, do the same using while loop.
print("Ejercicio 1:")
#para
i = 0
while i < 10:
    i += 1
    print(i)

#Ejercicio 2
#Iterate 10 to 0 using for loop, do the same using while loop.
print("Ejercicio 2:")
while i >= 0:
    print(i)
    i -= 1

#Ejercicio 3
#Write a loop that makes seven calls to print(), so we get on the output the following triangle:
print('Ejercicio 3:')
#         
##        
###
####
#####
######
#######
for i in range(8):
    print("#"*i)

#Ejercicio 4
#Use nested loops to create the following:
print('Ejercicio 4:')
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

for i in range(8):
    for j in range(8):
        print('#', end='')
    print()

#Ejercicio 5
#Print the following pattern:
print("Ejercicio 5:")
# 0 x 0 = 0
#1 x 1 = 1
#2 x 2 = 4
#3 x 3 = 9
#4 x 4 = 16
#5 x 5 = 25
#6 x 6 = 36
#7 x 7 = 49
#8 x 8 = 64
#9 x 9 = 81
#10 x 10 = 100

for num in range(11):
    print(f'{num} x {num} = {num * num}')


#Ejercicio 6
#Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
print("Ejercicio 6:")
lengProgra  =['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for lenguajes in lengProgra:
    print( lenguajes)


#Ejercicio 7
#Use for loop to iterate from 0 to 100 and print only even numbers
print("Ejercicio 7:")
for num in range(0, 101):
    if num % 2 == 0:
        print(num)

#Ejercicio 8
#Use for loop to iterate from 0 to 100 and print only odd numbers
print("Ejercicio 8:")
for num in range(0, 101):
    if num % 2 != 0:
        print(num)
