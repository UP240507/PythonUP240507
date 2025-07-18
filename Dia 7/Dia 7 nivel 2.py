#Ejercicio 1
#Join A and B
print("Ejercicio 1:")
A = {19, 22, 24, 20, 25, 26, 10}
B = {19, 22, 20, 25, 26, 24, 28, 27}

#Ejercicio 2
#Find A intersection B
print("Ejercicio 2:")
interseccion = A.intersection(B)
print(interseccion)

#Ejercicio 3
#Is A subset of B
print("Ejercicio 3:")
print(A.issubset(B))

#Ejercicio 4
#Are A and B disjoint sets
print("Ejercicio 4:")
print(A.isdisjoint(B))

#Ejercicio 5
#Join A with B and B with A
print("Ejercicio 5:")
UnionA = A.union(B)
UnionB = B.union(A)
print(UnionA)
print(UnionB)

#Ejercicio 6
#What is the symmetric difference between A and B
#Delete the sets completely
print("Ejercicio 6:")
print(A.symmetric_difference(B))
del A
del B