frutas = ("manzana", "platano", "fresa")
vegetales = ("zanahoria", "brocoli", "espinaca")
producto_animal = ("leche", "queso", "huevo")
food_stuff_tp = frutas + vegetales + producto_animal
print(food_stuff_tp)
food_stuff_list = list(food_stuff_tp)
tupla_mitad = food_stuff_tp[(len(food_stuff_tp)-1)//2 : len(food_stuff_tp)// 2 + 1]
print(tupla_mitad)
primerosTP = food_stuff_list[:3]
ultimosTP = food_stuff_list[-3:]
print()
print(primerosTP)
print(ultimosTP)
del food_stuff_tp

item = "manzana"
item_com = item in food_stuff_list
print(item)

print("----------------")
paises_nordicos = ("Dinamarca","Finlandia", "Islandia", "Noruega", "Suecia")
itemP = "Estonia"
paisNordico = itemP in paises_nordicos
print(paisNordico)
itemP = "Islandia"
paisNordico = itemP in paises_nordicos
print(paisNordico)